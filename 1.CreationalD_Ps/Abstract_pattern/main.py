from factory import WindowsFactory, MacFactory


def client_code(factory):
    button = factory.create_button()
    checkbox = factory.create_checkbox()

    print(button.paint())
    print(checkbox.paint())


if __name__ == "__main__":
    print("Windows UI:")
    client_code(WindowsFactory())

    print("\nMac UI:")
    client_code(MacFactory())