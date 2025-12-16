from button import Button
from checkbox import Checkbox

class MacButton(Button):
    def paint(self):
        print("Mac button")

class MacCheckbox(Checkbox):
    def paint(self):
        print("Mac checkbox")
