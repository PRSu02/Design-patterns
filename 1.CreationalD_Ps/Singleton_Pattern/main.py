from logger import Logger

if __name__ == "__main__":
    logger1 = Logger()
    logger2 = Logger()

    logger1.log("First message")
    logger2.log("Second message")

    print(logger1 is logger2)   # True