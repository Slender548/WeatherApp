from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import datetime
import requests


class WeatherApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.start()

    def start(self):
        self.setWindowTitle('Weather App')
        self.setMinimumSize(800, 900)
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QGridLayout()
        central_widget.setLayout(layout)
        square = QFrame(self)
        square.setFrameShape(QFrame.StyledPanel)
        square.setFrameShadow(QFrame.Raised)
        square.setStyleSheet("background-color: black;border-radius: 20px;")
<<<<<<< HEAD
        self.time_label = QLabel(time.strftime("%H:%M"), self)
        self.time_label.setFont(QFont("Roboto", 26))
        self.time_label.setStyleSheet("color: white;background-color: black;")
        self.time_label.setAlignment(Qt.AlignCenter)
        self.description_label = QLabel(forecast['weather'][0]['main'], self)
        self.description_label.setFont(QFont("Roboto", 26))
        self.description_label.setStyleSheet("color: white;background-color: black;")
        self.description_label.setAlignment(Qt.AlignCenter)
        temperature_label = QLabel(str(forecast['main']['temp'])+"°C", self)
        temperature_label.setFont(QFont("Roboto", 26))
        temperature_label.setStyleSheet("color: white;background-color: black;")
        temperature_label.setAlignment(Qt.AlignCenter)
=======
        labels_layout = QHBoxLayout()
        labels_layout.addWidget(description_label)
        labels_layout.addWidget(time_label)
        labels_layout.addWidget(temperature_label)
        square.setLayout(labels_layout)
        square.setMinimumSize(360, 90)
        square.setMaximumSize(480, 120)
        find_city = QLabel("Find your city!")
        find_city.setFont(QFont("Roboto",40))
        self.input = QLineEdit()
        self.input.setFont(QFont("Roboto",30))
        layout.addWidget(square, 0, 2, 0, 3)
        layout.addWidget(find_city,1,2,1,3)
        layout.addWidget(self.input,2,1,2,5)

<<<<<<< HEAD
    def update_background(self):
        if self.description_label.text() == "Sunny":
            random_set = random.randint(1, 3)
            sunny_set = f"background-image: url(Backgrounds/Sunny_{random_set}.jpg);"
            self.background.setStyleSheet(sunny_set)
        elif self.description_label.text() == "Clear":
            random_set = random.randint(1,3)

    def find_out_weather(self):
        ...

    def find_temp(self):
        ...

    def update_time(self):
        print("started")
        current_time = time.strftime("%H:%M")
        self.time_label.setText(current_time)
=======


if __name__ == "__main__":
    application = QApplication([])
    app = WeatherApp()
    app.show()
    application.exec_()
