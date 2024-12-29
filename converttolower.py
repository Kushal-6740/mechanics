import os
import tkinter as tk
from PIL import Image, ImageTk

# Initialize the main application window
root = tk.Tk()
root.geometry("1400x900")
root.resizable(True, True)
root.title("Mechanics Problem Solver")

# Create a frame for the main content
main_frame = tk.Frame(root, bg="black")
main_frame.pack(fill="both", expand=True, padx=20, pady=20)

# Problem statement
full_question = (
    "Replace the three horizontal forces and applied couple with an equivalent force-couple system at O "
    "by specifying the resultant R and couple M0. Next, determine the equation for the line of action of the stand-alone resultant force R."
)
label_question = tk.Label(main_frame, text=full_question, fg="yellow", font=('Comic Sans MS', 14), wraplength=1000, justify="left", bg="black")
label_question.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky='w')

# Create a frame for the images
image_frame = tk.Frame(main_frame, bg="black")
image_frame.grid(row=1, column=0, columnspan=2, pady=20)

# Get image paths dynamically using `os`
current_dir = os.path.dirname(os.path.abspath(__file__))  # Directory of the current script
image1_path = os.path.join(current_dir, "1-0.jpg")
image2_path = os.path.join(current_dir, "1-1.jpg")

# Load images
try:
    image1 = Image.open(image1_path)
    image1 = image1.resize((400, 240), Image.LANCZOS)
    img1 = ImageTk.PhotoImage(image1)

    image2 = Image.open(image2_path)
    image2 = image2.resize((400, 240), Image.LANCZOS)
    img2 = ImageTk.PhotoImage(image2)
except FileNotFoundError as e:
    print(f"Error loading images: {e}")
    exit()

# Display images
label1 = tk.Label(image_frame, image=img1, bg="black")
label1.grid(row=0, column=0, padx=10, pady=10)

label2 = tk.Label(image_frame, image=img2, bg="black")
label2.grid(row=0, column=1, padx=10, pady=10)

# Create a frame for the input fields
input_frame = tk.Frame(main_frame, bg="black")
input_frame.grid(row=2, column=0, columnspan=2, pady=20)

# Input fields and labels
inputs = [
    ("Value of F1 (kN):", 0),
    ("Value of F2 (kN):", 1),
    ("Value of F3 (kN):", 2),
    ("Distance for F2 (m):", 3),
    ("Distance for F3 (m):", 4),
    ("Applied Couple (kN-m):", 5)
]

entries = []
for text, row in inputs:
    label = tk.Label(input_frame, text=text, fg="white", font=('Arial', 18), bg="black")
    label.grid(row=row, column=0, padx=10, pady=10, sticky='e')
    entry = tk.Entry(input_frame, font=('Helvetica', 16))
    entry.grid(row=row, column=1, padx=10, pady=10, sticky='w')
    entries.append(entry)

e1, e2, e3, e4, e5, e6 = entries

# Create a frame for the buttons
button_frame = tk.Frame(main_frame, bg="black")
button_frame.grid(row=3, column=0, columnspan=2, pady=20)

# Function to calculate R and M0
def submit():
    try:
        F1 = float(e1.get())  # First force (kN)
        F2 = float(e2.get())  # Second force (kN)
        F3 = float(e3.get())  # Third force (kN)
        d1 = float(e4.get())  # Distance for F2 (m)
        d2 = float(e5.get())  # Distance for F3 (m)
        couple = float(e6.get())  # Applied couple (kN-m)

        # Resultant force R
        R = F1 + F2 + F3

        # Moment at O (M0)
        M0 = (F2 * d1) + (F3 * d2) - couple

        # Line of action equation: y = mx
        m = M0 / R
        line_eq = f"y = {round(m, 3)}x"

        # Display results
        label_result.config(text=f"Resultant Force, R = {round(R, 3)} kN\nMoment at O, M0 = {round(M0, 3)} kN-m\nLine of Action: {line_eq}")
    except ValueError:
        label_result.config(text="Please enter valid numerical values.")

# Create a button to submit the calculation
button_submit = tk.Button(button_frame, text="Submit", font=('Arial', 18), command=submit)
button_submit.grid(row=0, column=0, padx=10, pady=10)

# Create a button to calculate and display results
button_calculate = tk.Button(button_frame, text="Calculate", font=('Arial', 18), command=submit)
button_calculate.grid(row=0, column=1, padx=10, pady=10)

# Result label
label_result = tk.Label(main_frame, text="", fg="white", font=('Arial', 18), bg="black")
label_result.grid(row=4, column=0, columnspan=2, padx=10, pady=20, sticky='w')

# Configure root
root.configure(bg="black")
root.mainloop()