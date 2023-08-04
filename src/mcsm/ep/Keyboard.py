

class Keyboard:

    def forward(self, letter):
        return "ABCDEFGHIJKLMNOPQRSTUVWXYZ".find(letter)

    def backward(self, signal):
        return "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[signal]
