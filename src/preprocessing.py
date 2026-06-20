import pandas as pd

def load_data():
    """Load the raw cancer dataset."""
    return pd.read_csv("data/raw/india_cancer_patients_2022_2025.csv")

def dataset_summary(df):
    """Displays the basic dataset information."""
    print('Dataset shape:', df.shape)
    print('\n' + '-' * 50)

    print('\nDataset Information')
    df.info()
    print('\n' + '-' * 50)

    print('\nDescriptive Statistics')
    print(df.describe())
    print('\n' + '-' * 50)

def data_quality_report(df):
    """Check data quality report."""
    print('\nMissing Values:')
    print(df.isnull().sum())
    print('\n' + '-' * 50)

    print("\nDuplicate Rows:")
    print(df.duplicated().sum())
    print('\n' + '-' * 50)

def preview_data(df):
    '''Display sample records.'''
    print("\nFirst 5 Rows of Patients:")
    print(df.head())
    print('\n' + '-' * 50)

    print("\nLast 5 Rows of Patients:")
    print(df.tail())