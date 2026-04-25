import pandas as pd
from main import AnomalyDetector


def test_anomaly_logic():
    # שלב א': הכנת נתונים מזויפים
    # הפעם נשים מספיק נתונים "תקינים" כדי שהממוצע לא ייהרס מנתון אחד
    fake_data = pd.DataFrame({
        'timestamp': ['t1', 't2', 't3', 't4', 't5', 't6', 't7', 't8', 't9', 't10', 't11', 't12', 't13', 't14', 't15',
                      't16'],
        'value': [10, 11, 10, 12, 10, 11, 10, 12, 10, 11, 10, 12, 10, 11, 10, 1000]
    })

    # שלב ב': הפעלת המנוע
    detector = AnomalyDetector(fake_data)
    result = detector.detect_anomalies()

    # שלב ג': וידוא
    assert len(result) == 1, "Error: Should find exactly one anomaly"
    assert result['value'].iloc[0] == 1000, "Error: The anomaly value should be 1000"