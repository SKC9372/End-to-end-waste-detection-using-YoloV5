import os,sys
import yaml
from WasteDetection.utils.main_utils import read_yaml_file
from WasteDetection.logger import logging
from WasteDetection.exception import AppException
from WasteDetection.entity.config_entity import ModelTrainingConfig
from WasteDetection.entity.artifacts_entity import ModelTrainingArtifact


class ModelTrainer:
    def __init__(self,model_trainer_config:ModelTrainingConfig):
        self.model_trainer_config = model_trainer_config

    
    def initiate_model_training(self):
        logging.info("Enteres Model Trainer class of model_trainer")
        try:
            logging.info("Unzipping Data")
            os.system("unzip data.zip")
            os.system("rm data.zip")

            with open('data.yaml', 'r') as f:
                      num_classes = str(yaml.safe_load(f)['nc'])

            model_config_file_name = self.model_trainer_config.weight_name.split('.')[0]
            print(model_config_file_name)

            config = read_yaml_file(f"yolov5/models/{model_config_file_name}.yaml")

            config['nc'] = num_classes

            with open(f"yolov5/models/custom_{model_config_file_name}.yaml",'w') as f:
                 yaml.dump(config, f) 

            os.system(f"cd yolov5/ && python train.py --img 416 --batch {self.model_trainer_config.batch_size} --epochs {self.model_trainer_config.no_epochs} --data ../data.yaml --cfg ./models/custom_yolov5s.yaml --weights {self.model_trainer_config.weight_name} --name yolov5s_results  --cache")
            os.system("cp yolov5/runs/train/yolov5s_results/weights/best.pt yolov5/")
            os.makedirs(self.model_trainer_config.model_training_dir, exist_ok=True)
            os.system(f"cp yolov5/runs/train/yolov5s_results/weights/best.pt  {self.model_trainer_config.model_training_dir}/" )

            os.system("rm -rf yolov5/runs")
            os.system("rm -rf train")
            os.system("rm -rf valid")
            os.system("rm -rf data.yaml")
            
            model_trainer_artifact = ModelTrainingArtifact(
                trained_model_file_path="yolov5/best.pt",
            )

            logging.info("Exited initiate_model_trainer method of ModelTrainer class")
            logging.info(f"Model trainer artifact: {model_trainer_artifact}")

            return model_trainer_artifact
    
        except Exception as e:
                raise AppException(e,sys)
        
        
        