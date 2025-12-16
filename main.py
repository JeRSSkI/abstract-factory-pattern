from windows_factory import WindowsFactory
from mac_factory import MacFactory

def create_ui(factory):
    button = factory.create_button()
    checkbox = factory.create_checkbox()
    button.paint()
    checkbox.paint()

create_ui(WindowsFactory())
create_ui(MacFactory())
