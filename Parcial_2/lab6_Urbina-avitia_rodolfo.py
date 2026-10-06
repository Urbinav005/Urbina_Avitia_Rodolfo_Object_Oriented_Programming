"""
Lab 6.1 - Smart Home Upgrade
Polymorphism + Tkinter GUI

1. Second polymorphic behavior: turn_off()
2. New device class to test scalability (SmartSpeaker)
3. GUI upgrade: Turn Off button + Activity Log (Listbox with scrollbar)
4. Logo (logo.png in the same folder as this file)

IMPORTANT: do NOT name this file tkinter.py (it would shadow the standard library).
"""

import os
import tkinter as tk
from tkinter import ttk
from abc import ABC, abstractmethod
from datetime import datetime


# =====================================================================
# BASE CLASS (abstract)
# =====================================================================
class BaseItem(ABC):
    """Every smart device must implement both behaviors."""

    def __init__(self, name: str):
        self.name = name
        self.is_on = False

    @abstractmethod
    def turn_on(self) -> str:
        ...

    @abstractmethod
    def turn_off(self) -> str:
        ...


# =====================================================================
# CONCRETE DEVICES
# =====================================================================
class Light(BaseItem):
    def __init__(self):
        super().__init__("Living Room Light")

    def turn_on(self) -> str:
        self.is_on = True
        return f"{self.name}: The light is now ON and glowing warmly."

    def turn_off(self) -> str:
        self.is_on = False
        return f"{self.name}: The light is now OFF."


class Thermostat(BaseItem):
    def __init__(self):
        super().__init__("Thermostat")

    def turn_on(self) -> str:
        self.is_on = True
        return f"{self.name}: Heating started. Target temperature 22 °C."

    def turn_off(self) -> str:
        self.is_on = False
        return f"{self.name}: Heating stopped. Climate control is idle."


class SecurityCamera(BaseItem):
    def __init__(self):
        super().__init__("Security Camera")

    def turn_on(self) -> str:
        self.is_on = True
        return f"{self.name}: Recording started."

    def turn_off(self) -> str:
        self.is_on = False
        return f"{self.name}: Recording stopped."


# --- NEW DEVICE (scalability test): only a new class + one registry line ---
class SmartSpeaker(BaseItem):
    def __init__(self):
        super().__init__("Smart Speaker")

    def turn_on(self) -> str:
        self.is_on = True
        return f"{self.name}: Music is playing at volume 40%."

    def turn_off(self) -> str:
        self.is_on = False
        return f"{self.name}: Music paused. Speaker in standby."


# =====================================================================
# GUI
# =====================================================================
class SmartHomeApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # --- 1. WINDOW SETTINGS ---
        self.title("OOP Lab 6.1: Smart Home Upgrade")
        self.geometry("520x720")
        self.resizable(False, False)

        # --- 2. OBJECT REGISTRY ---
        self.items = {
            "Light": Light(),
            "Thermostat": Thermostat(),
            "Security Camera": SecurityCamera(),
            "Smart Speaker": SmartSpeaker(),   # <- the new device
        }

        self._build_interface()

    def _build_interface(self):
        # --- LOGO ---
        logo_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logo.png")
        try:
            self.logo_img = tk.PhotoImage(file=logo_path)   # keep a reference!
            self.logo_img = self.logo_img.subsample(3, 3)   # shrink to 1/3; adjust or remove
            tk.Label(self, image=self.logo_img).pack(pady=(10, 0))
            self.iconphoto(False, self.logo_img)            # also use as window icon
        except tk.TclError:
            pass  # no logo.png found: the app still opens without a logo

        # Header
        tk.Label(
            self,
            text="SMART HOME CONTROL",
            font=("Arial", 15, "bold"),
            fg="#2c3e50",
        ).pack(pady=12)

        # Radiobuttons
        group_box = tk.LabelFrame(
            self,
            text=" Select a Device ",
            font=("Arial", 10, "bold"),
            padx=15,
            pady=10,
        )
        group_box.pack(fill="x", padx=20, pady=5)

        first_key = list(self.items.keys())[0]
        self.selected_key = tk.StringVar(value=first_key)

        for key in self.items.keys():
            ttk.Radiobutton(
                group_box,
                text=key,
                value=key,
                variable=self.selected_key,
            ).pack(anchor="w", pady=3)

        # Buttons row (Turn On + Turn Off)
        btn_frame = tk.Frame(self)
        btn_frame.pack(pady=12)

        tk.Button(
            btn_frame,
            text="TURN ON",
            command=self._handle_turn_on,
            bg="#27ae60",
            fg="white",
            font=("Arial", 10, "bold"),
            relief="raised",
            cursor="hand2",
            padx=12,
            pady=6,
        ).pack(side="left", padx=8)

        tk.Button(
            btn_frame,
            text="TURN OFF",
            command=self._handle_turn_off,
            bg="#c0392b",
            fg="white",
            font=("Arial", 10, "bold"),
            relief="raised",
            cursor="hand2",
            padx=12,
            pady=6,
        ).pack(side="left", padx=8)

        # Output label
        self.lbl_output = tk.Label(
            self,
            text="Select a device and press TURN ON or TURN OFF.",
            font=("Arial", 10, "italic"),
            bg="#ecf0f1",
            fg="#34495e",
            relief="groove",
            height=3,
            wraplength=460,
            justify="center",
        )
        self.lbl_output.pack(fill="x", padx=20, pady=5)

        # Activity Log (Listbox + Scrollbar)
        log_frame = tk.LabelFrame(
            self,
            text=" Activity Log ",
            font=("Arial", 10, "bold"),
            padx=8,
            pady=8,
        )
        log_frame.pack(fill="both", expand=True, padx=20, pady=10)

        scrollbar = tk.Scrollbar(log_frame, orient="vertical")
        self.log_list = tk.Listbox(
            log_frame,
            height=8,
            yscrollcommand=scrollbar.set,
            font=("Courier", 9),
            activestyle="none",
        )
        scrollbar.config(command=self.log_list.yview)

        scrollbar.pack(side="right", fill="y")
        self.log_list.pack(side="left", fill="both", expand=True)

    # ---------------- Handlers ----------------
    def _handle_turn_on(self):
        device: BaseItem = self.items[self.selected_key.get()]
        # POLYMORPHIC CALL: no if/elif needed
        self._show_result(device.turn_on())

    def _handle_turn_off(self):
        device: BaseItem = self.items[self.selected_key.get()]
        # POLYMORPHIC CALL: no if/elif needed
        self._show_result(device.turn_off())

    def _show_result(self, message: str):
        self.lbl_output.config(text=message, font=("Arial", 10, "normal"))
        self._log(message)

    def _log(self, message: str):
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.log_list.insert(tk.END, f"[{timestamp}] {message}")
        self.log_list.see(tk.END)  # auto-scroll to the newest entry


# =====================================================================
# LAUNCHER
# =====================================================================
if __name__ == "__main__":
    app = SmartHomeApp()
    app.mainloop()
