import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s')

project_name = "textSummarizer"

list_of_files = [
    ".github/workflows/.gitkeep" ,  # for CI/CD deploymnet create a yaml file inside this directory,
                                     #inititially keep a .gitkeep empty file to upload to git, else empty folder is not uploaded
                                     # and github actions fails
     f"src/{project_name}/__init__.py", #constructor file  used in Python to define a folder as a package, for importing as a module
     f"src/{project_name}/components/__init__.py",
     f"src/{project_name}/utils/__init__.py",
     f"src/{project_name}/utils/common.py",
     f"src/{project_name}/logging/__init__.py",
     f"src/{project_name}/config/__init__.py",
     f"src/{project_name}/config/configuration.py",
     f"src/{project_name}/pipeline/__init__.py",
     f"src/{project_name}/entity/__init__.py",
     f"src/{project_name}/constants/__init__.py",
     "config/config.yaml",
     "params.yaml",
     "app.py",
     "main.py",
     "requirements.txt",
     "Dockerfile",
     "setup.py",
     "research/trial.ipynb",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir,filename = os.path.split(filepath)
    
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the {filename}")
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        logging.info(f"Creating empty file: {filepath}")
        with open(filepath, "w") as f:
            pass
    
    else:
        logging.info(f"File {filename} already exists")


