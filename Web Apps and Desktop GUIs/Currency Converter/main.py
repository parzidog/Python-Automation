from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QLineEdit,
    QComboBox,
)
from PyQt6.QtCore import Qt
from bs4 import BeautifulSoup
import requests


def get_currency(from_curr, to_curr):
    amount = text.text()
    url = f"https://www.x-rates.com/calculator/?from={from_curr}&to={to_curr}&amount={amount}"
    content = requests.get(url).text
    soup = BeautifulSoup(content, "html.parser")
    currency = soup.find("span", class_="ccOutputRslt").get_text()
    currency = round(float("".join(currency[0:-4].split(","))), 2)

    return currency


def Converter():
    input_txt = round(float(text.text()), 2)
    have_curr = from_curr.currentText()
    exp_curr = to_curr.currentText()
    rate = get_currency(have_curr, exp_curr)
    output = round(input_txt * rate, 2)
    output_label.setText(f"{input_txt} {have_curr} is equal to {output} {exp_curr}")


currencies = ["usd", "eur", "aud", "inr", "jpy"]


app = QApplication([])
window = QWidget()

window.setWindowTitle("Currency Converter")

layout = QVBoxLayout()
layout1 = QVBoxLayout()
layout2 = QVBoxLayout()
layout3 = QHBoxLayout()

from_curr = QComboBox()
from_curr.addItems(currencies)
layout1.addWidget(from_curr)

to_curr = QComboBox()
to_curr.addItems(currencies)
layout1.addWidget(to_curr)

text = QLineEdit()
layout2.addWidget(text)

btn = QPushButton("Convert")
layout2.addWidget(btn, alignment=Qt.AlignmentFlag.AlignBottom)
btn.clicked.connect(Converter)


layout3.addLayout(layout1)
layout3.addLayout(layout2)

layout.addLayout(layout3)

output_label = QLabel("")
layout.addWidget(output_label)

window.setLayout(layout)

window.show()
app.exec()
