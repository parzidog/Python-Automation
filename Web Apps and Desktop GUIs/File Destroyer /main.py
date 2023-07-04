from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QLineEdit,
    QComboBox,
    QFileDialog,
)
from PyQt6.QtCore import Qt
from pathlib import Path


def open_files():
    global filenames
    filenames, _ = QFileDialog.getOpenFileNames(window, "Select Files")

    files.setText("Files Selected: ")

    for file in filenames:
        global widget
        widget = QLabel(f"{file}")
        layout.addWidget(widget)


def destroy_files():
    for file in filenames:
        path = Path(file)
        with open(path, "wb") as f:
            f.write(b"")
        path.unlink()
        app.quit()


app = QApplication([])
window = QWidget()

window.setWindowTitle("Currency Converter")
layout = QVBoxLayout()

description = QLabel(
    'Select the files you want to destroy. The files will be <font color="red">PERMANENTLY</font> deleted'
)
layout.addWidget(description)

open_btn = QPushButton("Open Files")
open_btn.setToolTip("Open the files to destroy")
open_btn.setFixedWidth(150)
layout.addWidget(open_btn, alignment=Qt.AlignmentFlag.AlignCenter)
open_btn.clicked.connect(open_files)

destroy_btn = QPushButton("Destroy Files")
destroy_btn.setToolTip("Permanently Destroy Files")
destroy_btn.setFixedWidth(150)
layout.addWidget(destroy_btn, alignment=Qt.AlignmentFlag.AlignCenter)
destroy_btn.clicked.connect(destroy_files)

files = QLabel("No Files Selected")
layout.addWidget(files)

window.setLayout(layout)

window.show()
app.exec()
