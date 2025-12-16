from button import Button
from checkbox import Checkbox

class WindowsButton(Button):
    def paint(self):
        print("Windows button")

class WindowsCheckbox(Checkbox):
    def paint(self):
        print("Windows checkbox")
