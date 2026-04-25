import pandas as pd
from pathlib import Path
from typing import Union

def load_data(file_path: Union[str, Path]) -> pd.DataFrame:
    """
    Load dataset from a given file path.
    
    Args:
        file_path: Path to the CSV file.
        
    Returns:
        pd.DataFrame containing the data.
    """
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"The data file {path} was not found.")
    
    return pd.read_csv(path)
