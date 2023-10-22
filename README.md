# Python-Calculator

This Python script creates a simple calculator application using the `tkinter` library for the graphical user interface. The calculator allows basic arithmetic operations and provides an entry field for input and a set of buttons for interaction.

## Usage

1. **Prerequisites**: Ensure you have Python installed on your system.

2. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/calculator.git

3. **Run the Calculator**:

  ```bash
  python calculator.py
  ```
  The calculator window will open, and you can perform basic calculations using the provided buttons and the entry field.

4. **Features**:

Numeric Buttons (0-9): Click on these buttons to input numbers into the calculator's entry field.

Arithmetic Operators (+, -, *, /): Click on these buttons to input arithmetic operations into the calculator's entry field.

C (Clear): Click on the "C" button to clear the entry field.

= (Equals): Click on the "=" button to calculate the result of the expression entered in the entry field.

Error Handling: The calculator includes error handling. If you attempt an invalid calculation, it will display "Error" in the entry field.

5. **How it works**

The click_button function handles button clicks. It retrieves the text of the clicked button and performs different actions based on the text.

If the text is "=", it evaluates the expression in the entry field and displays the result.
If the text is "C", it clears the entry field.
For numeric and operator buttons, it appends the corresponding text to the entry field.
The GUI is created using tkinter. It consists of an entry field to display the input and results and a grid of buttons for interaction.

The calculator provides a simple and intuitive way to perform basic calculations.
