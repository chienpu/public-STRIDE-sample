def log_anomaly_to_neo4j(data, uri="bolt://localhost:7687", user="neo4j", password="password"):
    driver = GraphDatabase.driver(uri, auth=(user, password))
    with driver.session() as session:
        for entry in data:
            try:
                session.run(
                    "CREATE (a:Anomaly {SensorId: $SensorId, GlobalId: $GlobalId, MetricName: $MetricName, "
                    "Value: $Value, Timestamp: $Timestamp, Anomaly: $Anomaly})",
                    SensorId=entry['SensorId'], GlobalId=entry['GlobalId'],
                    MetricName=entry['MetricName'], Value=entry['Value'],
                    Timestamp=entry['Timestamp'], Anomaly=entry['Anomaly']
                )
            except Exception as e:
                print(f"Error logging anomaly: {e}")

log_anomaly_to_neo4j(anomaly_data)
