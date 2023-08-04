

class Rotor:

    def __init__(self, right_code, notch):
        self.left = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.right = right_code
        self.notch = notch

    def forward(self, signal):
        letter = self.right[signal]
        signal = self.left.find(letter)

        return signal

    def backward(self, signal):
        letter = self.left[signal]
        signal = self.right.find(letter)

        return signal

    def rotate(self):
        self.right = self.right[1:] + self.right[0]
        self.left = self.left[1:] + self.left[0]
