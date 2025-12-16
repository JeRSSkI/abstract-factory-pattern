from gui_factory import GUIFactory
from mac_components import MacButton, MacCheckbox

class MacFactory(GUIFactory):
    def create_button(self):
        return MacButton()

    def create_checkbox(self):
        return MacCheckbox()
