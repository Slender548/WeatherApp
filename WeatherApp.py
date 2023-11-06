import time
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import pendulum
import requests
import json
import random
import datetime

url = "http://ipinfo.io/json"
response = requests.get(url)
data = json.loads(response.text)
city = data['city']
API_key = "30a9a578777cde3029df04308eab6eec"
data = requests.get(f"http://api.openweathermap.org/data/2.5/weather?appid={API_key}&q={city}&units=metric")
forecast = data.json()
print(forecast['main']['temp'])
print(forecast['weather'][0]['main'])
print(pendulum.now())
print(datetime.date.today().month)

class WeatherApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.start()
        self.update_background()
        self.time_timer = QTimer(self)
        self.time_timer.timeout.connect(self.update_time)
        self.time_timer.start(10000)

    def start(self):
        self.background = QFrame(self)
        self.background.setFixedSize(1100, 900)
        self.setWindowTitle('Weather App')
        self.setWindowIcon(QIcon('icon.png'))
        self.setFixedSize(1100, 900)
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QGridLayout()
        central_widget.setLayout(layout)
        square = QFrame(self)
        square.setFrameShape(QFrame.StyledPanel)
        square.setFrameShadow(QFrame.Raised)
        square.setStyleSheet("background-color: black;border-radius: 20px;")
        self.time_label = QLabel(time.strftime("%H:%M"), self)
        self.time_label.setFont(QFont("Roboto", 26))
        self.time_label.setStyleSheet("color: white;background-color: black;")
        self.description_label = QLabel(forecast['weather'][0]['main'], self)
        self.description_label.setFont(QFont("Roboto", 26))
        self.description_label.setStyleSheet("color: white;background-color: black;")
        temperature_label = QLabel(str(forecast['main']['temp'])+"°C", self)
        temperature_label.setFont(QFont("Roboto", 26))
        temperature_label.setStyleSheet("color: white;background-color: black;")
        labels_layout = QHBoxLayout()
        labels_layout.addWidget(self.description_label)
        labels_layout.addWidget(self.time_label)
        labels_layout.addWidget(temperature_label)
        square.setLayout(labels_layout)
        square.setFixedSize(450, 120)
        find_city = QLabel("Find your city!")
        find_city.setAlignment(Qt.AlignCenter)
        find_city.setFont(QFont("Roboto", 40))
        self.input = QLineEdit()
        self.input.setFont(QFont("Roboto", 30))
        self.forecast_1 = QFrame(self)
        self.forecast_1.setFrameShape(QFrame.StyledPanel)
        self.forecast_1.setFrameShadow(QFrame.Raised)
        self.forecast_1.setStyleSheet("background-color: black;border-radius: 20px;")
        self.forecast_1.setFixedSize(150, 200)
        self.forecast_2 = QFrame(self)
        self.forecast_2.setFrameShape(QFrame.StyledPanel)
        self.forecast_2.setFrameShadow(QFrame.Raised)
        self.forecast_2.setStyleSheet("background-color: black;border-radius: 20px;")
        self.forecast_2.setFixedSize(150, 200)
        self.forecast_3 = QFrame(self)
        self.forecast_3.setFrameShape(QFrame.StyledPanel)
        self.forecast_3.setFrameShadow(QFrame.Raised)
        self.forecast_3.setStyleSheet("background-color: black;border-radius: 20px;")
        self.forecast_3.setFixedSize(150, 200)
        self.forecast_4 = QFrame(self)
        self.forecast_4.setFrameShape(QFrame.StyledPanel)
        self.forecast_4.setFrameShadow(QFrame.Raised)
        self.forecast_4.setStyleSheet("background-color: black;border-radius: 20px;")
        self.forecast_4.setFixedSize(150, 200)
        self.forecast_5 = QFrame(self)
        self.forecast_5.setFrameShape(QFrame.StyledPanel)
        self.forecast_5.setFrameShadow(QFrame.Raised)
        self.forecast_5.setStyleSheet("background-color: black;border-radius: 20px;")
        self.forecast_5.setFixedSize(150, 200)
        self.forecast_6 = QFrame(self)
        self.forecast_6.setFrameShape(QFrame.StyledPanel)
        self.forecast_6.setFrameShadow(QFrame.Raised)
        self.forecast_6.setStyleSheet("background-color: black;border-radius: 20px;")
        self.forecast_6.setFixedSize(150, 200)
        self.forecast_7 = QFrame(self)
        self.forecast_7.setFrameShape(QFrame.StyledPanel)
        self.forecast_7.setFrameShadow(QFrame.Raised)
        self.forecast_7.setStyleSheet("background-color: black;border-radius: 20px;")
        self.forecast_7.setFixedSize(150, 200)
        layout.addWidget(square, 1,3,1,4)
        layout.addWidget(find_city, 2, 2, 2, 5)
        layout.addWidget(self.input, 3, 2, 3, 5)
        layout.addWidget(self.forecast_1, 6, 1)
        layout.addWidget(self.forecast_2, 6, 2)
        layout.addWidget(self.forecast_3, 6, 3)
        layout.addWidget(self.forecast_4, 6, 4)
        layout.addWidget(self.forecast_5, 6, 5)
        layout.addWidget(self.forecast_6, 6, 6)
        layout.addWidget(self.forecast_7, 6, 7)

    def update_background(self):
        if self.description_label.text() == "Sunny":
            random_set = random.randint(1, 3)
            sunny_set = f"background-image: url(Backgrounds/Sunny_{random_set}.jpg);"
            self.background.setStyleSheet(sunny_set)

    def find_temp(self):
        ...

    def update_time(self):
        print("started")
        current_time = time.strftime("%H:%M")
        self.time_label.setText(current_time)


if __name__ == "__main__":
    application = QApplication([])
    app = WeatherApp()
    app.show()
    application.exec_()