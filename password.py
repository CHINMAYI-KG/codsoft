import sys
import random
import string
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox

class PasswordGeneratorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Password Generator")
        self.setGeometry(100, 100, 400, 200)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.length_label = QLabel("Enter password length:", self)
        layout.addWidget(self.length_label)

        self.length_input = QLineEdit(self)
        layout.addWidget(self.length_input)

        self.generate_button = QPushButton("Generate Password", self)
        self.generate_button.clicked.connect(self.generate_password)
        layout.addWidget(self.generate_button)

        self.result_label = QLabel("Generated Password: ", self)
        layout.addWidget(self.result_label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def generate_password(self):
        try:
            length = int(self.length_input.text())
            if length <= 0:
                raise ValueError("Length must be positive.")

            characters = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(random.choice(characters) for _ in range(length))
            self.result_label.setText(f"Generated Password: {password}")
        except ValueError:
            QMessageBox.critical(self, "Error", "Please enter a valid positive integer.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PasswordGeneratorApp()
    window.show()
    sys.exit(app.exec_())
