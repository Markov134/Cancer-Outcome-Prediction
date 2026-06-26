from preprocessing import *
from visualization import *
from feature_engineering import *

def main():
    df = load_data()
    create_preprocessor(df)

if __name__ == "__main__":
    main()
