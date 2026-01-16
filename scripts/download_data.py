import os
import zipfile
from kaggle.api.kaggle_api_extended import KaggleApi

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TARGET_DIR = os.path.join(PROJECT_ROOT, "data")

os.makedirs(TARGET_DIR, exist_ok=True)

api = KaggleApi()
api.authenticate()

dataset = "blastchar/telco-customer-churn"
zip_path = os.path.join(TARGET_DIR, "telco-customer-churn.zip")

if not os.path.exists(zip_path):
    print("Downloading dataset...")
    api.dataset_download_files(dataset, path=TARGET_DIR, unzip=False)
    print("Download complete.")

    print("Extracting dataset...")
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(TARGET_DIR)
    print("Extraction complete.")
else:
    print("Dataset already downloaded and extracted.")