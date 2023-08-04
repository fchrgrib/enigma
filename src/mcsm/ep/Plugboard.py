
class Plugboard:

    def __init__(self):
        self.left = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.right = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def switch_letter(self, letter_a, letter_b):
        A = self.left.find(letter_a)
        B = self.right.find(letter_b)

        self.left = self.left[:A] + letter_b + self.left[A+1:]
        self.left = self.left[:B] + letter_a + self.left[B+1:]

    def forward(self, signal):
        letter = self.right[signal]
        signal = self.left.find(letter)

        return signal

    def backward(self, signal):
        letter = self.left[signal]
        signal = self.right.find(letter)

        return signal

    def default(self):
        self.left = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.right = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

