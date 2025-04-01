import pandas as pd
import random
from datetime import datetime, timedelta

def generate_anomaly_data(
    num_records=200,
    anomaly_threshold=33.0,
    anomaly_rate=0.05,
    output_file="anomaly_data.csv"
):
    """
    Generate simulated IoT sensor data with injected anomalies.
    
    Parameters:
        num_records (int): Number of sensor records to generate.
        anomaly_threshold (float): Threshold above which a value is considered anomalous (only for temperature).
        anomaly_rate (float): Probability of an anomaly being injected.
        output_file (str): Output CSV file name.
    """
    data = []
    metrics = ["Temperature", "Humidity", "Pressure"]

    for i in range(num_records):
        sensor_id = f"s{i+1}"
        global_id = f"g{i+1}"
        metric = random.choice(metrics)

        if metric == "Temperature":
            value = round(random.uniform(20.0, 40.0), 2)
            is_anomaly = value > anomaly_threshold and random.random() < anomaly_rate
        elif metric == "Humidity":
            value = round(random.uniform(30.0, 80.0), 2)
            is_anomaly = False  # No anomaly rule applied
        else:  # Pressure
            value = round(random.uniform(950.0, 1050.0), 2)
            is_anomaly = False  # No anomaly rule applied

        timestamp = datetime.utcnow() + timedelta(minutes=random.randint(0, 100))

        data.append({
            "SensorId": sensor_id,
            "GlobalId": global_id,
            "MetricName": metric,
            "Value": value,
            "Timestamp": timestamp.isoformat(),
            "Anomaly": "Yes" if is_anomaly else "No"
        })

    df = pd.DataFrame(data)
    df.to_csv(output_file, index=False)
    print(f"✅ Anomaly dataset generated: {output_file}")

# Run the function (uncomment to execute)
# generate_anomaly_data()
