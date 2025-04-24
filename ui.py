import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime, timedelta
from sleepLog import createDb, logSleep, getLastSleep

class SleepApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Yawn Keeper")
        self.root.geometry("500x400")
        
        createDb()
        
        self.user_name = tk.StringVar()
        self.ideal_sleep = tk.DoubleVar(value=8.0)
        self.wake_up_time = tk.StringVar(value="07:00")
        self.last_sleep = tk.DoubleVar()
        self.sleep_debt = tk.DoubleVar()
        self.suggested_bedtime = tk.StringVar()
        
        self.create_widgets()
    
    def create_widgets(self):
        
        notebook = ttk.Notebook(self.root)
        notebook.pack(fill='both', expand=True)
        
        setup_frame = ttk.Frame(notebook)
        notebook.add(setup_frame, text="Main")
        
        ttk.Label(setup_frame, text="Yawn Keeper", font=('Arial', 18)).pack(pady=10)
        
        ttk.Label(setup_frame, text="Your Name:").pack(pady=5)
        ttk.Entry(setup_frame, textvariable=self.user_name).pack(pady=5)
        
        ttk.Label(setup_frame, text="Ideal Sleep Hours:").pack(pady=5)
        ttk.Spinbox(setup_frame, from_=4, to=12, increment=0.5, textvariable=self.ideal_sleep).pack(pady=5)
        
        ttk.Label(setup_frame, text="Wake-up Time (HH:MM):").pack(pady=5)
        ttk.Entry(setup_frame, textvariable=self.wake_up_time).pack(pady=5)
        
        ttk.Button(setup_frame, text="Save", command=self.save_setup).pack(pady=20)
        
        dashboard_frame = ttk.Frame(notebook)
        notebook.add(dashboard_frame, text="Dashboard")
        
        self.dashboard_title = ttk.Label(dashboard_frame, text="Sleep Dashboard", font=('Arial', 14))
        self.dashboard_title.pack(pady=10)
        
        ttk.Label(dashboard_frame, text="Last Night's Sleep (in hours):").pack(pady=5)
        ttk.Entry(dashboard_frame, textvariable=self.last_sleep).pack(pady=5)
        
        ttk.Button(dashboard_frame, text="Log Sleep", command=self.log_sleep).pack(pady=10)
        
        results_frame = ttk.LabelFrame(dashboard_frame, text="Your Sleep Stats")
        results_frame.pack(pady=20, padx=20, fill='both', expand=True)
        
        ttk.Label(results_frame, text="Sleep Duration:").grid(row=0, column=0, sticky='w', padx=5, pady=5)
        self.sleep_duration_label = ttk.Label(results_frame, text="")
        self.sleep_duration_label.grid(row=0, column=1, sticky='w', padx=5, pady=5)
        
        ttk.Label(results_frame, text="Sleep Debt:").grid(row=1, column=0, sticky='w', padx=5, pady=5)
        self.sleep_debt_label = ttk.Label(results_frame, text="")
        self.sleep_debt_label.grid(row=1, column=1, sticky='w', padx=5, pady=5)
        
        ttk.Label(results_frame, text="Suggested Bedtime:").grid(row=2, column=0, sticky='w', padx=5, pady=5)
        self.bedtime_label = ttk.Label(results_frame, text="")
        self.bedtime_label.grid(row=2, column=1, sticky='w', padx=5, pady=5)
    
    def save_setup(self):
        if not self.user_name.get():
            messagebox.showerror("Error", "Please enter your name")
            return
        
        try:
            datetime.strptime(self.wake_up_time.get(), "%H:%M")
        except ValueError:
            messagebox.showerror("Error", "Please enter wake-up time in HH:MM format")
            return
        
        messagebox.showinfo("Success", "Info saved successfully!")
    
    def log_sleep(self):
        try:
            sleep_duration = float(self.last_sleep.get())
            if sleep_duration <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid positive number for sleep duration")
            return
        
        logSleep(self.user_name.get(), sleep_duration)
        
        ideal_sleep = float(self.ideal_sleep.get())
        sleep_debt = getLastSleep(self.user_name.get()) - ideal_sleep
        suggested_bedtime = self.calculate_bedtime(self.wake_up_time.get(), ideal_sleep)
        
        self.sleep_duration_label.config(text=f"{sleep_duration} hours")
        self.sleep_debt_label.config(text=f"{sleep_debt:+.1f} hours")
        self.bedtime_label.config(text=suggested_bedtime)
        
        messagebox.showinfo("Success", "Sleep logged successfully!")
    
    def calculate_bedtime(self, wake_up_time, hours_needed):
        try:
            wake_hour, wake_min = map(int, wake_up_time.split(":"))
            wake_time = datetime.combine(datetime.today(), datetime.min.time()) + timedelta(hours=wake_hour, minutes=wake_min)
            bed_time = wake_time - timedelta(hours=hours_needed)
            return bed_time.strftime("%H:%M")
        except:
            return "Invalid time"

if __name__ == "__main__":
    root = tk.Tk()
    app = SleepApp(root)
    root.mainloop()