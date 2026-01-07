import paho.mqtt.client as mqtt
import random
import time
import json
import threading
import tkinter as tk
from tkinter import messagebox

# MQTT Client setup
client = None
publishing = False  # Flag to start/stop publishing

def log_message(message):
    """Display log messages in the Tkinter text box."""
    log_text.insert(tk.END, message + "\n")
    log_text.see(tk.END)  # Auto-scroll

def start_publishing():
    """Starts publishing random temperature & humidity data to MQTT broker."""
    global client, publishing

    broker = broker_entry.get()
    port = port_entry.get()
    topic = topic_entry.get()

    if not broker or not port or not topic:
        messagebox.showerror("Error", "Please enter Broker, Port, and Topic")
        return

    try:
        port = int(port)
    except ValueError:
        messagebox.showerror("Error", "Port must be a number!")
        return

    # Initialize MQTT Client
    client = mqtt.Client(client_id="Python_Client", protocol=mqtt.MQTTv311)

    try:
        client.connect(broker, port, 60)
        log_message(f"Connected to MQTT Broker: {broker}:{port}")
    except Exception as e:
        messagebox.showerror("MQTT Connection Error", f"Failed to connect: {e}")
        return

    publishing = True
    thread = threading.Thread(target=publish_data, args=(topic,), daemon=True)
    thread.start()

def stop_publishing():
    """Stops publishing data."""
    global publishing
    publishing = False
    log_message("Publishing stopped.")

def publish_data(topic):
    """Function to publish random temperature and humidity data."""
    global publishing, client

    while publishing:
        temperature = round(random.uniform(20.0, 35.0), 2)
        humidity = round(random.uniform(30.0, 80.0), 2)

        payload = json.dumps({"temp": temperature, "hum": humidity})
        log_message(f"Publishing: {payload}")

        client.publish(topic, payload)
        time.sleep(5)  # Send data every 5 seconds

# --- GUI Setup ---
root = tk.Tk()
root.title("MQTT Publisher")
root.geometry("400x400")

tk.Label(root, text="MQTT Broker:").pack()
broker_entry = tk.Entry(root, width=30)
broker_entry.insert(0, "broker.emqx.io") # Default public broker for testing
broker_entry.pack()

tk.Label(root, text="MQTT Port:").pack()
port_entry = tk.Entry(root, width=10)
port_entry.insert(0, "1883") # Default MQTT port
port_entry.pack()

tk.Label(root, text="MQTT Topic:").pack()
topic_entry = tk.Entry(root, width=30)
topic_entry.insert(0, "test/sensor/data")
topic_entry.pack()

start_button = tk.Button(root, text="Start Publishing", command=start_publishing)
start_button.pack(pady=5)

stop_button = tk.Button(root, text="Stop Publishing", command=stop_publishing)
stop_button.pack(pady=5)

log_text = tk.Text(root, height=10, width=50)
log_text.pack()

root.mainloop()