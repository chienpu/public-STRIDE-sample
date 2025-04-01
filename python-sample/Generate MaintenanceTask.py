import pandas as pd
from datetime import timedelta
import uuid  # Generate unique ment_id

# ✅ Define file paths
anomaly_file = r"C:\Users\User\OneDrive\04 Project Work\2025 ODIA Research\01 Datasets for Building Ontology\4-1-4-2_Neo4jUpdate\Anomaly_Data_300.csv"
maintenance_file = r"C:\Users\User\OneDrive\04 Project Work\2025 ODIA Research\01 Datasets for Building Ontology\4-1-4-2_Neo4jUpdate\MaintenanceTask.csv"

# ✅ Load anomaly data
df = pd.read_csv(anomaly_file)

# ✅ Normalize column names (remove spaces & ensure consistency)
df.columns = df.columns.str.strip()

# ✅ Update to match actual column names
required_cols = ["event_id", "sensor_id", "global_id", "Timestamp"]
available_cols = [col for col in required_cols if col in df.columns]

if len(available_cols) < 4:
    print(f"❌ Missing required columns! Found: {df.columns.tolist()}")
    exit()

# ✅ Convert `Timestamp` to datetime format
df["Timestamp"] = pd.to_datetime(df["Timestamp"])

# ✅ Create MaintenanceTask dataset
df_maintenance = df[["event_id", "sensor_id", "global_id", "Timestamp"]].copy()

# ✅ Generate unique `ment_id`
df_maintenance["ment_id"] = [str(uuid.uuid4()) for _ in range(len(df_maintenance))]

# ✅ Set `ment_time` as `Timestamp + 1 minute`
df_maintenance["ment_time"] = df_maintenance["Timestamp"] + timedelta(minutes=1)

# ✅ Save to CSV
df_maintenance.to_csv(maintenance_file, index=False)

print(f"✅ `MaintenanceTask.csv` has been successfully created at: {maintenance_file}")
