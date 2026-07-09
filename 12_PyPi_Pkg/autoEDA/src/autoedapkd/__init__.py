from .autoEDA import perform_eda

__all__ = ['perform_eda',] 

def main() -> None:
    """Main entry point for the command-line interface."""
    import argparse
    import pandas as pd
    parser = argparse.ArgumentParser(description="Automated Exploratory Data Analysis")
    parser.add_argument("file_path", help="Path to the CSV file")
    parser.add_argument("--target", help="Optional target column name", default=None)
    
    args = parser.parse_args()
    
    try:
        print(f"\nLoading dataset from: {args.file_path}")
        df = pd.read_csv(args.file_path)
        
        # Call the EDA function
        perform_eda(df, args.target)
        
    except FileNotFoundError:
        print(f"Error: File not found at {args.file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")