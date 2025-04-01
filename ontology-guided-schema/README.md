# Ontology-Guided Schema for STRIDE

This directory contains the ontology-based schema used to configure the Neo4j Data Importer for the STRIDE prototype.

## 📌 Purpose

The schema defines the nodes, properties, and relationships that structure the graph database. It enables ontology-guided automation for predictive maintenance by linking facility components, sensor data, and anomaly triggers to reasoning and task generation workflows.

## 🧩 Included File

- `neo4j_importer_model.json`: Configuration file for the [Neo4j Data Importer](https://neo4j.com/docs/data-importer/current/). Use this file to preload the STRIDE schema into a Neo4j database.

## 🧠 Core Ontology Elements

### Node Labels

| Label                      | Description                               |
|---------------------------|-------------------------------------------|
| `Sensor`                  | IoT devices monitoring components         |
| `Performance Data`        | Time-series sensor readings               |
| `Building Component`      | Components with BIM/COBie mapping         |
| `Anomaly`                 | Abnormal system behaviors                 |
| `Generated Task`          | Automatically generated maintenance tasks |
| `Responsible Party`       | Stakeholder or entity accountable         |
| `IFC Component`           | BIM-based asset with structured metadata  |
| `COBie Data`              | COBie-exported tabular component data     |
| `I*_` prefixed nodes      | Represent KPI indicators for validation   |

### Key Relationships

| Type                 | Role in STRIDE Ontology                                     |
|----------------------|-------------------------------------------------------------|
| `[:MONITORS_LATENCY]`| Tracks update time from sensors                             |
| `[:GENERATES]`       | Links sensors to generated readings                         |
| `[:MAPS_SENSOR_DATA]`| Maps sensor input to the component it monitors              |
| `[:ASSOCIATES_WITH]` | Connects building components with relevant sensors          |
| `[:TRIGGERS]`        | Indicates that an anomaly triggers a task                   |
| `[:ASSIGNS_TO]`      | Assigns generated tasks to responsible parties              |
| `[:EVALUATES]`       | Links system logs to evaluation indicators                  |
| `[:REPRESENTS]`      | Associates IFC or COBie data to actual components           |

## 🛠 How to Use

1. Open [Neo4j Data Importer](https://neo4j.com/docs/data-importer/current/)
2. Upload `neo4j_importer_model.json`
3. Connect to your Neo4j instance
4. Drag and drop data files (e.g., `Sensor_Data_300.csv`) into corresponding nodes

This allows you to reproduce the STRIDE prototype’s knowledge graph structure and test reasoning queries described in the article.

## 📎 License

Provided for academic and non-commercial purposes under the MIT license.

