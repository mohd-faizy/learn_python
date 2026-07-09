import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


def perform_eda(df: pd.DataFrame, target_column: str = None):
    """Performs automated Exploratory Data Analysis (EDA) on a pandas DataFrame.

    - Displays basic info and missing values.
    - Shows descriptive statistics.
    - Generates correlation heatmaps, feature distributions, and boxplots against a target column.
    """
    print("=" * 50, "\nAUTOMATED EXPLORATORY DATA ANALYSIS (EDA)\n", "=" * 50)

    # 1. Dataset structure and summary
    print("\n--- 1. Dataset Info ---")
    df.info()

    # 2. Check for missing/null values
    missing = df.isnull().sum()
    print("\n--- 2. Missing Values ---")
    print(missing[missing > 0] if missing.any() else "No missing values.")

    # 3. Descriptive statistics
    print("\n--- 3. Descriptive Statistics ---")
    num_cols = df.select_dtypes(include="number").columns
    cat_cols = df.select_dtypes(include=["object", "category"]).columns

    if len(num_cols) > 0:
        print("\nNumerical Variables:")
        print(df[num_cols].describe().T)

    if len(cat_cols) > 0:
        print("\nCategorical Variables:")
        print(df[cat_cols].describe().T)

    # 4. Visualizations
    print("\n--- 4. Visualizations ---")
    sns.set_theme(style="whitegrid")

    # Plot correlation heatmap if multiple numerical columns exist
    if len(num_cols) > 1:
        plt.figure(figsize=(8, 6))
        sns.heatmap(df[num_cols].corr(), annot=True, cmap="coolwarm", fmt=".2f")
        plt.title("Correlation Heatmap")
        plt.tight_layout()
        plt.show()

    # Plot distributions (histograms) for numerical columns
    for col in num_cols[:3]:
        plt.figure(figsize=(6, 4))
        sns.histplot(df[col], kde=True).set_title(f"Distribution of {col}")
        plt.tight_layout()
        plt.show()

    # Plot boxplots to identify outliers in numerical columns
    for col in num_cols[:3]:
        plt.figure(figsize=(6, 4))
        sns.boxplot(y=df[col]).set_title(f"Boxplot of {col}")
        plt.tight_layout()
        plt.show()

    # Plot count/frequency plots for categorical columns
    for col in cat_cols[:3]:
        plt.figure(figsize=(6, 4))
        sns.countplot(x=col, data=df, order=df[col].value_counts().index).set_title(f"Frequency of {col}")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    print("\nEDA Completed successfully.")


if __name__ == "__main__":
    # Generate sample data for testing the EDA function
    np.random.seed(42)
    sample_data = pd.DataFrame(
        {
            "Age": np.random.randint(18, 65, 100),
            "Salary": np.random.normal(50000, 15000, 100),
            "Experience": np.random.randint(0, 20, 100),
            "Department": np.random.choice(
                ["IT", "HR", "Finance", "Marketing"], 100
            ),
        }
      )
    # Inject some missing values into 'Age' to test missing value detection
    sample_data.loc[10:15, "Age"] = np.nan

    # Run the EDA
    perform_eda(sample_data, target_column="Department")

