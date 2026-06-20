from preprocessing import *

def main():
    df = load_data()
    dataset_summary(df)
    data_quality_report(df)
    preview_data(df)

if __name__ == "__main__":
    main()
