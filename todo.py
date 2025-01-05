from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QListWidget, QLineEdit, QMessageBox
)
import sys

class ToDoAppPyQt5(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("To-Do List - PyQt5")
        self.setGeometry(300, 100, 400, 400)

        # Task List
        self.tasks = []

        # Layout
        self.layout = QVBoxLayout()

        # Widgets
        self.task_input = QLineEdit(self)
        self.task_input.setPlaceholderText("Enter a new task")

        self.add_button = QPushButton("Add Task", self)
        self.add_button.clicked.connect(self.add_task)

        self.update_button = QPushButton("Update Task", self)
        self.update_button.clicked.connect(self.update_task)

        self.task_list = QListWidget(self)

        self.delete_button = QPushButton("Delete Task", self)
        self.delete_button.clicked.connect(self.delete_task)

        # Add widgets to layout
        self.layout.addWidget(self.task_input)
        self.layout.addWidget(self.add_button)
        self.layout.addWidget(self.update_button)
        self.layout.addWidget(self.task_list)
        self.layout.addWidget(self.delete_button)

        self.setLayout(self.layout)

    def add_task(self):
        task = self.task_input.text().strip()
        if task:
            self.tasks.append(task)
            self.task_list.addItem(task)
            self.task_input.clear()
        else:
            QMessageBox.warning(self, "Warning", "Task cannot be empty!")

    def update_task(self):
        selected_items = self.task_list.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, "Warning", "No task selected to update!")
            return

        new_task = self.task_input.text().strip()
        if not new_task:
            QMessageBox.warning(self, "Warning", "Task input cannot be empty for update!")
            return

        for item in selected_items:
            row = self.task_list.row(item)
            self.tasks[row] = new_task
            self.task_list.item(row).setText(new_task)
        self.task_input.clear()

    def delete_task(self):
        selected_items = self.task_list.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, "Warning", "No task selected!")
            return

        for item in selected_items:
            self.tasks.remove(item.text())
            self.task_list.takeItem(self.task_list.row(item))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ToDoAppPyQt5()
    window.show()
    sys.exit(app.exec_())
