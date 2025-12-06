import sys
from abc import ABC, abstractmethod
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QDialog
from PyQt6.QtCore import Qt, QSize

class BaseClicker(ABC):
    @abstractmethod
    def click(self):
        pass

    @abstractmethod
    def get_count(self):
        pass

    @abstractmethod
    def reset(self):
        pass

class ReverseClicker(BaseClicker):
    def __init__(self, start=100):
        self.start_value = start
        self._value = start

    def click(self):
        if self._value > 0:
            self._value -= 1

    def get_count(self):
        return self._value

    def reset(self):
        self._value = self.start_value

class HeartDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Судьба")
        self.setFixedSize(400, 400)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setLayout(layout)

        label = QLabel("Ботай вечно, бро!")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("font-size: 24px; font-weight: bold;")
        layout.addWidget(label)

        heart = QLabel("♥")
        heart.setAlignment(Qt.AlignmentFlag.AlignCenter)
        heart.setStyleSheet("font-size: 200px; color: red;")
        layout.addWidget(heart)

        close_btn = QPushButton("OK")
        close_btn.clicked.connect(self.accept)
        close_btn.setStyleSheet("""
            QPushButton {
                background-color: #3cb043;
                color: white;
                padding: 10px;
                border-radius: 8px;
                font-size: 18px;
                min-width: 100px;
            }
            QPushButton:hover {
                background-color: #2e8b34;
            }
        """)
        layout.addWidget(close_btn, alignment=Qt.AlignmentFlag.AlignCenter)

class ClickerWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Чилл-кликер")
        self.clicker = ReverseClicker(start=100)
        central = QWidget()
        self.setCentralWidget(central)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        central.setLayout(layout)
        self.label = QLabel("Кликов до чилла осталось: 100")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label)

        self.button = QPushButton("Кликай, брат")
        self.button.clicked.connect(self.on_click)
        self.button.setStyleSheet("""
            QPushButton {
                background-color: #3cb043;
                color: white;
                padding: 10px;
                border-radius: 8px;
                font-size: 18px;
            }
            QPushButton:hover {
                background-color: #2e8b34;
            }
        """)
        layout.addWidget(self.button)

    def on_click(self):
        self.clicker.click()
        value = self.clicker.get_count()
        if value > 0:
            self.label.setText(f"Кликов до чилла осталось: {value}")
        else:
            dialog = HeartDialog(self)
            dialog.exec()
            self.clicker.reset()
            self.label.setText(
                f"Кликов до чилла осталось: {self.clicker.get_count()}"
            )

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ClickerWindow()
    window.show()
    app.exec()
