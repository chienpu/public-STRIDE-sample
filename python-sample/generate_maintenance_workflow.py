def generate_maintenance_workflow(anomaly_data, api_url, token):
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    try:
        response = requests.post(api_url, headers=headers, json={"anomaly_data": anomaly_data})
        print("Triggered:", response.status_code)
    except Exception as e:
        print("Error:", e)

# Example call
trigger_task(anomaly_data, "https://api.flow.microsoft.com/...your-flow-url...", "YOUR_TOKEN")
