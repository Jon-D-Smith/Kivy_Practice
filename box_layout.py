from kivy.app import App 
from kivy.uix.button import Button 
from kivy.uix.boxlayout import BoxLayout 

class BoxLayoutExample(App):
    def build(self):
        layout = BoxLayout(orientation='horizontal')
        btn1 = Button(text='Click One')
        btn2 = Button(text='Click Two')
        btn3 = Button(text='Click Three')
        btn4 = Button(text='Click Four')
        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(btn3)
        layout.add_widget(btn4)
        return layout

if __name__ == "__main__":
    window = BoxLayoutExample()
    window.run()