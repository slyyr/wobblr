import pandas as pd
import matplotlib.pyplot as plt

# function to loading the csv data
def load_sensor_data(file_path):
    data = pd.read_csv(file_path)
    return data

if __name__ == "__main__":
    df = load_sensor_data("../../data/raw/sensor_data.csv")

    # checking for missing values
    print("Missing values:")
    print(df.isnull().sum())

    # checking for duplicate rows
    print("\nDuplicate rows:")
    print(df.duplicated().sum())

    # checking other details
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

    WHEEL_BASE = 0.5

    df["linear_velocity"] = (df["left_wheel_velocity"] + df["right_wheel_velocity"]) / 2
    df["angular_velocity"] = (df["right_wheel_velocity"] - df["left_wheel_velocity"]) / WHEEL_BASE

    print(f"Mean of linear velocity : {df['linear_velocity'].mean()}")
    print(f"STD of linear velocity : {df['linear_velocity'].std()}")
    print((f"Max of linear velocity : {df['linear_velocity'].max()}"))
    print(f"Mean of angular velocity : {df['angular_velocity'].mean()}")
    print(f"Max of angular velocity : {df['angular_velocity'].abs().max()}")
    print(f"STD of angular velocity : {df['angular_velocity'].std()}")

    # to find linear acceleration

    df["linear_acceleration"] = df['linear_velocity'].diff() / df["timestamp"].diff()

    # four statistics of linear acceleration

    print("Mean acceleration:", df["linear_acceleration"].mean())
    print("STD acceleration:", df["linear_acceleration"].std())
    print("Min acceleration:", df["linear_acceleration"].min())
    print("Max acceleration:", df["linear_acceleration"].max())

    # some properties of acceleration to be checked

    print("acceleration qantiles:")
    print(df["linear_acceleration"].quantile([0.01, 0.05, 0.50, 0.95, 0.99]))

    print("\nExtreme acceleration:")
    print(df["linear_acceleration"].abs().nlargest(10))

    print("\nMissing acceleration values:")
    print(df["linear_acceleration"].isnull().sum())


    # using matplotlib for plotting the graph of values

    plt.plot(df["timestamp"], df["linear_acceleration"], color="green")
    plt.xlabel("Time", color="red", fontweight="bold")
    plt.ylabel("Linear acceleration (m/s²)", color="red", fontweight="bold")
    plt.title("Raw Linear Acceleration", color="red", fontweight="bold", fontsize=15)
    plt.show()

    # adding subplots

    fig, ax1 = plt.subplots()

    ax1.plot(df["timestamp"], df["linear_velocity"])
    ax1.set_xlabel("Time (s)")
    ax1.set_ylabel("Linear velocity (m/s)")

    # cloning one of the subplot and adding it with ax1 plot
    ax2 = ax1.twinx()
    ax2.plot(df["timestamp"], df["linear_acceleration"],color="red")
    ax2.set_ylabel("Linear acceleration (m/s²)")

    plt.title("Velocity and Acceleration")
    plt.show()