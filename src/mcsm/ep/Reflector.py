
class Reflector:

    def __init__(self, right_code):
        self.left = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.right = right_code

    def reflect(self, signal):
        letter = self.right[signal]
        signal = self.left.find(letter)

        return signal
