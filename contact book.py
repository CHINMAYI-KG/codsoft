import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLineEdit, QPushButton, QLabel, QListWidget, QHBoxLayout, QFormLayout

class ContactBookApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Contact Book")
        self.setGeometry(100, 100, 500, 400)
        self.contacts = {}
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.contact_list_widget = QListWidget(self)
        layout.addWidget(self.contact_list_widget)

        form_layout = QFormLayout()

        self.name_input = QLineEdit(self)
        form_layout.addRow("Name:", self.name_input)

        self.phone_input = QLineEdit(self)
        form_layout.addRow("Phone Number:", self.phone_input)

        self.email_input = QLineEdit(self)
        form_layout.addRow("Email:", self.email_input)

        self.address_input = QLineEdit(self)
        form_layout.addRow("Address:", self.address_input)

        layout.addLayout(form_layout)

        self.add_button = QPushButton("Add Contact", self)
        self.add_button.clicked.connect(self.add_contact)
        layout.addWidget(self.add_button)

        self.search_input = QLineEdit(self)
        self.search_input.setPlaceholderText("Search by Name or Phone")
        layout.addWidget(self.search_input)

        self.search_button = QPushButton("Search Contact", self)
        self.search_button.clicked.connect(self.search_contact)
        layout.addWidget(self.search_button)

        self.update_button = QPushButton("Update Contact", self)
        self.update_button.clicked.connect(self.update_contact)
        layout.addWidget(self.update_button)

        self.delete_button = QPushButton("Delete Contact", self)
        self.delete_button.clicked.connect(self.delete_contact)
        layout.addWidget(self.delete_button)

        self.result_label = QLabel(self)
        layout.addWidget(self.result_label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def add_contact(self):
        name = self.name_input.text()
        phone = self.phone_input.text()
        email = self.email_input.text()
        address = self.address_input.text()

        if name and phone:
            self.contacts[name] = {'phone': phone, 'email': email, 'address': address}
            self.update_contact_list()
            self.result_label.setText(f"Contact {name} added successfully!")
        else:
            self.result_label.setText("Name and phone are required!")

    def update_contact_list(self):
        self.contact_list_widget.clear()
        for name, details in self.contacts.items():
            self.contact_list_widget.addItem(f"{name} - {details['phone']}")

    def search_contact(self):
        search_text = self.search_input.text().lower()
        self.contact_list_widget.clear()

        for name, details in self.contacts.items():
            if search_text in name.lower() or search_text in details['phone']:
                self.contact_list_widget.addItem(f"{name} - {details['phone']}")

    def update_contact(self):
        selected_item = self.contact_list_widget.currentItem()
        if selected_item:
            selected_name = selected_item.text().split(' - ')[0]
            if selected_name in self.contacts:
                self.name_input.setText(selected_name)
                self.phone_input.setText(self.contacts[selected_name]['phone'])
                self.email_input.setText(self.contacts[selected_name]['email'])
                self.address_input.setText(self.contacts[selected_name]['address'])
                self.result_label.setText(f"Editing contact: {selected_name}")

    def delete_contact(self):
        selected_item = self.contact_list_widget.currentItem()
        if selected_item:
            selected_name = selected_item.text().split(' - ')[0]
            if selected_name in self.contacts:
                del self.contacts[selected_name]
                self.update_contact_list()
                self.result_label.setText(f"Contact {selected_name} deleted successfully!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ContactBookApp()
    window.show()
    sys.exit(app.exec_())
