from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class MyBoxLayout(BoxLayout):
    pass
 
class BoxLayoutEx(App):
    def build(self):
 
 
        return MyBoxLayout()
 
if __name__ == "__main__":
    window = BoxLayoutEx()
    window.run()