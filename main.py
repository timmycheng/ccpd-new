import tkinter as tk
from tkinter import ttk, filedialog, messagebox

class GUI:

    def __init__(self):

        self.root = tk.Tk()
        self.root.title("CCPD")
        self.root.geometry("1200x800")
        
        # Create main container with two columns
        self.main_frame = ttk.Frame(self.root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Left frame for image selection and display
        self.left_frame = ttk.Frame(self.main_frame, padding="5")
        self.left_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Right frame for results
        self.right_frame = ttk.Frame(self.main_frame, padding="5")
        self.right_frame.grid(row=0, column=1, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Create sections
        self.create_input_section()
        self.create_image_display()
        self.create_button_section()
        self.create_output_section()

    def create_input_section(self):
        # Input file path
        ttk.Label(self.main_frame, text="Input File Path:").grid(row=0, column=0, sticky=tk.W)
        self.input_path = ttk.Entry(self.main_frame, width=50)
        self.input_path.grid(row=0, column=1, padx=5)
        ttk.Button(self.main_frame, text="Browse", command=self.browse_input).grid(row=0, column=2)

    def create_button_section(self):
        # Process button
        self.process_btn = ttk.Button(self.main_frame, text="Start Processing", command=self.process_files)
        self.process_btn.grid(row=1, column=1, pady=20)

    def create_image_display(self):
        # Image display area
        ttk.Label(self.left_frame, text="Selected Image:").grid(row=1, column=0, sticky=tk.W)
        self.image_canvas = tk.Canvas(self.left_frame, width=500, height=500, bg="white")
        self.image_canvas.grid(row=2, column=0, pady=10)
        
    def create_output_section(self):
        # Output log area in right frame
        ttk.Label(self.right_frame, text="Processing Results:").grid(row=0, column=0, sticky=tk.W)
        self.log_text = tk.Text(self.right_frame, height=35, width=70)
        self.log_text.grid(row=1, column=0, pady=10)
        # Add scrollbar
        scrollbar = ttk.Scrollbar(self.right_frame, orient=tk.VERTICAL, command=self.log_text.yview)
        scrollbar.grid(row=1, column=1, sticky=(tk.N, tk.S))
        self.log_text['yscrollcommand'] = scrollbar.set

    def browse_input(self):
        filename = filedialog.askdirectory()
        if filename:
            self.input_path.delete(0, tk.END)
            self.input_path.insert(0, filename)

    def process_files(self):
        input_path = self.input_path.get()
        if not input_path:
            messagebox.showerror("Error", "Please select an input file path!")
            return
        # Add actual processing logic here
        self.log_text.insert(tk.END, f"Processing folder: {input_path}\n")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = GUI()
    app.run()

