# STRIDE Sample Repository for Journal Review

This repository contains selected artifacts from the **STRIDE (Semantic Trigger Reasoning and Integration for Data-Driven Engineering)** framework. It supports journal peer review by demonstrating the core concepts of ontology-driven predictive maintenance using Neo4j and Python.

> 🔒 This is a **public sample**. Proprietary and full-scale datasets are omitted for privacy and intellectual property considerations.

---

## 🧭 Repository Structure

| Folder/File             | Description                                                        |
|-------------------------|--------------------------------------------------------------------|
| `ontology-guided-schema/` | Sample Neo4j schema (JSON) and RDF-style ontology mapping           |
| `python-sample/`        | Key scripts for anomaly generation, detection, and logging         |
| `sample_dataset/`          | Mock datasets (CSV) used for ontology population and testing       |
| `docs/`                 | Prototype documentation and experiment overview                   |
| `images/`               | Diagrams: architecture layers, BPMN workflows, RDF mapping         |
| `README.md`             | This document                                                      |
| `LICENSE`               | MIT License for academic and non-commercial use                   |


---

## 🧠 Core Concepts Demonstrated

- **Ontology Schema (Neo4j Data Importer)**: Sample schema for mapping assets, sensors, and anomalies.
- **RDF-style Conceptual Alignment**: Visualization of STRIDE’s compatibility with RDF/OWL.
- **Python Reasoning Script**: Automates anomaly detection from mock sensor logs.
- **BPMN Diagram**: Describes collaborative ontology development process.
- **Framework Overview Images**: Visual breakdown of STRIDE components and evolution.

---

## 🛠️ How to Use

This repository includes minimal files required to reproduce Listing 1 and Listing 2 in the STRIDE prototype.

### 1. **Ontology Schema**
- `ontology-guided-schema/neo4j_importer_model.json`  
  Neo4j Data Importer JSON schema defining node and relationship types used in STRIDE.

### 2. **Prototype Overview Document**
- `docs/STRIDE_Prototype.md`  
  Describes the STRIDE architecture and references Listing 1 and 2 with context and Cypher logic.

### 3. **Scripts for Listing 1 & 2**
- `python-sample/Generate Anomaly Data.py`  
  Generates temperature and energy-based anomaly data.
- `python-sample/Generate MaintenanceTask.py`  
  Automatically creates task nodes when anomalies are detected.
- `python-sample/Generate_TRIGGERS.py`  
  Establishes semantic `[:TRIGGERS]` edges between anomalies and tasks.

### 4. **Sample Datasets**
- `sample_dataset/`  
  Required files:
  - `Sensor_Data_300.csv`
  - `Anomaly_Data_300.csv`
  - `Performance_Data_with_Anomly_300.csv`
  - `Edge_MAPS_SENSOR_DATA.csv`
  - `Edge_GENERATES.csv`
  - `BuildingComponent_Dataset.csv`

These support:
- **Listing 1**: Energy Consumption Anomaly Detection
- **Listing 2**: Critical Maintenance Workflow (composite rule)

### 5. **System and Ontology Diagrams**
- `images/` *(optional folder)*  
  Includes system architecture and RDF-aligned ontology visualization used in the manuscript.
   
---

## 📎 Related Publication

This repository supports the manuscript:  
**"STRIDE: A Semantic Framework for Ontology-Guided Integration and Predictive Maintenance Automation"** (submitted to *Advanced Engineering Informatics*).

---

## 📩 Contact

Maintained by [chienpu](https://github.com/chienpu).  
For academic use or collaboration questions, please contact me via [chienpu@gmail.com](mailto:chienpu@gmail.com).

