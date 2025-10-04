import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import threading
import os
import sys
import subprocess
import yaml
import torch

class TerminalCapture:
    """
    Captures stdout and stderr to update a status Label widget
    with the last output line.
    """
    def __init__(self, status_label_widget):
        self.status_label_widget = status_label_widget
        self.last_line = "Terminal ready"
        self.original_stdout = sys.stdout
        self.original_stderr = sys.stderr
        self.capture_stdout()

    def capture_stdout(self):
        sys.stdout = self
        sys.stderr = self

    def write(self, text):
        self.original_stdout.write(text)
        cleaned_text = text.strip()
        if cleaned_text:
            self.last_line = cleaned_text
            # Update the status label with the last line
            self.status_label_widget.config(text=self.last_line)
            self.status_label_widget.update_idletasks()

    def flush(self):
        self.original_stdout.flush()

    def get_last_line(self):
        return self.last_line

class VideoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Video Processing Application")
        # --- CHANGE: Reduced window size for a more compact layout ---
        self.root.geometry("1024x600")
        self.root.minsize(900, 550)
        
        self.setup_theme()
        
        self.device_info = self.get_device_info()
        
        # --- Variables ---
        self.video_path = None
        self.sam2_chkpt_path = None
        self.model_cfg_path = None
        self.processing_thread = None
        
        self.config_data = self.load_config()
        
        self.create_widgets()
        
    def setup_theme(self):
        """Sets up the Forest-dark theme from the .tcl file"""
        try:
            tcl_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'forest-dark.tcl')
            if os.path.exists(tcl_file):
                self.root.tk.call('source', tcl_file)
                style = ttk.Style()
                style.theme_use('forest-dark')
                print("✅ Forest-dark theme loaded successfully")
            else:
                print("⚠️ forest-dark.tcl not found. Using default theme.")
        except Exception as e:
            print(f"❌ Error loading theme: {e}")

    def load_config(self):
        """Loads configuration from config.yaml if it exists"""
        config_path = "config.yaml"
        if os.path.exists(config_path):
            try:
                with open(config_path, 'r') as f:
                    config = yaml.safe_load(f) or {}
                print(f"✅ Configuration loaded from {config_path}")
                return config
            except Exception as e:
                print(f"❌ Error loading configuration: {e}")
                return {}
        else:
            print("ℹ️ config.yaml file not found")
            return {}

    def get_device_info(self):
        """Gets device information (GPU/CPU)"""
        try:
            if torch.cuda.is_available():
                gpu_name = torch.cuda.get_device_name(0)
                gpu_memory = torch.cuda.get_device_properties(0).total_memory / 1024**3 # GB
                return f"GPU: {gpu_name} ({gpu_memory:.1f} GB)"
            else:
                return "CPU: No GPU available"
        except ImportError:
            return "CPU: Torch is not available"

    def create_widgets(self):
        # --- CHANGE: Main layout restructured for compactness ---
        
        # 1. Status line at the very bottom
        status_line_frame = ttk.Frame(self.root)
        status_line_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=(5, 10))

        # 2. Main container for the two-column layout
        main_container = ttk.Frame(self.root)
        main_container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        main_container.rowconfigure(0, weight=1)
        main_container.columnconfigure(0, minsize=220) # Left column for process selection
        main_container.columnconfigure(1, weight=1)    # Right column for everything else

        # 3. Create and place the two main panes
        process_pane = ttk.Labelframe(main_container, text="Process Selection")
        process_pane.grid(row=0, column=0, sticky="nsew", padx=(0, 10))

        controls_pane = ttk.Frame(main_container)
        controls_pane.grid(row=0, column=1, sticky="nsew")

        # 4. Populate the panes
        self.create_process_selection_panel(process_pane)
        self.create_controls_panel(controls_pane)
        
        # 5. Populate the status line
        status_label_title = ttk.Label(status_line_frame, text="LAST MESSAGE:", font=('Arial', 9, 'bold'))
        status_label_title.pack(side=tk.LEFT, padx=(5, 5))
        
        self.status_line_label = ttk.Label(
            status_line_frame, 
            text="Terminal ready",
            font=('Consolas', 10),
            anchor='w',
            wraplength=1000
        )
        self.status_line_label.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
        
        self.terminal_capture = TerminalCapture(self.status_line_label)

    def create_process_selection_panel(self, parent):
        """Creates the left panel with only the process selection radio buttons."""
        options = ["first_step", "second_step", "third_step", "fourth_step", "fifth_step", "sixth_step", "seventh_step", "eighth_step"]
        self.selected_option = tk.StringVar(value=options[0])
        
        for option in options:
            rb = ttk.Radiobutton(parent, text=f"{option.replace('_', ' ').title()}", 
                                 variable=self.selected_option, 
                                 value=option, command=self.on_option_selected)
            rb.pack(anchor='w', pady=5, padx=10)

    def create_controls_panel(self, parent):
        """Creates the right panel with status, configuration, and actions."""
        # --- Grid layout for the right panel ---
        parent.columnconfigure(0, weight=1)
        parent.rowconfigure(1, weight=1) # Allow config frame to expand

        # --- 1. Status and Info Section ---
        status_labelframe = ttk.Labelframe(parent, text="Status & Info")
        status_labelframe.grid(row=0, column=0, sticky="new", pady=(0, 10))
        status_labelframe.columnconfigure(0, weight=1)

        device_label = ttk.Label(status_labelframe, text=self.device_info, font=('Arial', 10, 'bold'))
        device_label.pack(fill=tk.X, padx=10, pady=5)
        print(f"Device information: {self.device_info}")

        self.status_labels = {}
        info_labels = ["Status: Idle", "Selected Process: First Step"]
        for i, text in enumerate(info_labels):
            label = ttk.Label(status_labelframe, text=text, anchor='w')
            label.pack(fill=tk.X, padx=10, pady=2)
            self.status_labels[f"label_{i}"] = label

        # --- 2. Configuration Section ---
        config_labelframe = ttk.Labelframe(parent, text="Configuration")
        config_labelframe.grid(row=1, column=0, sticky="nsew", pady=(0, 10))
        config_labelframe.columnconfigure(1, weight=1)

        # File-based Parameters
        file_params = [
            ("Video:", "video_path", "video_search_var", self.browse_video, "root", ""),
            ("SAM2 Checkpoint:", "sam2_chkpt_path", "sam_search_var", self.browse_sam_checkpoint, "sam2_chkpt", ""),
            ("Model Config:", "model_cfg_path", "model_cfg_var", self.browse_model_cfg, "model_cfg", "configs/sam2.1/sam2.1_hiera_l.yaml")
        ]
        
        for i, (label_text, path_attr, var_attr, cmd, config_key, default) in enumerate(file_params):
            ttk.Label(config_labelframe, text=label_text).grid(row=i, column=0, sticky='w', pady=4, padx=5)
            entry_frame = ttk.Frame(config_labelframe)
            entry_frame.grid(row=i, column=1, sticky='ew', pady=4, padx=5)
            
            var = tk.StringVar()
            setattr(self, var_attr, var)
            path_value = self.config_data.get(config_key, default)
            
            if path_value:
                setattr(self, path_attr, path_value)
                if os.path.exists(path_value):
                    var.set(os.path.basename(path_value))
                else:
                    var.set(path_value)

            entry = ttk.Entry(entry_frame, textvariable=var, state='readonly')
            entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
            browse_btn = ttk.Button(entry_frame, text="...", command=cmd, width=3)
            browse_btn.pack(side=tk.RIGHT, padx=(5, 0))

        # Numeric Parameters
        numeric_params = [
            ("Factor:", "fac_var", "fac", "2"),
            ("Num Images:", "n_imgs_var", "n_imgs", "200"),
            ("Num Objects:", "n_obj_var", "n_obj", "20"),
            ("SAHI Image Size:", "img_size_sahi_var", "img_size_sahi", "512"),
            ("SAHI Overlap:", "overlap_sahi_var", "overlap_sahi", "0.2")
        ]
        
        for i, (label, var_name, key, default) in enumerate(numeric_params, start=len(file_params)):
            ttk.Label(config_labelframe, text=label).grid(row=i, column=0, sticky='w', pady=4, padx=5)
            config_value = self.config_data.get(key, default)
            var = tk.StringVar(value=str(config_value))
            setattr(self, var_name, var)
            entry = ttk.Entry(config_labelframe, textvariable=var, width=15)
            entry.grid(row=i, column=1, sticky='w', pady=4, padx=5)

        # --- 3. Actions Section ---
        actions_frame = ttk.Labelframe(parent, text="Actions")
        actions_frame.grid(row=2, column=0, sticky="sew")
        actions_frame.columnconfigure(0, weight=1)
        actions_frame.columnconfigure(1, weight=1)
        
        self.execute_btn = ttk.Button(actions_frame, text="Execute Process", command=self.execute_process, state=tk.DISABLED)
        self.execute_btn.grid(row=0, column=0, sticky='ew', padx=5, pady=5)
        
        clear_btn = ttk.Button(actions_frame, text="Clear Status Line", command=self.clear_status_line)
        clear_btn.grid(row=0, column=1, sticky='ew', padx=5, pady=5)
        
        if self.video_path:
            self.execute_btn.configure(state=tk.NORMAL)

    def clear_status_line(self):
        """Clears the status line"""
        self.status_line_label.config(text="")
        print("Status line cleared\n")
    
    def browse_video(self):
        file_path = filedialog.askopenfilename(title="Select video", filetypes=[("Video files", "*.mp4 *.avi *.mov"), ("All files", "*.*")])
        if file_path:
            self.video_path = file_path
            self.video_search_var.set(os.path.basename(file_path))
            self.update_status_labels()
            print(f"Video selected: {os.path.basename(file_path)}\n")
            if self.video_path:
                self.execute_btn.configure(state=tk.NORMAL)

    def browse_sam_checkpoint(self):
        file_path = filedialog.askopenfilename(title="Select SAM2 checkpoint", filetypes=[("Checkpoint files", "*.pth *.pt"), ("All files", "*.*")])
        if file_path:
            self.sam2_chkpt_path = file_path
            self.sam_search_var.set(os.path.basename(file_path))
            print(f"SAM2 checkpoint selected: {os.path.basename(file_path)}\n")

    def browse_model_cfg(self):
        file_path = filedialog.askopenfilename(title="Select Model Config", filetypes=[("YAML files", "*.yaml *.yml"), ("All files", "*.*")])
        if file_path:
            self.model_cfg_path = file_path
            self.model_cfg_var.set(os.path.basename(file_path))
            print(f"Model config selected: {os.path.basename(file_path)}\n")
            
    def on_option_selected(self):
        option = self.selected_option.get()
        process_name = option.replace('_', ' ').title()
        self.status_labels["label_1"].configure(text=f"Selected Process: {process_name}")
        if self.video_path:
            self.execute_btn.configure(state=tk.NORMAL)

    def update_status_labels(self):
        status_text = "Idle"
        option_text = f"Selected Process: {self.selected_option.get().replace('_', ' ').title()}"
        self.status_labels["label_0"].configure(text=f"Status: {status_text}")
        self.status_labels["label_1"].configure(text=option_text)
    
    def execute_process(self):
        if not self.video_path:
            messagebox.showwarning("Warning", "Please select a video first.")
            return
        
        if self.processing_thread and self.processing_thread.is_alive():
            messagebox.showwarning("Warning", "A process is already running.")
            return
        
        self.processing_thread = threading.Thread(target=self.run_selected_process, daemon=True)
        self.processing_thread.start()
        
    def run_selected_process(self):
        """Executes the selected process with all parameters"""
        try:
            step = self.selected_option.get()
            print(f"Starting process: {step}\n")
            self.status_labels["label_0"].configure(text="Status: Processing...")
            
            cmd = [
                "uv", "run", "python", "-m", f"segmentedcreator.{step}",
                "--root", self.video_path,
                "--fac", self.fac_var.get(),
                "--n_imgs", self.n_imgs_var.get(),
                "--n_obj", self.n_obj_var.get(),
                "--img_size_sahi", self.img_size_sahi_var.get(),
                "--overlap_sahi", self.overlap_sahi_var.get(),
            ]
            
            if self.sam2_chkpt_path:
                cmd.extend(["--sam2_chkpt", self.sam2_chkpt_path])
            if self.model_cfg_path:
                cmd.extend(["--model_cfg", self.model_cfg_path])
            
            print(f"Executing: {' '.join(cmd)}\n")
            
            process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                universal_newlines=True,
                bufsize=1,
                encoding='utf-8',
                errors='replace'
            )
            
            for line in process.stdout:
                pass 
            
            process.wait()
            
            if process.returncode == 0:
                final_msg = "✅ Process completed successfully!"
                print(f"{final_msg}\n")
                self.status_labels["label_0"].configure(text="Status: Completed")
            else:
                final_msg = f"❌ Process failed with code: {process.returncode}"
                print(f"{final_msg}\n")
                self.status_labels["label_0"].configure(text="Status: Error")
                messagebox.showerror("Error", f"The process failed with code {process.returncode}")
            
            self.status_line_label.config(text=final_msg)

        except FileNotFoundError:
            error_msg = "Error: 'uv' not found. Make sure 'uv' is installed and in your PATH."
            print(error_msg)
            self.status_labels["label_0"].configure(text="Status: Error - uv not found")
            self.status_line_label.config(text=error_msg)
            messagebox.showerror("Error", error_msg)
        except Exception as e:
            error_msg = f"Error executing process: {str(e)}"
            print(error_msg)
            self.status_labels["label_0"].configure(text="Status: Error")
            self.status_line_label.config(text=error_msg)
            messagebox.showerror("Error", error_msg)

    def on_closing(self):
        sys.stdout = self.terminal_capture.original_stdout
        sys.stderr = self.terminal_capture.original_stderr
        self.root.destroy()

def main():
    root = tk.Tk()
    app = VideoApp(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()

if __name__ == "__main__":
    main()