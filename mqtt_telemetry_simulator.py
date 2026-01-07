import customtkinter as ctk
import paho.mqtt.client as mqtt
import random
import time
import json
import threading
from tkinter import messagebox

# Set the appearance mode and color theme
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class MQTTApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("IoT Telemetry Simulator")
        self.geometry("500x600")
        
        self.client = None
        self.publishing = False

        # --- UI LAYOUT ---
        self.grid_columnconfigure(0, weight=1)

        # Header
        self.label = ctk.CTkLabel(self, text="MQTT Data Publisher", font=ctk.CTkFont(size=20, weight="bold"))
        self.label.pack(pady=20)

        # Input Frame
        self.input_frame = ctk.CTkFrame(self)
        self.input_frame.pack(padx=20, pady=10, fill="x")

        self.broker_entry = ctk.CTkEntry(self.input_frame, placeholder_text="Broker (e.g., broker.emqx.io)")
        self.broker_entry.insert(0, "broker.emqx.io")
        self.broker_entry.pack(padx=10, pady=5, fill="x")

        self.port_entry = ctk.CTkEntry(self.input_frame, placeholder_text="Port (e.g., 1883)")
        self.port_entry.insert(0, "1883")
        self.port_entry.pack(padx=10, pady=5, fill="x")

        self.topic_entry = ctk.CTkEntry(self.input_frame, placeholder_text="Topic")
        self.topic_entry.insert(0, "test/sensor/data")
        self.topic_entry.pack(padx=10, pady=5, fill="x")

        # Buttons
        self.start_button = ctk.CTkButton(self, text="Start Publishing", command=self.start_publishing, fg_color="green", hover_color="#228B22")
        self.start_button.pack(pady=10)

        self.stop_button = ctk.CTkButton(self, text="Stop Publishing", command=self.stop_publishing, fg_color="red", hover_color="#B22222")
        self.stop_button.pack(pady=5)

        # Log Box
        self.log_text = ctk.CTkTextbox(self, height=200)
        self.log_text.pack(padx=20, pady=20, fill="both", expand=True)

    def log_message(self, message):
        self.log_text.insert("end", f"[{time.strftime('%H:%M:%S')}] {message}\n")
        self.log_text.see("end")

    def start_publishing(self):
        if self.publishing:
            return

        broker = self.broker_entry.get()
        port = self.port_entry.get()
        topic = self.topic_entry.get()

        if not all([broker, port, topic]):
            messagebox.showerror("Error", "All fields are required!")
            return

        try:
            port = int(port)
            self.client = mqtt.Client(client_id=f"PyClient_{random.randint(0,100)}", protocol=mqtt.MQTTv311)
            self.client.connect(broker, port, 60)
            
            self.publishing = True
            self.log_message(f"Connected to {broker}")
            
            # Start background thread
            thread = threading.Thread(target=self.publish_loop, args=(topic,), daemon=True)
            thread.start()
            
            self.start_button.configure(state="disabled")
        except Exception as e:
            messagebox.showerror("Connection Error", str(e))

    def stop_publishing(self):
        self.publishing = False
        self.start_button.configure(state="normal")
        self.log_message("Publishing stopped.")

    def publish_loop(self, topic):
        while self.publishing:
            temp = round(random.uniform(20.0, 35.0), 2)
            hum = round(random.uniform(30.0, 80.0), 2)
            payload = json.dumps({"temp": temp, "hum": hum, "unit": "metric"})
            
            try:
                self.client.publish(topic, payload)
                self.log_message(f"Sent: {payload}")
            except Exception as e:
                self.log_message(f"Error: {e}")
                break
            
            time.sleep(5)

if __name__ == "__main__":
    app = MQTTApp()
    app.mainloop()