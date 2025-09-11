def generate_anomaly_data_process(num_records=200, threshold=33):
    return [{
        "SensorId": f"s{i+1}",
        "GlobalId": f"g{i+1}",
        "MetricName": "Temperature",
        "Value": round(random.uniform(20, 40), 2),
        "Timestamp": datetime.utcnow().isoformat(),
        "Anomaly": "Yes" if round(random.uniform(20, 40), 2) > threshold else "No"
    } for i in range(num_records)]

anomaly_data = generate_anomaly_data()
