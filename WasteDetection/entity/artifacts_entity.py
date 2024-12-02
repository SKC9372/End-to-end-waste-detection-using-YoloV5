from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    data_zip_file_path: str 
    feature_zip_file_path: str

@dataclass
class DataValidationArtifact:
    data_validation_status: bool

@dataclass
class ModelTrainingArtifact:
    trained_model_file_path: str