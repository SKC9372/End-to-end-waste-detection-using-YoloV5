import os,sys
from WasteDetection.logger import logging
from WasteDetection.exception import AppException
from WasteDetection.components.data_ingestion import DataIngestion

from WasteDetection.entity.artifacts_entity import DataIngestionArtifact
from WasteDetection.entity.config_entity import DataIngestionConfig

class TrainingPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()

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

    def run_pipeline(self)->None:
        try:
            data_ingestion_artifact = self.start_data_ingestion()

        except Exception as e:
            raise AppException(e,sys)
