import pandas as pd

# ✅ Define file paths
anomaly_file = r"C:\Users\User\OneDrive\04 Project Work\2025 ODIA Research\01 Datasets for Building Ontology\4-1-4-2_Neo4jUpdate\Anomaly_Data_300.csv"
maintenance_file = r"C:\Users\User\OneDrive\04 Project Work\2025 ODIA Research\01 Datasets for Building Ontology\4-1-4-2_Neo4jUpdate\MaintenanceTask.csv"
output_file = r"C:\Users\User\OneDrive\04 Project Work\2025 ODIA Research\01 Datasets for Building Ontology\4-1-4-2_Neo4jUpdate\Edge_TRIGGERS.csv"

# ✅ Load anomaly and maintenance datasets
df_anomaly = pd.read_csv(anomaly_file)
df_maintenance = pd.read_csv(maintenance_file)

# ✅ Normalize column names (remove spaces & ensure consistency)
df_anomaly.columns = df_anomaly.columns.str.strip()
df_maintenance.columns = df_maintenance.columns.str.strip()

# ✅ Ensure correct column names exist
required_anomaly_cols = ["event_id", "sensor_id", "global_id", "Timestamp"]
required_maintenance_cols = ["event_id", "sensor_id", "global_id", "ment_id"]

if not set(required_anomaly_cols).issubset(df_anomaly.columns) or not set(required_maintenance_cols).issubset(df_maintenance.columns):
    print(f"❌ Missing required columns in datasets!")
    print(f"🔍 Anomaly Dataset Columns: {df_anomaly.columns.tolist()}")
    print(f"🔍 Maintenance Dataset Columns: {df_maintenance.columns.tolist()}")
    exit()

# ✅ Convert timestamps to datetime format
df_anomaly["Timestamp"] = pd.to_datetime(df_anomaly["Timestamp"])
df_maintenance["ment_time"] = pd.to_datetime(df_maintenance["ment_time"])

# ✅ Merge to create "TRIGGERS" relationships
df_triggers = df_anomaly[["event_id", "sensor_id", "global_id", "Timestamp"]].merge(
    df_maintenance[["event_id", "sensor_id", "global_id", "ment_id"]],
    on=["event_id", "sensor_id", "global_id"],
    how="left"
)

# ✅ Rename columns for clarity in Neo4j
df_triggers.rename(columns={
    "Timestamp": "anomaly_time",
    "ment_id": "triggers_ment_id"
}, inplace=True)

# ✅ Save to CSV
df_triggers.to_csv(output_file, index=False)

print(f"✅ `Edge_TRIGGERS.csv` has been successfully created at: {output_file}")
