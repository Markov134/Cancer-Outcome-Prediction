import kagglehub

def download_dataset():
    # Download latest version
    path = kagglehub.dataset_download("ashyou09/india-cancer-patient-dataset-2022-2025")
    print("Path to dataset files:", path)
    return path

