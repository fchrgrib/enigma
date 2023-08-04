from PyQt5.QtWidgets import QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit


def plugboard(text_field1_connect, text_field2_connect, button_connect):
    layout_main = QVBoxLayout()
    layout_main.addWidget(QLabel("Plugboard:"))

    text_field1 = QLineEdit()
    text_field1.setPlaceholderText("Example: A")
    text_field1.textChanged.connect(text_field1_connect)

    text_field2 = QLineEdit()
    text_field2.setPlaceholderText("Example: B")
    text_field2.textChanged.connect(text_field2_connect)

    button = QPushButton("Post")
    button.clicked.connect(button_connect)

    layout_part = QHBoxLayout()
    layout_part.addWidget(text_field1)
    layout_part.addWidget(QLabel("to"))
    layout_part.addWidget(text_field2)
    layout_part.addWidget(button)
    layout_main.addLayout(layout_part)

    return layout_main
