from pathlib import Path
import pandas as pd


class DataLoader:
    """Handles loading telemetry data from CSV files."""

    def __init__(self, file_path: str | Path):
        self.file_path = Path(file_path)

    def load_data(self) -> pd.DataFrame:
        if not self.file_path.exists():
            raise FileNotFoundError(f"Data file not found: {self.file_path}")
        return pd.read_csv(self.file_path)


class AnomalyDetector:
    """Detects anomalies in time-series data using Z-Score thresholding."""

    def __init__(self, df: pd.DataFrame, threshold_std: float = 3.0):
        self.df = df
        self.threshold_std = threshold_std

    def detect_anomalies(self) -> pd.DataFrame:
        average_cpu = self.df['value'].mean()
        cpu_std = self.df['value'].std()

        if cpu_std == 0 or pd.isna(cpu_std):
            return pd.DataFrame(columns=self.df.columns)

        threshold = average_cpu + (self.threshold_std * cpu_std)
        anomalies = self.df[self.df['value'] > threshold]
        return anomalies


if __name__ == "__main__":
    loader = DataLoader('ec2_cpu_utilization_24ae8d.csv')
    my_data = loader.load_data()

    detector = AnomalyDetector(my_data)
    found_anomalies = detector.detect_anomalies()

    print(f"Average CPU: {my_data['value'].mean():.5f}")
    print("\n--- Anomalies Detected ---")
    print(found_anomalies)