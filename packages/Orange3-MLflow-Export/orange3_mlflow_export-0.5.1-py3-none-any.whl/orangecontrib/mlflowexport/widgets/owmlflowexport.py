import tempfile
import zipfile
import os
from pathlib import Path

import mlflow
import mlflow.pyfunc
import mlflow.sklearn
import numpy as np
from Orange.base import Model
from Orange.data import Table
from Orange.widgets.utils.save.owsavebase import OWSaveBase
from Orange.widgets.utils.widgetpreview import WidgetPreview
from Orange.widgets.widget import Input, Msg


class OrangeModelWrapper(mlflow.pyfunc.PythonModel):
    """
    A wrapper class that packages Orange models with their preprocessing steps
    for MLFlow deployment.
    """
    
    def __init__(self, orange_model):
        self.orange_model = orange_model
        self.model_domain = orange_model.domain
        # Store the original training domain for proper preprocessing
        self.original_domain = orange_model.original_domain if hasattr(orange_model, 'original_domain') else orange_model.domain
        
    def predict(self, context, model_input):
        """
        Apply the Orange model including preprocessing to input data.
        
        Args:
            context: MLFlow context
            model_input: pandas DataFrame, list, or numpy array with input data
            
        Returns:
            numpy array with predictions
        """
        from Orange.data import Table, Domain, ContinuousVariable, DiscreteVariable
        import pandas as pd
        import numpy as np

        # Handle different input types
        if isinstance(model_input, list):
            # Convert list to numpy array
            data_array = np.array(model_input)
            if data_array.ndim == 1:
                data_array = data_array.reshape(1, -1)
        elif isinstance(model_input, pd.DataFrame):
            data_array = model_input.values
        elif isinstance(model_input, np.ndarray):
            if model_input.ndim == 1:
                data_array = model_input.reshape(1, -1)
            else:
                data_array = model_input
        else:
            # Try to convert to numpy array
            data_array = np.array(model_input)
            if data_array.ndim == 1:
                data_array = data_array.reshape(1, -1)
        
        # Create a simple domain with continuous variables matching input size
        # The Orange model will handle the domain transformation internally
        n_features = data_array.shape[1]
        attrs = [ContinuousVariable(f"x{i}") for i in range(n_features)]
        domain = Domain(attrs)
        
        # Convert to Orange Table
        orange_table = Table.from_numpy(domain, data_array)
        
        # Apply the model (which includes preprocessing via domain transformation)
        try:
            # Call model directly - it handles domain transformation internally
            predictions = self.orange_model(orange_table)
            
            # Handle different prediction formats
            if hasattr(predictions, 'shape') and len(predictions.shape) > 1:
                # Classification with probabilities
                return predictions
            else:
                # Regression or classification without probabilities
                return np.array(predictions).reshape(-1, 1)
                
        except Exception as e:
            raise ValueError(f"Prediction failed: {str(e)}")
    
    def get_model_metadata(self):
        """Get metadata about the wrapped model."""
        metadata = {
            "model_type": type(self.orange_model).__name__,
            "model_name": getattr(self.orange_model, 'name', 'Orange Model'),
            "domain_attributes": [attr.name for attr in self.model_domain.attributes],
        }
        
        if self.model_domain.class_var:
            metadata["target_variable"] = self.model_domain.class_var.name
            if self.model_domain.class_var.is_discrete:
                metadata["target_classes"] = list(self.model_domain.class_var.values)
                metadata["model_task"] = "classification"
            else:
                metadata["model_task"] = "regression"
        
        return metadata


