import random
import pandas as pd
from datetime import datetime

def generate_anomaly_data(num_records=200, threshold=33):
    """Generates a list of simulated sensor data with anomalies."""
    data = []
    for i in range(num_records):
        # Generate a value once to ensure consistency
        value = round(random.uniform(20, 40), 2)
        anomaly_status = "Yes" if value > threshold else "No"
        
        data.append({
            "SensorId": f"s{i+1}",
            "GlobalId": f"g{i+1}",
            "MetricName": "Temperature",
            "Value": value,
            "Timestamp": datetime.utcnow().isoformat(),
            "Anomaly": anomaly_status
        })
    return data

# --- Main execution ---
if __name__ == "__main__":
    print("Generating anomaly data...")
    anomaly_data = generate_anomaly_data()
    
    # Convert to a pandas DataFrame and save as a CSV file
    df = pd.DataFrame(anomaly_data)
    df.to_csv("anomaly_data.csv", index=False)
    
    print(f"Successfully generated and saved {len(anomaly_data)} records to anomaly_data.csv")
