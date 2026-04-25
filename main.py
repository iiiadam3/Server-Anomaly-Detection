import pandas as pd


class DataLoader:
    def __init__(self, file_path):
        # שומרים את נתיב הקובץ בתוך האובייקט
        self.file_path = file_path

    def load_data(self):
        # קוראים את הקובץ באמצעות המשתנה מה"תיק" (self.file_path)
        # ושומרים למשתנה מקומי זמני בשם df
        df = pd.read_csv(self.file_path)
        # מחזירים אותו החוצה
        return df


class AnomalyDetector:
    def __init__(self, df):
        # שומרים את הטבלה בתוך האובייקט
        self.df = df

    def detect_anomalies(self):
        # המשימה שלך: תעתיק לפה את הלוגיקה של חישוב הממוצע, סטיית התקן והסינון
        # שים לב שאתה צריך להשתמש ב- self.df במקום סתם df
        average_cpu = self.df['value'].mean()
        print("\n-----Average CPU utilization-----")
        print(f"Average CPU: {average_cpu:.5f}")

        cpu_std = self.df['value'].std()
        threshold = average_cpu + (3 * cpu_std)

        anomalies = self.df[self.df['value'] > threshold]
        print("--- Anomalies Detected ---")
        return anomalies


# --- כאן מתחיל החלק שמריץ את התוכנית בפועל ---

if __name__ == "__main__":
    # 1. טעינת הנתונים דרך המחלקה הראשונה
    loader = DataLoader('ec2_cpu_utilization_24ae8d.csv')
    my_data = loader.load_data()

    # 2. זיהוי חריגות דרך המחלקה השנייה
    detector = AnomalyDetector(my_data)
    found_anomalies = detector.detect_anomalies()

    # 3. הדפסה
    print("--- Anomalies Detected (OOP Version) ---")
    print(found_anomalies)