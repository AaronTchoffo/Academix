from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QHBoxLayout
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import (QPixmap, QIcon)

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

        #Logo
        self.setWindowIcon(QIcon("assets/icons/logo.png"))
        self.logo_label = QLabel()
        pixmap = QPixmap("assets/icons/login_logo.png")
        self.logo_label.setPixmap(pixmap)
        self.logo_label.setPixmap(pixmap.scaled(75, 75))
        self.logo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

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

        container_layout.addWidget(self.logo_label)
        container_layout.addWidget(self.username_input)
        container_layout.addLayout(password_layout)
        container_layout.addWidget(self.login_button)
        
        container.setLayout(container_layout)
        main_layout.addWidget(container)
        self.setLayout(main_layout)