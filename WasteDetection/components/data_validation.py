import os,sys
import shutil
from WasteDetection.logger import logging
from WasteDetection.exception import AppException
from WasteDetection.entity.config_entity import DataValidationConfig
from WasteDetection.entity.artifacts_entity import (DataIngestionArtifact, DataValidationArtifact)



class DataValidation:
    def __init__(self, data_ingestion_artifact: DataIngestionArtifact,
                 data_validation_config: DataValidationConfig
                 ):
        try:
            self.data_ingestion_artifact = data_ingestion_artifact
            self.data_validation_config = data_validation_config
        except Exception as e:
            raise AppException(e, sys)
        
    def validate_all_files_exist(self):
        try:
            validation_status = None
            all_files = os.listdir(self.data_ingestion_artifact.feature_zip_file_path)
            for file in all_files:
                if file not in self.data_validation_config.required_file_list:
                    validation_status = False
                    os.makedirs(self.data_validation_config.data_validation_dir,exist_ok=True)
                    with open(self.data_validation_config.valid_status_file_dir,'w') as f:
                        f.write(f"Validation staus: {validation_status}")
                else:
                    validation_status = True
                    os.makedirs(self.data_validation_config.data_validation_dir,exist_ok=True)
                    with open(self.data_validation_config.valid_status_file_dir,'w') as f:
                        f.write(f"Validation status: {validation_status}")
            return validation_status
        except Exception as e:
            raise AppException(e,sys)
        
    def initiate_data_validation(self):
        logging.info("Entered intiate_data_validation method")
        try:
            status = self.validate_all_files_exist()
            data_validation_artifact = DataValidationArtifact(
                data_validation_status=status)
            logging.info("Exited intiate_data_validation method")
            logging.info(f"DataValidationArtifact : {data_validation_artifact}")
            
            file_path = os.path.abspath(self.data_ingestion_artifact.data_zip_file_path)

            if status:
                shutil.copy(file_path,os.getcwd())
            return data_validation_artifact
        except Exception as e:
            raise AppException(e,sys)