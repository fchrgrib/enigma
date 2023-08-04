import sys

from PyQt5.QtWidgets import QApplication

from src.gui.MainProgram import Window

if __name__ == '__main__':

    app = QApplication(sys.argv)

    main = Window()
    main.show()
    sys.exit(app.exec_())

