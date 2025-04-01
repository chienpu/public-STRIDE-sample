# STRIDE Prototype Implementation

This document provides implementation notes, dataset specifications, and validation instructions for reproducing the STRIDE prototype.

---

## 📌 Overview

The STRIDE prototype demonstrates semantic task-driven reasoning and integration for predictive maintenance using:

- **Neo4j** as the graph-based ontology database
- **Python** for simulation and automation logic
- **Power Automate** for workflow execution

---

## ⚙️ Components

### 1. Dataset Generation

- **Script**: `python-sample/generate_anomaly_data.py`
- **Output**: `data-sample/anomaly_data.csv`

This script generates synthetic IoT sensor data (Temperature, Humidity, Pressure) and injects anomalies for simulation purposes.

**Attributes**:
| Field       | Description                                 |
|-------------|---------------------------------------------|
| SensorId    | Unique identifier for the sensor            |
| GlobalId    | Associated component or system              |
| MetricName  | Type of metric measured                     |
| Value       | Recorded value                              |
| Timestamp   | Time of recording                           |
| Anomaly     | Boolean flag for anomaly presence           |

```bash
python data/generate_anomaly_data.py
```

---

### 2. Integration with Neo4j

- Import `anomaly_data.csv` via the **Neo4j Data Importer**
- Use the provided node/relationship schema in the `schema/` directory
- Validate mappings using ontology structure defined in STRIDE

---

### 3. Automation & Visualization

- Trigger data flow using **Power Automate**
- Use BI tools (e.g., Power BI) to visualize tasks, anomalies, and performance KPIs
- Real-time insights are logged to the graph and exported logs folder

---

## ✅ Validation Strategy

The prototype is validated based on the following indicators:

- **Logging Dataset Accuracy**
- **Data Update Latency**
- **Anomaly Detection Accuracy**
- **Automated Maintenance Task Rate**
- **Query Response Time Efficiency**

See `evaluation/validation_metrics.xlsx` for test results and detailed methods.

---

## 🧪 Minimal Reproducible Examples

Two lightweight examples are included to demonstrate STRIDE’s semantic reasoning logic and Neo4j-based query workflows.

---

### 📌 Example 1: Energy Consumption Anomaly Detection

Detects excessive energy usage (1.5× above average) and automatically generates a `MaintenanceTask` node.

- **Relationships Used**: `[:MONITORS]`, `[:GENERATES]`
- **Cypher Logic**:

```cypher
MATCH (s:Sensor)-[:MONITORS]->(c:Chiller)
WHERE s.type = 'Energy_Consumption' AND s.value > 1.5 * c.avg_energy
RETURN c.Chiller_ID, s.value, c.avg_energy
```

- **Files Required**:
  - `Sensor_Data_300.csv`
  - `Anomaly_Data_300.csv`
  - `Edge_MAPS_SENSOR_DATA.csv`
  - `Edge_GENERATES.csv`
  - `BuildingComponent_Dataset.csv`

---

### 📌 Example 2: Critical Maintenance Workflow (Composite Rule)

Combines high energy and temperature anomalies to trigger a high-priority `MaintenanceTask`.

- **Relationships Used**: `[:MONITORS]`, `[:DETECTED_BY]`, `[:TRIGGERS]`
- **Cypher Logic**:

```cypher
MATCH (s1:Sensor)-[:MONITORS]->(c:BuildingComponent)
WHERE s1.type = 'Energy_Consumption' AND s1.value > 1.5 * c.avg_energy
MATCH (s2:Sensor)-[:MONITORS]->(c)
WHERE s2.type = 'Temperature' AND s2.value > 33
MERGE (a:Anomaly {type: 'Critical'})
MERGE (a)-[:DETECTED_BY]->(s1)
MERGE (a)-[:DETECTED_BY]->(s2)
MERGE (a)-[:ASSOCIATES_WITH]->(c)
MERGE (a)-[:TRIGGERS]->(:MaintenanceTask {priority: 'High'})
RETURN c.ComponentId, a.type
```

- **Files Required**:
  - `Sensor_Data_300.csv`
  - `Performance_Data_with_Anomly_300.csv`
  - `Anomaly_Data_300.csv`
  - `Edge_GENERATES.csv`

---

## 📂 File Structure

```
python-sample/
├── generate_anomaly_data.py   # Script to generate test datasets

data-sample/
├── anomaly_data.csv           # Output dataset

ontology-guided-schema/
├── neo4j_import_schema.json   # Neo4j Data Importer schema

docs/
└── STRIDE_Prototype.md        # This document
```

---

## 📮 Contact

For questions or contributions, open an issue or contact the STRIDE team via GitHub Discussions.
