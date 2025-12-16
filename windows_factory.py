from gui_factory import GUIFactory
from windows_components import WindowsButton, WindowsCheckbox

class WindowsFactory(GUIFactory):
    def create_button(self):
        return WindowsButton()

    def create_checkbox(self):
        return WindowsCheckbox()
