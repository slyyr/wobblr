import pandas as pd

def load_sensor_data(file_path):
    data = pd.read_csv(file_path)
    return data

if __name__ == "__main__":
    df = load_sensor_data("../../data/raw/sensor_data.csv")

    print(df["temperature"])