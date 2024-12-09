import pandas as pd

def read_input_file(file_path: str) -> list:
    """Reads the car input file and returns a list of dictionaries."""
    df = pd.read_csv(file_path, dtype=str)  # Ensure all data is read as strings
    return df.to_dict(orient="records")


def read_output_file(file_path: str) -> dict:
    """Reads the car output file and returns a dictionary."""
    output_data = {}
    with open(file_path, 'r', encoding="utf-8") as file:
        for line in file.readlines():
            reg, valuation = line.strip().split(",")
            output_data[reg] = str(valuation)
    return output_data