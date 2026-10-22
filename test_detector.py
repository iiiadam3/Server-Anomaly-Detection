import pandas as pd
import pytest
from main import AnomalyDetector, DataLoader


def test_anomaly_detected():
    """Verify that an extreme spike is flagged as an anomaly."""
    fake_data = pd.DataFrame({
        'timestamp': [f't{i}' for i in range(1, 17)],
        'value': [10, 11, 10, 12, 10, 11, 10, 12, 10, 11, 10, 12, 10, 11, 10, 1000]
    })

    detector = AnomalyDetector(fake_data)
    result = detector.detect_anomalies()

    assert len(result) == 1, "Error: Should find exactly one anomaly"
    assert result['value'].iloc[0] == 1000, "Error: The anomaly value should be 1000"


def test_no_anomalies_in_normal_data():
    """Verify that stable metrics return an empty DataFrame."""
    normal_data = pd.DataFrame({
        'timestamp': [f't{i}' for i in range(1, 11)],
        'value': [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
    })

    detector = AnomalyDetector(normal_data)
    result = detector.detect_anomalies()

    assert result.empty, "Error: Should not detect anomalies in constant data"


def test_missing_file_raises_error():
    """Verify that DataLoader raises FileNotFoundError for non-existent files."""
    loader = DataLoader("non_existent_file.csv")
    with pytest.raises(FileNotFoundError):
        loader.load_data()