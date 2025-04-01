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

This repository includes curated files from the STRIDE prototype to support journal review, reproducibility, and semantic reasoning demonstrations.

1. **Ontology Schema**  
   → `ontology-guided-schema/neo4j_importer_model.json`  
   Neo4j Data Importer JSON schema defining node and relationship types used in STRIDE.

2. **Prototype Overview Document**  
   → `docs/STRIDE_Prototype.md`  
   Provides system architecture, validation strategy, and walkthroughs of semantic logic used in **Listing 1** and **Listing 2**.

3. **Semantic Reasoning Scripts**  
   → `python-sample/Anomaly_Reasoning_Sample.py` *(optional future file)*  
   Demonstrates rule-based reasoning using Neo4j Cypher queries. *(You can add this file if desired.)*

4. **Anomaly Data Generator**  
   → `python-sample/generate_anomaly_data.py`  
   Python script for generating synthetic sensor data and injecting labeled anomalies.

5. **Sample Datasets for Listings**  
   → `sample_dataset/`  
   Includes files required to run:
   - **Listing 1: Energy Consumption Anomaly Detection**
   - **Listing 2: Critical Maintenance Workflow**  
   Files include:
   - `Sensor_Data_300.csv`
   - `Anomaly_Data_300.csv`
   - `Performance_Data_with_Anomly_300.csv`
   - `Edge_MAPS_SENSOR_DATA.csv`
   - `Edge_GENERATES.csv`
   - `BuildingComponent_Dataset.csv`

6. **System and Ontology Diagrams**  
   → `images/` *(optional folder to include)*  
   Includes architecture diagrams and RDF-aligned schema visualizations (referenced in the manuscript).
   
---

## 📎 Related Publication

This repository supports the manuscript:  
**"STRIDE: A Semantic Framework for Ontology-Guided Integration and Predictive Maintenance Automation"** (submitted to *Advanced Engineering Informatics*).

---

## 📩 Contact

Maintained by [chienpu](https://github.com/chienpu).  
For academic use or collaboration questions, please contact me via [chienpu@gmail.com](mailto:chienpu@gmail.com).

