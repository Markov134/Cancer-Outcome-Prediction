from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    roc_curve,
    classification_report
)

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.tree import DecisionTreeClassifier

import pandas as pd
import matplotlib.pyplot as plt

def create_preprocessor(df):
    # Make a copy of the dataset so we don't alter original.
    df_copy = df.copy()

    # We do this to parse the Date.
    # Machine Learning cannot handle 2024-05-04 so we split it up.
    df_copy['Diagnosis_Date'] = pd.to_datetime(
        df_copy['Diagnosis_Date'])

    df_copy['Diagnosis_Year'] = df_copy['Diagnosis_Date'].dt.year
    df_copy['Diagnosis_Month'] = df_copy['Diagnosis_Date'].dt.month
    df_copy['Diagnosis_Day'] = df_copy['Diagnosis_Date'].dt.day

    # We create the preprocessing pipelines for both numerical and categorical data.
    numeric_features = [
        'Age',
        'Survival_Months',
        'Diagnosis_Year',
        'Diagnosis_Month',
        'Diagnosis_Day'
    ]

    # The SimpleImputer handles missing values
    # The StandardScaler standardizes numerical features.
    numeric_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='median')),
        ('scaler', StandardScaler())])

    # Categorical is data that aren't numeric.
    categorical_features = [
        "Gender",
        "State",
        "City",
        "Cancer_Type",
        "Stage",
        "Treatment_Type",
    ]

    # One-Hot Encoding is basically turning the strings into binary
    categorical_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
        ('onehot', OneHotEncoder(handle_unknown='ignore'))])

    # Puts everything together
    preprocessor = ColumnTransformer(
        transformers=[
            ('numerical', numeric_transformer, numeric_features),
            ('categorical', categorical_transformer, categorical_features)])

    columns_to_drop=[
        "Patient_ID",
        'Diagnosis_Date',
        "Hospital_Name"
    ]

    df_copy = df_copy.drop(columns=columns_to_drop)

    X = df_copy.drop('Status', axis=1)
    y = df_copy['Status']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    print("\nTrain Shape:", X_train.shape)
    print("Test Shape :", X_test.shape)

    model = {
        "Logistic Regression":
            LogisticRegression(max_iter=500),

        "Decision Tree":
            DecisionTreeClassifier(random_state=42),

        "Random Forest":
            RandomForestClassifier(
                n_estimators=200,
                random_state=42
            ),

        "Gradient Boosting":
            GradientBoostingClassifier(
                random_state=42
            )
    }

    results = []

    plt.figure(figsize=(12, 8))

    for name, model in model.items():

        pipeline = Pipeline([
            ('preprocessor', preprocessor),
            ('model', model)
        ])

        # Train
        pipeline.fit(X_train, y_train)

        # Prediction
        y_pred = pipeline.predict(X_test)

        # Probability
        y_prob = pipeline.predict_proba(X_test)[:, 1]

        # Metrics
        accuracy = accuracy_score(y_test, y_pred)

        precision = precision_score(
            y_test,
            y_pred,
            average='weighted'
        )

        recall = recall_score(
            y_test,
            y_pred,
            average='weighted'
        )

        f1 = f1_score(
            y_test,
            y_pred,
            average='weighted'
        )

        roc_auc = roc_auc_score(
            y_test,
            y_prob
        )

        results.append([
            name,
            accuracy,
            precision,
            recall,
            f1,
            roc_auc
        ])

        print("\n" + "=" * 50)
        print(name)
        print("=" * 50)

        print("\nAccuracy :", round(accuracy, 4))
        print("Precision:", round(precision, 4))
        print("Recall   :", round(recall, 4))
        print("F1 Score :", round(f1, 4))
        print("ROC AUC  :", round(roc_auc, 4))

        print("\nClassification Report:\n")
        print(classification_report(y_test, y_pred))

        # ROC Curve
        fpr, tpr, _ = roc_curve(y_test, y_prob, pos_label='Deceased')

        plt.plot(
            fpr,
            tpr,
            lw=2,
            label=f'{name} (AUC={roc_auc:.3f})'
        )

    plt.plot(
        [0, 1],
        [0, 1],
        linestyle='--'
    )

    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title("ROC Curve Comparison")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("outputs/figures/ROC_Curve_Comparison.png")
    plt.show()

    results_df = pd.DataFrame(
        results,
        columns=[
            "Model",
            "Accuracy",
            "Precision",
            "Recall",
            "F1 Score",
            "ROC AUC"
        ]
    )

    results_df = results_df.sort_values(
        by='ROC AUC',
        ascending=False
    )

    print("\n")
    print("=" * 70)
    print("MODEL COMPARISON")
    print("=" * 70)

    print(results_df)

    best_model = results_df.iloc[0]

    print("\nBest Model:")
    print(best_model)