# 📡 IoT Telemetry Simulator: Double UI Suite

[![Python Version](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/)
[![MQTT](https://img.shields.io/badge/protocol-MQTT-orange.svg)](https://mqtt.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A robust, multi-threaded Python application designed to bridge the gap between **IoT Hardware** and **Software Development**. This suite allows you to simulate real-time sensor data (Temperature & Humidity) and stream it over MQTT without needing a single physical wire.

---

## 📸 Visuals

| 🖥️ Modern Dark Interface (CustomTkinter) | 🏛️ Classic Lightweight UI (Tkinter) |
| :---: | :---: |
| ![Modern GUI](https://via.placeholder.com/400x300?text=Upload+Modern+Screenshot+Here) | ![Simple GUI](https://via.placeholder.com/400x300?text=Upload+Simple+Screenshot+Here) |
| *Sleek, responsive, and timestamped.* | *Fast, native, and lightweight.* |

---

## ✨ Key Features

* **Dual-UI Experience:** Choose between a high-end `CustomTkinter` dark-mode interface or a standard `Tkinter` lightweight version.
* **Smart Threading:** Data publishing runs on a background daemon thread, ensuring the GUI remains smooth and responsive.
* **Real-Time Telemetry:** Simulates realistic temperature and humidity fluctuations using JSON payloads.
* **Auto-Logging:** Features a built-in terminal window within the app to monitor outgoing data and connection heartbeats.
* **Flexible Config:** Connect to any MQTT broker (Public or Local) by simply typing the address and port.

---

## 🛠️ Tech Stack

- **Core:** Python 3.13
- **Communication:** [Paho-MQTT](https://eclipse.org/paho/)
- **UI Frameworks:** `CustomTkinter` (Modern), `Tkinter` (Legacy)
- **Data Handling:** JSON & Python Threading

---

## 🚀 Quick Start

### 1. Clone the repository
```bash
git clone [https://github.com/taniiishaa/IoT-MQTT-Data-Simulator.git](https://github.com/taniiishaa/IoT-MQTT-Data-Simulator.git)
cd IoT-MQTT-Data-Simulator
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run your preferred version
- For the Modern Experience:
```bash
python Modern_GUI/mqtt_telemetry_simulator.py
```

- For the Classic Experience:
```bash
python Simple_GUI/mqtt_publisher.py
```

## 📂 Project Structure

```text
📁 IoT Telemetry Simulator: Double UI Suite/
│
├── Modern_GUI/             
│    └── mqtt_telemetry_simulator.py  # Advanced Dark Mode UI
├── Simple_GUI/             
│    └── mqtt_publisher.py            # Classic Lightweight UI 
├── 📄 requirements.txt     # Project dependencies
├── 📄 .gitignore           # Keeps your repo clean
├── 📄 README.md            # Project documentation

```
## 🎯 Use Cases

- IoT Dashboard Testing: Feed data into Node-RED, Grafana, or Home Assistant.
- Academic Projects: Perfect for demonstrating MQTT protocol logic.
- App Debugging: Test your MQTT subscriber apps without setting up physical ESP32/Arduino sensors.

## 🤝 Contributing

Feel free to fork this project, report bugs, or submit pull requests. Let's make IoT testing easier for everyone!
