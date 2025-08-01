# Python Sample Scripts for STRIDE

This folder contains the Python scripts to support the validation of the STRIDE framework, as described in our manuscript. The scripts are organized into two main functions:

1.  **Simulated Dataset Generation (for Section 3.4.3):** A set of scripts to generate a sophisticated, multi-file dataset that simulates a realistic anomaly scenario.
2.  **Workflow Demonstration (for Section 4.1.4):** A simplified set of scripts that demonstrates the core data processing and automation workflow as shown in the manuscript's code listings.

---
### Requirements and Installation

To run these scripts, you will need **Python 3.8+** and a running **Neo4j database instance**.

1.  Create a text file named `requirements.txt` and paste the following content into it:
    ```
    # For connecting to the Neo4j database
    neo4j==5.17.0

    # For making HTTP requests to the Power Automate API
    requests==2.31.0

    # For data handling and creating CSV files
    pandas==2.2.0
    uuid
    ```
2.  Install the required Python libraries using this file:
    ```bash
    pip install -r requirements.txt
    ```

---
### Part 1: Simulated Dataset Generation (for Section 3.4.3)

These scripts are used to generate the rich, simulated dataset used for the main validation.

#### **Scripts Overview**

* **`Generate_Anomaly_Data.py`**: Generates a realistic, time-series dataset of sensor readings that simulates a daily temperature cycle with a multi-stage anomaly event. The output is saved to `anomaly_data.csv`.
* **`Generate_MaintenanceTask.py`**: Reads the `anomaly_data.csv` file and creates a corresponding `MaintenanceTask.csv` file, assigning a unique ID and a timestamp for each task.
* **`Generate_TRIGGERS.py`**: Reads both the anomaly and maintenance task CSV files and creates a final `Edge_TRIGGERS.csv` file, which defines the `[:TRIGGERS]` relationships between anomalies and their corresponding tasks.

#### **Usage**
Run the scripts in the following order:
1.  `Generate_Anomaly_Data.py`
2.  `Generate_MaintenanceTask.py`
3.  `Generate_TRIGGERS.py`

---
### Part 2: Workflow Demonstration (for Section 4.1.4)

These scripts are simplified versions corresponding to the code listings in the manuscript, intended to demonstrate the core data processing pipeline.

#### **Scripts Overview**

* **`generate_anomaly_data_process.py`**: A simple script to generate random anomaly data for the workflow demonstration.
* **`log_anomalies_to_neo4j.py`**: Reads the data and logs anomaly records as `:Anomaly` nodes in the Neo4j database.
* **`trigger_workflow.py`**: Reads the data and sends anomaly records to an external workflow platform (e.g., Power Automate) via an API call.

#### **Usage**
Run the scripts in the following order:
1.  `generate_anomaly_data_process.py`
2.  `log_anomalies_to_neo4j.py`
3.  `trigger_workflow.py`

---
### Configuration

Before running the scripts that interact with Neo4j or Power Automate, please ensure you update the configuration details (database URI/user/password and the API URL/token) within each script to match your environment.

