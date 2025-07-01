# Dice como se representa la secuencia

class Sequence:
    def __init__(self, identifier: str, sequence: str):
        self.identifier = identifier
        self.sequence = sequence

    def __repr__(self):
        return f">{self.identifier}\n{self.sequence}"
    def get_id(self):
        return self.identifier
    def get_secuencia(self):
        return self.sequence