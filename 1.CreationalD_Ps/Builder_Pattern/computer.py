class Computer:
    def __init__(self):
        self.cpu = None
        self.ram = None
        self.storage = None
        self.gpu = None
    
    def __str__(self):
        return f"Computer(CPU: {self.cpu}, RAM: {self.ram}, Storage: {self.storage}, GPU: {self.gpu})"
