# Sample Dataset for STRIDE Prototype

This folder contains a simplified example dataset used to demonstrate the STRIDE framework's ontology-based data integration and reasoning capabilities.

## Minimal Reproducible Examples

This repository includes two minimal examples to help reviewers understand the semantic reasoning and automation capabilities of STRIDE:

### 1. Energy Consumption Anomaly Detection

Detects energy usage exceeding 1.5× the average and automatically generates a `MaintenanceTask`.

- **Key Relationships**: `[:MONITORS]`, `[:GENERATES]`
- **Cypher Query**: See [Listing 1](docs/STRIDE_Prototype.md#listing-1)
- **Dataset Files**:
  - `Sensor_Data_300.csv`
  - `Anomaly_Data_300.csv`
  - `Edge_MAPS_SENSOR_DATA.csv`
  - `Edge_GENERATES.csv`
  - `BuildingComponent_Dataset.csv`

### 2. Critical Maintenance Workflow (Composite Rule)

Combines abnormal energy and temperature readings to trigger a high-priority task.

- **Key Relationships**: `[:MONITORS]`, `[:DETECTED_BY]`, `[:TRIGGERS]`
- **Cypher Query**: See [Listing 2](docs/STRIDE_Prototype.md#listing-2)
- **Dataset Files**:
  - `Sensor_Data_300.csv`
  - `Performance_Data_with_Anomly_300.csv`
  - `Anomaly_Data_300.csv`
  - `Edge_GENERATES.csv`

## License

This dataset is provided for academic and review purposes only.
MIT License 