class OWMLFlowExport(OWSaveBase):
    """
    Export Orange models to MLFlow format with preprocessing steps included.
    """
    name = "MLFlow Export"
    description = "Export a trained model with preprocessing to MLFlow format."
    icon = "icons/SaveModel.svg"
    priority = 3100
    keywords = "mlflow, export, model, save, preprocessing"
    
    class Inputs:
        model = Input("Model", Model)
        data = Input("Data", Table)  # Optional: for capturing preprocessing pipeline
    
    class Warning(OWSaveBase.Warning):
        no_preprocessing = Msg("No preprocessing steps detected in the model")
        export_failed = Msg("MLFlow export failed: {}")
    
    class Information(OWSaveBase.Information):
        export_success = Msg("Model exported successfully to MLFlow format")
        preprocessing_included = Msg("Preprocessing steps included in export")
    
    filters = ["MLFlow Model Archive (*.zip)"]
    
    def __init__(self):
        super().__init__()
        self.model = None
        self.sample_data = None
        self.last_export_path = None
    
    @Inputs.model
    def set_model(self, model):
        """Set the model to be exported."""
        self.model = model
        self.data = model  # For compatibility with OWSaveBase
        self.on_new_input()
        
        if model:
            self.Information.preprocessing_included()
    
    @Inputs.data
    def set_sample_data(self, data):
        """Optional: Set sample data for testing the model export."""
        self.sample_data = data
    
    def do_save(self):
        """Export the model to MLFlow format as a zip archive."""
        if not self.model:
            return
        
        # Check if filename is set
        if not hasattr(self, 'filename') or not self.filename:
            self.Warning.export_failed("No filename specified")
            return
        
        self.Warning.clear()
        self.Information.clear()
        
        try:
            # Create a wrapper for the Orange model
            wrapped_model = OrangeModelWrapper(self.model)
            
            # Get model metadata
            metadata = wrapped_model.get_model_metadata()
            
            # Set up output path - change extension to .zip
            output_path = Path(self.filename)
            if output_path.suffix not in ['.zip', '.mlflow']:
                output_path = output_path.with_suffix('.zip')
            elif output_path.suffix == '.mlflow':
                # Replace .mlflow with .zip
                output_path = output_path.with_suffix('.zip')
            
            # Create two temporary directories - one for MLFlow tracking, one for the model
            with tempfile.TemporaryDirectory() as temp_tracking_dir:
                with tempfile.TemporaryDirectory() as temp_model_dir:
                    mlflow.set_tracking_uri(f"file://{temp_tracking_dir}")
                    
                    # Create a default experiment if none exists
                    try:
                        experiment = mlflow.get_experiment_by_name("Default")
                        experiment_id = experiment.experiment_id
                    except Exception:
                        experiment_id = mlflow.create_experiment("Default")
                    
                    # Set the experiment explicitly
                    mlflow.set_experiment(experiment_id=experiment_id)
                    
                    # Start an MLFlow run
                    with mlflow.start_run():
                        # Log the model with its preprocessing pipeline
                        conda_env = {
                            'channels': ['defaults', 'conda-forge'],
                            'dependencies': [
                                'python=3.12',
                                'pyqt',
                                'orange3',
                                'orange-spectroscopy',
                                'numpy',
                                'pandas',
                                'scikit-learn',
                                'cloudpickle',
                                'pip',
                                {
                                    'pip': [
                                        'mlflow'
                                    ]
                                }
                            ],
                            'name': 'orange_mlflow_env'
                        }
                        
                        # Create signature if we have sample data
                        signature = None
                        if self.sample_data:
                            try:
                                # Create a sample prediction to infer signature
                                import pandas as pd
                                
                                # Convert Orange Table to pandas DataFrame for signature
                                sample_df = self._orange_to_pandas(self.sample_data[:5])
                                
                                # Get predictions
                                sample_predictions = wrapped_model.predict(None, sample_df)
                                
                                # Infer signature
                                signature = mlflow.models.infer_signature(
                                    sample_df, 
                                    sample_predictions
                                )
                            except Exception as e:
                                print(f"Could not infer signature: {e}")
                        
                        # Log the model - MLflow uses cloudpickle by default to serialize Python models
                        # This embeds the OrangeModelWrapper class in the model artifact
                        mlflow.pyfunc.log_model(
                            artifact_path="orange_model",
                            python_model=wrapped_model,
                            conda_env=conda_env,
                            signature=signature,
                            registered_model_name=None,
                            input_example=self._orange_to_pandas(self.sample_data[:1]) if self.sample_data else None
                        )
                        
                        # Log additional metadata
                        mlflow.log_params(metadata)
                        
                        # Log model metrics if available
                        if hasattr(self.model, 'score') and self.sample_data:
                            try:
                                score = self.model.score(self.sample_data)
                                mlflow.log_metric("model_score", score)
                            except:
                                pass
                        
                        # Save model to temporary directory
                        model_save_path = os.path.join(temp_model_dir, "model")
                        mlflow.pyfunc.save_model(
                            path=model_save_path,
                            python_model=wrapped_model,
                            conda_env=conda_env,
                            signature=signature,
                            input_example=self._orange_to_pandas(self.sample_data[:1]) if self.sample_data else None
                        )
                        
                        # Create zip archive with all model files at the root
                        with zipfile.ZipFile(str(output_path), 'w', zipfile.ZIP_DEFLATED) as zipf:
                            # Walk through the model directory and add all files to the zip
                            for root, dirs, files in os.walk(model_save_path):
                                for file in files:
                                    file_path = os.path.join(root, file)
                                    # Calculate the archive name - files should be at root of zip
                                    arcname = os.path.relpath(file_path, model_save_path)
                                    zipf.write(file_path, arcname)
            
            self.last_export_path = str(output_path)
            self.Information.export_success()
            
            # Print export details
            print(f"\nModel exported successfully to: {output_path}")
            print(f"Model type: {metadata.get('model_task', 'unknown')}")
            print(f"Input features: {metadata.get('domain_attributes', [])}")
            if 'target_variable' in metadata:
                print(f"Target variable: {metadata['target_variable']}")
            if 'target_classes' in metadata:
                print(f"Target classes: {metadata['target_classes']}")
            
            # Provide usage instructions
            print("\nTo load and use this model:")
            print(f"  1. Unzip the archive: unzip {output_path}")
            print(f"  2. Load the model:")
            print(f"     import mlflow")
            print(f"     model = mlflow.pyfunc.load_model('.')")
            print(f"     predictions = model.predict(data)")
            
        except Exception as e:
            self.Warning.export_failed(str(e))
            raise
    
    def _orange_to_pandas(self, orange_table):
        """Convert Orange Table to pandas DataFrame."""
        import pandas as pd
        
        if orange_table is None or len(orange_table) == 0:
            return None
        
        # Extract data
        data = orange_table.X
        
        # Create DataFrame with default column names (0, 1, 2, ..., n)
        df = pd.DataFrame(data)
        
        return df
    
    def get_save_filename(self):
        """Override to set default extension."""
        result = super().get_save_filename()
        if isinstance(result, tuple):
            filename, selected_filter = result
            # Always add .zip extension if not present
            if filename and not filename.endswith('.zip'):
                filename += '.zip'
            return filename, selected_filter
        else:
            # Handle case where only filename is returned
            filename = result
            if filename and not filename.endswith('.zip'):
                filename += '.zip'
            return filename


if __name__ == "__main__":
    # Example usage with a simple model
    import Orange
    from Orange.classification import LogisticRegressionLearner
    from Orange.preprocess import Normalize, Continuize, Impute
    from Orange.preprocess import preprocess
    
    # Load sample data
    iris = Orange.data.Table("iris")
    
    # Create a preprocessing pipeline
    preprocessor = preprocess.PreprocessorList([
        Continuize(),
        Impute(),
        Normalize()
    ])
    
    # Apply preprocessing and train a model
    preprocessed_data = preprocessor(iris)
    learner = LogisticRegressionLearner()
    model = learner(preprocessed_data)
    
    # The model now includes the preprocessing steps in its domain transformation
    
    # Run the widget
    WidgetPreview(OWMLFlowExport).run(
        set_model=model,
        set_sample_data=iris
    )