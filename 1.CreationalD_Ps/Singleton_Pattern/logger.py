from singleton import Singleton

class Logger(Singleton):
    def log(self, message):
        print(f"LOG: {message}")