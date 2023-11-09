import time
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import requests
import json
import random

url = "http://ipinfo.io/json"
response = requests.get(url)
data = json.loads(response.text)
city = data['city']
API_key = ""

# forecast = data.json()
forcast = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_key}&units=metric")
datum = json.loads(forcast.text)['list'][2:]
target_time = ["12:00:00", "18:00:00"]
for i in [j for j in datum if j['dt_txt'].split()[-1] == target_time[0] or j['dt_txt'].split()[-1] == target_time[1]]:
    print(i)
    print(i['main']['temp'])
    print(i['weather'][0]['main'])
    print(i['wind']['speed'])
print(json.loads(forcast.text))


# print(forecast['main']['temp'])
# print(forecast['weather'][0]['main'])
# print(datetime.date.today().month)

class WeatherApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.set_background()
        self.set_upper_square()
        self.create_upper_settings()
        self.fill_square()
        self.set_note()
        self.set_input()
        self.set_forecast()
        self.order_everything()
        self.fill_background()
        self.set_timer()

    def order_everything(self) -> None:
        self.layout.addWidget(self.main_square, 1, 3, 1, 4)
        self.layout.addWidget(self.find_city, 2, 2, 2, 5)
        self.layout.addWidget(self.input, 3, 2, 3, 5)
        self.layout.addWidget(self.forecast_1, 6, 1)
        self.layout.addWidget(self.forecast_2, 6, 2)
        self.layout.addWidget(self.forecast_3, 6, 3)
        self.layout.addWidget(self.forecast_4, 6, 4)
        self.layout.addWidget(self.forecast_5, 6, 5)
        self.layout.addWidget(self.forecast_6, 6, 6)
        self.layout.addWidget(self.forecast_7, 6, 7)

    def create_upper_settings(self) -> None:
        weather = self.find_out_weather()
        self.time_label = QLabel(time.strftime("%H:%M"), self)
        self.time_label.setFont(QFont("Roboto", 26))
        self.time_label.setStyleSheet("color: white;background-color: black;")
        self.time_label.setAlignment(Qt.AlignCenter)
        self.description_label = QLabel(weather['weather'][0]['main'], self)
        self.description_label.setFont(QFont("Roboto", 26))
        self.description_label.setStyleSheet("color: white;background-color: black;")
        self.description_label.setAlignment(Qt.AlignCenter)
        self.temperature_label = QLabel(str(weather['main']['temp']) + "°C", self)
        self.temperature_label.setFont(QFont("Roboto", 26))
        self.temperature_label.setStyleSheet("color: white;background-color: black;")
        self.temperature_label.setAlignment(Qt.AlignCenter)

    def set_upper_square(self) -> None:
        self.main_square = QFrame(self)
        self.main_square.setFrameShape(QFrame.StyledPanel)
        self.main_square.setFrameShadow(QFrame.Raised)
        self.main_square.setStyleSheet("background-color: black;border-radius: 20px;")

    def set_background(self) -> None:
        self.background = QFrame(self)
        self.background.setFixedSize(1500, 1100)
        self.setWindowTitle('Weather App')
        self.setWindowIcon(QIcon('icon.png'))
        self.setFixedSize(1300, 900)
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.layout = QGridLayout()
        self.central_widget.setLayout(self.layout)

    def set_timer(self) -> None:
        self.time_timer = QTimer(self)
        self.time_timer.timeout.connect(self.update_time)
        self.time_timer.start(10000)

    def set_input(self) -> None:
        self.input = QLineEdit()
        self.input.setFont(QFont("Roboto", 30))

    def set_note(self) -> None:
        self.find_city = QLabel("Find your city!")
        self.find_city.setAlignment(Qt.AlignCenter)
        self.find_city.setFont(QFont("Roboto", 40))

    def set_forecast(self) -> None:
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

    def fill_background(self) -> None:
        if self.description_label.text() == "Sunny":
            random_set = random.randint(1, 8)
            sett = f"background-image: url(Backgrounds/Sunny/Sunny_{random_set}.jpg);"
            self.background.setStyleSheet(sett)
        elif self.description_label.text() == "Clear":
            random_set = random.randint(1, 4)
            sett = f"background-image: url(Backgrounds/Clear/Clear_{random_set}.jpg);"
            self.background.setStyleSheet(sett)

        elif self.description_label.text() == "Clouds":
            random_set = random.randint(1, 5)
            sett = f"background-image: url(Backgrounds/Clouds/Clouds_{random_set}.jpg);"
            self.background.setStyleSheet(sett)

    def fill_square(self) -> None:
        self.labels_layout = QHBoxLayout()
        self.labels_layout.addWidget(self.description_label)
        self.labels_layout.addWidget(self.time_label)
        self.labels_layout.addWidget(self.temperature_label)
        self.main_square.setLayout(self.labels_layout)
        self.main_square.setFixedSize(500, 120)

    def find_out_forecast(self, city: str = None):
        if city == None:
            city = self.find_user_city()
        forcast = requests.get(
            f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_key}&units=metric")
        datum = json.loads(forcast.text)['list'][2:]
        target_time = ["12:00:00", "18:00:00"]
        forecasts = [[]]
        count = 0
        j = 0
        for i in [j for j in datum if
                  j['dt_txt'].split()[-1] == target_time[0] or j['dt_txt'].split()[-1] == target_time[1]]:
            count += 1
            forecasts[j].append(i['main']['temp'])
            forecasts[j].append(i['weather'][0]['main'])
            forecasts[j].append(i['wind']['speed'])
            if count == 3:
                j += 1
                forecasts.append([i])
        return forecasts

    def find_out_weather(self, city: str = None) -> json:
        if city is None:
            city = self.find_user_city()
        data = requests.get(f"http://api.openweathermap.org/data/2.5/weather?appid={API_key}&q={city}&units=metric")
        return json.loads(data.text)

    def find_user_city(self) -> str:
        url = "http://ipinfo.io/json"
        response = requests.get(url)
        data = json.loads(response.text)
        return data['city']

    def update_time(self) -> None:
        current_time = time.strftime("%H:%M")
        self.time_label.setText(current_time)

    def populate_forecast_frame(self):
        ...


if __name__ == "__main__":
    application = QApplication([])
    app = WeatherApp()
    app.show()
    application.exec_()
