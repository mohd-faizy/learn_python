import pandas as pd
import seaborn as sns
from autoedapkd import perform_eda

def main():
    print("Loading the Titanic dataset for demonstration...")
    # We use seaborn to load a sample dataset
    df = sns.load_dataset("titanic")
    
    print("Performing EDA using autoeda-faizymohd...")
    # The function expects a pandas DataFrame and an optional target_column
    perform_eda(df, target_column="survived")
    
    print("EDA completed successfully!")

if __name__ == "__main__":
    main()
