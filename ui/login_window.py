from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLineEdit, QPushButton, QHBoxLayout
)
from PyQt6.QtCore import Qt

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Academix Login Screen")
        self.resize(600, 500)

        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        container = QWidget()
        container_layout = QVBoxLayout()
        container_layout.setSpacing(15)

        #username
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Username")

        #Password
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        password_layout = QHBoxLayout()
        password_layout.addWidget(self.password_input)

        #Login button
        self.login_button = QPushButton("Login")

        container_layout.addWidget(self.username_input)
        container_layout.addLayout(password_layout)
        container_layout.addWidget(self.login_button)
        
        container.setLayout(container_layout)
        main_layout.addWidget(container)
        self.setLayout(main_layout)