import os 
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format = '[%(asctime)s]: %(message)s:')

project_name = 'WasteDetection'


list_of_files = [
    ".github/workflows/.gitkeep",
    "data/.gitkeep",
    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_validation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/constant/__init__.py",
    f"{project_name}/constant/training_pipeline/__init__.py",
    f"{project_name}/constant/application.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/entity/artifacts.entity.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/training_pipeline.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/main_utils.py",
    "research/trials.ipynb",
    "templates/index.html",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py"

]


for file in list_of_files:
    file_path = Path(file)

    file_path.parent.mkdir(parents=True,exist_ok=True)

    if not file_path.exists():
        file_path.touch()
        logging.info(f"Created: {file_path}")
    else:
        logging.info(f"Already exists: {file_path}")