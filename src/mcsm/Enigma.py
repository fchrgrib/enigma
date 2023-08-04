from src.mcsm.ep import Reflector, Keyboard, Plugboard, Rotor


class Enigma:

    def __init__(self):
        self.keyboard = Keyboard.Keyboard()
        self.plugboard = Plugboard.Plugboard()
        self.rotorI = Rotor.Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Y")
        self.rotorII = Rotor.Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", "M")
        self.rotorIII = Rotor.Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", "D")
        self.reflector = Reflector.Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")

    def encrypt(self, letter):
        if self.rotorII.left[0] == self.rotorII.notch and self.rotorIII.left[0] == self.rotorIII.notch:
            self.rotorI.rotate()
            self.rotorII.rotate()
            self.rotorIII.rotate()
        elif self.rotorII.left[0] == self.rotorII.notch:
            self.rotorI.rotate()
            self.rotorII.rotate()
            self.rotorIII.rotate()
        elif self.rotorIII.left[0] == self.rotorIII.notch:
            self.rotorII.rotate()
            self.rotorIII.rotate()
        else:
            self.rotorIII.rotate()

        signal = self.keyboard.forward(letter)
        signal = self.plugboard.forward(signal)
        signal = self.rotorIII.forward(signal)
        signal = self.rotorII.forward(signal)
        signal = self.rotorI.forward(signal)
        signal = self.reflector.reflect(signal)
        signal = self.rotorI.backward(signal)
        signal = self.rotorII.backward(signal)
        signal = self.rotorIII.backward(signal)
        signal = self.plugboard.backward(signal)

        return self.keyboard.backward(signal)

    def switch_letter(self, letter_a, letter_b):
        self.plugboard.switch_letter(letter_a, letter_b)

    def default_plugboard(self):
        self.plugboard.default()