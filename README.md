# Automated Server Anomaly Detection Pipeline

## 📌 Overview
An automated, OOP-based Python pipeline designed to detect anomalies in server telemetry data. Using real-world AWS EC2 CPU utilization metrics, the system applies statistical modeling (Z-Score) to flag unusual spikes in CPU usage. 

This project simulates a real-world **Site Reliability Engineering (SRE)** and **Data Validation** workflow, moving from raw data ingestion to automated testing and Continuous Integration (CI/CD).

## 🚀 Features & Architecture
* **Data Engineering:** Processes real-world AWS server metrics using `pandas`.
* **Statistical Modeling:** Implements dynamic Z-Score thresholding (Mean + 3 Standard Deviations) for anomaly detection.
* **Object-Oriented Design (OOP):** Modular and scalable architecture divided into `DataLoader` and `AnomalyDetector` classes.
* **Robust Validation:** Fully unit-tested logic using `pytest` with mocked data sets.
* **CI/CD Pipeline:** Integrated with **GitHub Actions** for automated testing on every push, ensuring code reliability.

## 🛠️ Tech Stack
* **Language:** Python 3.10
* **Data Processing:** Pandas
* **Testing:** Pytest
* **DevOps / CI/CD:** GitHub Actions, Git

## ⚙️ How to Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/iiiadam3/Server-Anomaly-Detection.git

# 2. Install dependencies
pip install pandas pytest

# 3. Run the Anomaly Detector
python main.py

# 4. Run the automated tests
pytest