from PySide2.QtWidgets import *

if __name__ == '__main__':
    app = QApplication([])

    wdg = QWidget()

    hbox = QHBoxLayout()

    vbox = QVBoxLayout()
    vbox.addLayout(hbox)

    wdg.setLayout(vbox)
