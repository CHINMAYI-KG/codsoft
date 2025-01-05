from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QHBoxLayout

class CalculatorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simple Calculator (PyQt5)")
        self.setGeometry(100, 100, 400, 300)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        
        self.result_label = QLabel("Result: ", self)
        layout.addWidget(self.result_label)
        
        self.num1_input = QLineEdit(self)
        self.num1_input.setPlaceholderText("Enter first number")
        layout.addWidget(self.num1_input)

        self.num2_input = QLineEdit(self)
        self.num2_input.setPlaceholderText("Enter second number")
        layout.addWidget(self.num2_input)
        
        # Buttons for operations
        button_layout = QHBoxLayout()
        self.add_button = QPushButton("+", self)
        self.add_button.clicked.connect(lambda: self.calculate("+"))
        button_layout.addWidget(self.add_button)

        self.sub_button = QPushButton("-", self)
        self.sub_button.clicked.connect(lambda: self.calculate("-"))
        button_layout.addWidget(self.sub_button)

        self.mul_button = QPushButton("*", self)
        self.mul_button.clicked.connect(lambda: self.calculate("*"))
        button_layout.addWidget(self.mul_button)

        self.div_button = QPushButton("/", self)
        self.div_button.clicked.connect(lambda: self.calculate("/"))
        button_layout.addWidget(self.div_button)
        
        layout.addLayout(button_layout)
        
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def calculate(self, operation):
        try:
            num1 = float(self.num1_input.text())
            num2 = float(self.num2_input.text())
            
            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2
            elif operation == "*":
                result = num1 * num2
            elif operation == "/":
                if num2 == 0:
                    self.result_label.setText("Error: Division by zero")
                    return
                result = num1 / num2
            else:
                self.result_label.setText("Invalid operation")
                return
            
            self.result_label.setText(f"Result: {result}")
        except ValueError:
            self.result_label.setText("Error: Invalid input")

# Run the PyQt5 application
if __name__ == "__main__":
    app = QApplication([])
    window = CalculatorApp()
    window.show()
    app.exec_()
