from PyQt5.QtWidgets import QDialog, QLabel, QVBoxLayout, QPushButton, QHBoxLayout

from src.gui.pp.Keyboard import main_keyboard
from src.gui.pp.Plugboard import plugboard

from src.mcsm.Enigma import Enigma


class Window(QDialog):

    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        self.enigma = Enigma()

        self.list_plugboard = ""
        self.text_field1 = ""
        self.text_field2 = ""
        self.text_input = ""
        self.text_output = ""

        self.setGeometry(700, 700, 700, 700)
        self.setWindowTitle("Enigma")

        self.original_text = QLabel()
        self.original_text.setGeometry(700, 700, 700, 700)
        self.original_text.setWordWrap(True)
        font_ot = self.original_text.font()
        font_ot.setPointSize(20)
        self.original_text.setFont(font_ot)
        self.encrypt_text = QLabel()
        self.encrypt_text.setGeometry(700, 700, 700, 700)
        self.encrypt_text.setWordWrap(True)
        self.encrypt_text.setFont(font_ot)

        self.label1 = QLabel("plain text")
        self.label2 = QLabel("chipper text")

        self.encrypt_button = QPushButton("Encrypt")
        self.encrypt_button.clicked.connect(self.encrypt_label)
        self.decrypt_button = QPushButton("Decrypt")
        self.decrypt_button.clicked.connect(self.decrypt_label)

        self.clear_button = QPushButton("Clear All")
        self.clear_button.clicked.connect(self.clear_all)

        self.plugboard = plugboard(self.text_field1_oc, self.text_field2_oc, self.switch_letter)
        self.label3 = QLabel()

        layout_decen = QHBoxLayout()
        layout_decen.addWidget(self.encrypt_button)
        layout_decen.addWidget(self.decrypt_button)

        layout_main = QVBoxLayout()
        layout_main.addWidget(self.clear_button)
        layout_main.addLayout(layout_decen)
        layout_main.addWidget(self.label1)
        layout_main.addWidget(self.original_text)
        layout_main.addWidget(self.label2)
        layout_main.addWidget(self.encrypt_text)
        layout_main.addLayout(main_keyboard(lambda: self.input_keyboard("Q"), lambda: self.input_keyboard("W"),
                                            lambda: self.input_keyboard("E"),
                                            lambda: self.input_keyboard("R"), lambda: self.input_keyboard("T"),
                                            lambda: self.input_keyboard("Y"),
                                            lambda: self.input_keyboard("U"), lambda: self.input_keyboard("I"),
                                            lambda: self.input_keyboard("O"),
                                            lambda: self.input_keyboard("P"), lambda: self.input_keyboard("A"),
                                            lambda: self.input_keyboard("S"),
                                            lambda: self.input_keyboard("D"), lambda: self.input_keyboard("F"),
                                            lambda: self.input_keyboard("G"),
                                            lambda: self.input_keyboard("H"), lambda: self.input_keyboard("J"),
                                            lambda: self.input_keyboard("K"),
                                            lambda: self.input_keyboard("L"), lambda: self.input_keyboard("Z"),
                                            lambda: self.input_keyboard("X"),
                                            lambda: self.input_keyboard("C"), lambda: self.input_keyboard("V"),
                                            lambda: self.input_keyboard("B"),
                                            lambda: self.input_keyboard("N"), lambda: self.input_keyboard("M")))

        layout_main.addLayout(self.plugboard)
        layout_main.addWidget(QLabel("plugboard list:"))
        layout_main.addWidget(self.label3)

        self.setLayout(layout_main)

    def clear_all(self):
        self.text_input = ""
        self.text_output = ""
        self.original_text.setText(self.text_input)
        self.encrypt_text.setText(self.text_output)
        self.enigma = Enigma()
        self.list_plugboard = ""
        self.label3.setText(self.list_plugboard)
        self.enigma.default_plugboard()

    def input_keyboard(self, letter):
        self.text_input += letter
        self.text_output += self.enigma.encrypt(letter)
        self.original_text.setText(self.text_input)
        self.encrypt_text.setText(self.text_output)

    def encrypt_label(self):
        self.text_input = ""
        self.text_output = ""
        self.original_text.setText(self.text_input)
        self.encrypt_text.setText(self.text_output)
        self.enigma = Enigma()
        self.label1.setText("plain text")
        self.label2.setText("chipper text")

    def decrypt_label(self):
        self.text_input = ""
        self.text_output = ""
        self.original_text.setText(self.text_input)
        self.encrypt_text.setText(self.text_output)
        self.enigma = Enigma()
        self.label1.setText("chipper text")
        self.label2.setText("plain text")

    def text_field1_oc(self, text):
        self.text_field1 = text

    def text_field2_oc(self, text):
        self.text_field2 = text

    def switch_letter(self):
        if len(self.text_field1) != 1:
            return
        if len(self.text_field2) != 1:
            return

        self.enigma.switch_letter(self.text_field1, self.text_field2)

        if len(self.list_plugboard) == 0:
            self.list_plugboard += self.text_field1 + self.text_field2
        else:
            self.list_plugboard += "," + self.text_field1 + self.text_field2

        self.label3.setText(self.list_plugboard)




