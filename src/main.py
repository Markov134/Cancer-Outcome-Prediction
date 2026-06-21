from preprocessing import *
from visualization import *

def main():
    df = load_data()
    dataset_summary(df)
    data_quality_report(df)
    preview_data(df)
    #plot_age_distribution(df)
    #plot_cancer_type_distribution(df)
    #plot_stage_distribution(df)
    #plot_treatment_type_distribution(df)
    #plot_survival_month_distribution(df)
    #plot_patient_status_distribution(df)
    #plot_survival_months_by_cancer_type(df)
    #plot_survival_months_by_stage(df)
    #plot_status_by_stage(df)

if __name__ == "__main__":
    main()
