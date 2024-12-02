import os,sys
from WasteDetection.logger import logging
from WasteDetection.exception import AppException
from WasteDetection.components.data_ingestion import DataIngestion
from WasteDetection.components.data_validation import DataValidation
from WasteDetection.components.model_trainer import ModelTrainer

from WasteDetection.entity.artifacts_entity import (DataIngestionArtifact,DataValidationArtifact,ModelTrainingArtifact)
from WasteDetection.entity.config_entity import (DataIngestionConfig,DataValidationConfig,ModelTrainingConfig)

class TrainingPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
        self.data_validation_config = DataValidationConfig()
        self.model_training_config = ModelTrainingConfig()


    def start_data_ingestion(self) -> DataIngestionArtifact:
        try:
            logging.info("Starting data ingestion process")
            logging.info("Getting the url")

            data_ingestion = DataIngestion(data_ingestion_config=
                                           self.data_ingestion_config)
            
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()

            logging.info("Data ingestion process completed successfully")
            
            return data_ingestion_artifact
    
        except Exception as e:
            AppException(e,sys) 

    def start_data_validation(self,data_ingestion_artifact: DataIngestionArtifact) -> DataValidationArtifact:
        logging.info("Entering DataValidationArtifact of TrainingPipeline Class")

        try:
            data_validation = DataValidation(data_ingestion_artifact=data_ingestion_artifact,
                                             data_validation_config=self.data_validation_config)
            
            data_validation_artifact = data_validation.initiate_data_validation()

            logging.info("Data Validation process completed successfully")
            
            return data_validation_artifact
        
        except Exception as e:
            raise AppException(e,sys)
        
    def start_model_trainer(self) -> ModelTrainingArtifact:
        logging.info("Entering ModelTrainingArtifact of TrainingPipeline Class")

        try:
            model_trainer = ModelTrainer(
                model_trainer_config= self.model_training_config
            )
            model_trainer_artifact = model_trainer.initiate_model_training()

            return model_trainer_artifact
        
        except Exception as e:
            raise AppException(e,sys)


    def run_pipeline(self)->None:
        try:
            data_ingestion_artifact = self.start_data_ingestion()
            data_validation_artifact = self.start_data_validation(
                data_ingestion_artifact=data_ingestion_artifact
                )
            if data_validation_artifact.data_validation_status == True:
                model_trainer_artifact = self.start_model_trainer()
            
            else:
                raise Exception("Data is not in correct format")
            

        except Exception as e:
            raise AppException(e,sys)
