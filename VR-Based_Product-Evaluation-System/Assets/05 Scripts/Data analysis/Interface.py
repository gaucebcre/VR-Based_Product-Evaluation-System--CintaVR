import tkinter as tk
from tkinter import filedialog
import subprocess
import os

# Function to open the file explorer and select a folder
def select_folder():
    folder = filedialog.askdirectory()  # Opens the file explorer
    if folder:  # If a folder is selected, update the text entry and enable buttons
        entry_path.delete(0, tk.END)  # Clear the text entry
        entry_path.insert(0, folder)  # Insert the selected folder path
        # Enable buttons to run scripts
        btn_script1.config(state=tk.NORMAL)
        btn_script2.config(state=tk.NORMAL)
        btn_script3.config(state=tk.NORMAL)

# Function to run the scripts with the selected folder path
def run_script(script):
    path = entry_path.get()  # Get the folder path from the text entry
    if path:  # If the path is not empty
        # Get the path of the current script (interface.py)
        interface_dir = os.path.dirname(os.path.abspath(__file__))  # Get directory of interface.py
        script_path = os.path.join(interface_dir, script)  # Join the interface.py path with the script name
        
        subprocess.run(["python", script_path, path])  # Run the script with the full path
    else:
        print("Please select a folder.")

# Create the main window
root = tk.Tk()
root.title("Script Runner")

# Set window size
root.geometry("800x300")

# Set a stylish background color
root.config(bg="#f0f0f0")

# Create a frame for the path selection and button
frame_path = tk.Frame(root, bg="#f0f0f0")
frame_path.pack(pady=20)

# Create the text entry where the selected path will appear
entry_path = tk.Entry(frame_path, width=35, font=("Arial", 12), relief="solid", bd=2)
entry_path.pack(side=tk.LEFT, padx=10)

# Create the button to select a folder (on the right side of the entry box)
btn_select = tk.Button(frame_path, text="Select Folder", font=("Arial", 12), relief="raised", bg="#f0f0f0", fg="black", width=15, height=1, command=select_folder)
btn_select.pack(side=tk.LEFT)

# Create a frame for the script buttons
frame_buttons = tk.Frame(root, bg="#f0f0f0")
frame_buttons.pack(pady=20)

# Create the buttons to run the scripts with an initial disabled state
btn_script1 = tk.Button(frame_buttons, text="Position", font=("Arial", 12), relief="raised", bg="#f0f0f0", fg="black", width=20, height=2, command=lambda: run_script("DrawPosition.py"), state=tk.DISABLED)
btn_script1.grid(row=0, column=0, padx=10, pady=5)

btn_script2 = tk.Button(frame_buttons, text="Position heatmap", font=("Arial", 12), relief="raised", bg="#f0f0f0", fg="black", width=20, height=2, command=lambda: run_script("PositionHeatmap.py"), state=tk.DISABLED)
btn_script2.grid(row=1, column=0, padx=10, pady=5)

btn_script3 = tk.Button(frame_buttons, text="Eye-tracking", font=("Arial", 12), relief="raised", bg="#f0f0f0", fg="black", width=20, height=2, command=lambda: run_script("EyeTracking.py"), state=tk.DISABLED)
btn_script3.grid(row=2, column=0, padx=10, pady=5)

# Start the GUI event loop
root.mainloop()
