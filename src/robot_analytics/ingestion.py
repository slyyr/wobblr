import pandas as pd

def load_sensor_data(file_path):
    data = pd.read_csv(file_path)
    return data

if __name__ == "__main__":
    df = load_sensor_data("../../data/raw/sensor_data.csv")

    print("Missing values:")
    print(df.isnull().sum())

    print("\nDuplicate rows:")
    print(df.duplicated().sum())

    dt = df["timestamp"].diff()
    print("\nTime difference:")

    print("min:", dt.min())
    print("max:", dt.max())
    print("mean:", dt.mean())
    print("std:", dt.std())

    print("\nTimestamp monotonic:", df["timestamp"].is_monotonic_increasing)

    sensor_cols = [
        "imu_accel_x",
        "imu_accel_y",
        "imu_accel_z",
        "left_wheel_velocity",
        "right_wheel_velocity",
        "temperature"
    ]

    print("\nSensor statistics:")
    print(df[sensor_cols].describe())

    for col in sensor_cols:
        print(f"\n{col}")
        print("min :", df[col].min())
        print("max :", df[col].max())
        print("mean:", df[col].mean())
        print("std :", df[col].std())