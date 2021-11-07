from kivy.app import App 
from kivy.uix.gridlayout import GridLayout 
from kivy.uix.label import Label 
from kivy.uix.textinput import TextInput 
from kivy.uix.button import Button

class LoginScreen(GridLayout):

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='User Name'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
        self.add_widget(Label(text='password'))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)
        self.response = Label(text="")
        self.add_widget(self.response)

        def login(instance):
            if(self.username.text == "jon" and self.password.text == "password"):
                print("Logged in Successfully!")
                self.response.text = "This is where you would log in...If we actually had an app to login to..."
            else:
                print("Unknown username or password")
        loginButton = Button(text="Login" )
        loginButton.bind(on_press=login)
        self.add_widget(loginButton)

class MyApp(App):
    def build(self):
        return LoginScreen()

if __name__ == '__main__':
    MyApp().run()    