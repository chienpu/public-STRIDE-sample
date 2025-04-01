import pandas as pd
import random
from datetime import datetime, timedelta

# ✅ 設定檔案存儲路徑
file_path = r"C:\Users\User\OneDrive\04 Project Work\2025 ODIA Research\06 Python Code Test\4-1-4 Anomaly Detection\anomaly_data.csv"

# ✅ 生成數據
num_records = 300  # 總數據量，讓數據覆蓋 00:00 - 23:55
start_time = datetime(2025, 2, 1, 0, 0)  # 從午夜 00:00 開始

# ✅ 產生 SensorId & GlobalId
sensor_ids = [f"S{i+1}" for i in range(num_records)]
global_ids = [f"G{i+1}" for i in range(num_records)]
timestamps = [start_time + timedelta(minutes=5 * i) for i in range(num_records)]

# ✅ 溫度區間設計
values = []
anomalies = []
anomaly_phase = 0  # 異常階段 (0: 正常, 1: 初始異常, 2: 中度異常, 3: 高度異常, 4: 降溫處理)

for i, ts in enumerate(timestamps):
    hour = ts.hour  # 取得當前小時數

    # ✅ 設定不同時段的正常溫度範圍
    if 0 <= hour < 8 or 22 <= hour < 24:  # 🌙 深夜 & 早晨（25~28°C）
        temp = round(random.uniform(25, 28), 2)

    elif 8 <= hour < 10:  # 🌅 早晨（26~30°C）
        temp = round(random.uniform(26, 30), 2)

    elif 10 <= hour < 12:  # 🌞 上午（27~32°C）
        temp = round(random.uniform(27, 32), 2)

    elif 12 <= hour < 15:  # 🔥 **異常區間（溫度升高）**
        if anomaly_phase == 0:
            temp = round(random.uniform(30, 32.5), 2)
        elif anomaly_phase == 1:
            temp = round(random.uniform(32.5, 35), 2)
        elif anomaly_phase == 2:
            temp = round(random.uniform(35, 37.5), 2)
        else:
            temp = round(random.uniform(37.5, 40), 2)

        # 過渡到下一階段
        if i % 10 == 0 and anomaly_phase < 3:
            anomaly_phase += 1  # 漸進式升溫

    elif 15 <= hour < 17:  # 🔻 **異常回復（溫度逐步下降）**
        if anomaly_phase == 3:
            temp = round(random.uniform(35, 37.5), 2)
        elif anomaly_phase == 2:
            temp = round(random.uniform(32.5, 35), 2)
        elif anomaly_phase == 1:
            temp = round(random.uniform(30, 32.5), 2)
        else:
            temp = round(random.uniform(27, 32), 2)  # 恢復正常溫度

        # 降溫過渡
        if i % 10 == 0 and anomaly_phase > 0:
            anomaly_phase -= 1  # 逐步降溫

    elif 17 <= hour < 19:  # 🌇 下午4:00 - 6:00（27~32°C）
        temp = round(random.uniform(27, 32), 2)

    elif 19 <= hour < 22:  # 🌆 晚上7:00 - 10:00（26~30°C）
        temp = round(random.uniform(26, 30), 2)

    else:
        temp = round(random.uniform(25, 28), 2)  # 🌙 預設深夜冷卻區間

    # ✅ 設定異常標記
    status = "Yes" if temp > 33 else "No"
    values.append(temp)
    anomalies.append(status)

# ✅ 確保異常點為紅色
anomaly_flags = ["Yes" if val > 33 else "No" for val in values]

# ✅ 建立 DataFrame
df_anomaly = pd.DataFrame({
    "SensorId": sensor_ids,
    "GlobalId": global_ids,
    "MetricName": ["Temperature"] * num_records,
    "Value": [f"{val} C" for val in values],  # 加上 "C" 單位
    "Timestamp": [ts.isoformat() for ts in timestamps],
    "Anomaly": anomaly_flags
})

# ✅ 儲存到指定的 OneDrive 資料夾
df_anomaly.to_csv(file_path, index=False)

print(f"✅ 異常數據已成功保存至: {file_path}")
