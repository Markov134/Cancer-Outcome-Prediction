import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style("darkgrid")
plt.rcParams['figure.figsize'] = (12,6)

def plot_age_distribution(df):
    sns.histplot(
        df['Age'],
        bins=20,
        kde=True
    )

    plt.title("Age Distribution")
    plt.ylabel("Number of Patients")
    plt.savefig("outputs/figures/age_distribution.png")
    plt.show()

def plot_cancer_type_distribution(df):
    df['Cancer_Type'].value_counts().plot(kind='bar')
    plt.title("Cancer Type Distribution")
    plt.xlabel("Cancer Type")
    plt.ylabel("Number of Patients")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("outputs/figures/cancer_type_distribution.png")
    plt.show()

def plot_stage_distribution(df):
    sns.countplot(
        x='Stage',
        data=df,
        order=df['Stage'].value_counts().index
    )

    plt.title("Cancer Stage Distribution")
    plt.ylabel("Number of Patients")
    plt.savefig("outputs/figures/stage_distribution.png")
    plt.show()

def plot_treatment_type_distribution(df):
    sns.countplot(
        y='Treatment_Type',
        data=df,
        order=df['Treatment_Type'].value_counts().index
    )

    plt.title("Treatment Type Distribution")
    plt.xlabel("Number of Patients")
    plt.ylabel("Treatment Type")
    plt.tight_layout()
    plt.savefig("outputs/figures/treatment_type_distribution.png")
    plt.show()

def plot_patient_status_distribution(df):
    df['Status'].value_counts().plot(kind='pie', autopct='%1.1f%%')

    plt.title("Patient Status Distribution")
    plt.ylabel("")
    plt.savefig("outputs/figures/patient_status_distribution.png")
    plt.show()

def plot_survival_month_distribution(df):
    sns.histplot(
        df['Survival_Months'],
        bins=25,
        kde=True
    )

    plt.title("Survival Months Distribution")
    plt.xlabel("Months")
    plt.ylabel("Frequency")
    plt.savefig("outputs/figures/survival_month_distribution.png")
    plt.show()

def plot_survival_months_by_cancer_type(df):
    sns.boxplot(
        data=df,
        x="Cancer_Type",
        y="Survival_Months",
        order=df.groupby("Cancer_Type")['Survival_Months'].median().sort_values().index
    )

    plt.xticks(rotation=45)
    plt.title("Survival Months by Cancer Type")
    plt.xlabel("Cancer Type")
    plt.ylabel("Survival Months")
    plt.tight_layout()
    plt.savefig("outputs/figures/survival_months_by_cancer_type.png")
    plt.show()

def plot_survival_months_by_stage(df):
    sns.boxplot(
        data=df,
        x='Stage',
        y='Survival_Months',
        order=df.groupby("Stage")['Survival_Months'].median().sort_values().index
    )

    plt.xticks(rotation=45)
    plt.title("Survival Months by Cancer Stage")
    plt.ylabel("Survival Months")
    plt.tight_layout()
    plt.savefig("outputs/figures/survival_months_by_stage.png")
    plt.show()

def plot_status_by_stage(df):
    sns.countplot(
        data=df,
        x="Stage",
        hue="Status"
    )

    plt.title("Patient Status by Cancer Stage")
    plt.ylabel("Number of Patients")
    plt.savefig("outputs/figures/status_by_stage.png")
    plt.show()
