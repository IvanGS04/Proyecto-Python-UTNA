import tkinter as tk
from tkinter import ttk

class TinyGSInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("HipatiaTepezala Console")
        self.root.geometry("400x600")

        # Crear estilo para etiquetas
        estilo_etiqueta = ttk.Style()
        estilo_etiqueta.configure("Estilo.TLabel", font=('Arial', 12), padding=(5, 2))

        # Crear etiquetas para mostrar datos
        self.status_label = ttk.Label(root, text="Status: Offline", style="Estilo.TLabel")
        self.status_label.pack()

        self.version_label = ttk.Label(root, text="Version: 2105260", style="Estilo.TLabel")
        self.version_label.pack()

        self.creation_date_label = ttk.Label(root, text="Creation date: 2 days ago", style="Estilo.TLabel")
        self.creation_date_label.pack()

        self.last_packet_label = ttk.Label(root, text="Last Packet: Never", style="Estilo.TLabel")
        self.last_packet_label.pack()

        self.position_label = ttk.Label(root, text="Position (Lat, Lang): 22.231, -102.176", style="Estilo.TLabel")
        self.position_label.pack()

        self.qth_locator_label = ttk.Label(root, text="QTH Locator: DL82vf", style="Estilo.TLabel")
        self.qth_locator_label.pack()

        self.elevation_label = ttk.Label(root, text="Elevation: 2099.00 m", style="Estilo.TLabel")
        self.elevation_label.pack()

        self.auto_tuning_label = ttk.Label(root, text="Auto tuning: ON", style="Estilo.TLabel")
        self.auto_tuning_label.pack()

        self.test_mode_label = ttk.Label(root, text="Test mode: OFF", style="Estilo.TLabel")
        self.test_mode_label.pack()

        self.confirmed_packets_label = ttk.Label(root, text="Confirmed packets: 0", style="Estilo.TLabel")
        self.confirmed_packets_label.pack()

        self.telemetry_packets_label = ttk.Label(root, text="Telemetry packets: 0", style="Estilo.TLabel")
        self.telemetry_packets_label.pack()

        self.antenna_label = ttk.Label(root, text="Type of antenna: -", style="Estilo.TLabel")
        self.antenna_label.pack()

        self.band_label = ttk.Label(root, text="Band: null - null MHz", style="Estilo.TLabel")
        self.band_label.pack()

        # ... Agrega más etiquetas según sea necesario

        # Botón para actualizar datos
        self.update_button = ttk.Button(root, text="Actualizar", command=self.simular_actualizacion)
        self.update_button.pack(pady=10)
        


    def simular_actualizacion(self):
        # Simulamos actualizar los datos (puedes reemplazar esto con lógica real si es necesario)
        self.status_label.config(text="Status: Online")
        self.version_label.config(text="Version: 2106010")
        self.creation_date_label.config(text="Creation date: 1 week ago")
        self.last_packet_label.config(text="Last Packet: 2 hours ago")
        self.position_label.config(text="Position (Lat, Lang): 22.231, -102.176")
        self.qth_locator_label.config(text="QTH Locator: DL82vf")
        self.elevation_label.config(text="Elevation: 2099.00 m")
        self.auto_tuning_label.config(text="Auto tuning: OFF")
        self.test_mode_label.config(text="Test mode: ON")
        self.confirmed_packets_label.config(text="Confirmed packets: 5")
        self.telemetry_packets_label.config(text="Telemetry packets: 10")
        self.antenna_label.config(text="Type of antenna: Yagi")
        self.band_label.config(text="Band: 435.000 - 438.000 MHz")

        # ... Actualiza más etiquetas según sea necesario

# Crear la ventana principal
root = tk.Tk()

# Crear la interfaz de TinyGS
tinygs_interface = TinyGSInterface(root)

# Iniciar el bucle principal de la interfaz gráfica
root.mainloop()
