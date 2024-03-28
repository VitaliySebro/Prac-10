from kivy.app import App 
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.slider import Slider
from kivy.uix.spinner import Spinner
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import ScreenManager, Screen

class MainScreen(Screen):
    def __init__(self, name="main"):
        super().__init__(name=name)
        layout = BoxLayout(orientation='horizontal')
        
        btn1 = Button(text="Go to Screen 1", on_press=self.switch_to_screen1)
        btn2 = Button(text="Go to Screen 2", on_press=self.switch_to_screen2)
        btn3 = Button(text="Go to Screen 3", on_press=self.switch_to_screen3)
        btn4 = Button(text="Go to Screen 4", on_press=self.switch_to_screen4)
        
        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(btn3)
        layout.add_widget(btn4)
        
        self.add_widget(layout)

    def switch_to_screen1(self, instance):
        self.manager.current = 'screen1'

    def switch_to_screen2(self, instance):
        self.manager.current = 'screen2'

    def switch_to_screen3(self, instance):
        self.manager.current = 'screen3'

    def switch_to_screen4(self, instance):
        self.manager.current = 'screen4'

class OtherScreen1(Screen):
    def __init__(self, name="first"):
        super().__init__(name=name)
        layout = BoxLayout(orientation='vertical') 
        back_btn = Button(text="Back to Main", on_press=self.switch_back)
        input = TextInput(hint_text="Enter your text")
        self.txt = Label(text="Welcome to Screen 1", font_size=20)
        layout.add_widget(self.txt)  
        layout.add_widget(input) 
        layout.add_widget(back_btn)
        self.add_widget(layout)

    def switch_back(self, instance):
        self.manager.current = 'main'
        
class OtherScreen2(Screen):
    def __init__(self, name="second"):
        super().__init__(name=name)
        layout = BoxLayout(orientation='vertical')
        back_btn = Button(text="Back to Main", on_press=self.switch_back)
        spinner = Spinner(text='Choose an option', values=('Option 1', 'Option 2', 'Option 3'))
        layout.add_widget(Label(text="Screen 2", font_size=20))
        layout.add_widget(spinner)
        layout.add_widget(back_btn)
        self.add_widget(layout)

    def switch_back(self, instance):
        self.manager.current = 'main'
        
class OtherScreen3(Screen):
    def __init__(self, name="third"):
        super().__init__(name=name)
        layout = BoxLayout(orientation='vertical')
        back_btn = Button(text="Back to Main", on_press=self.switch_back)
        slider = Slider(min=0, max=100, value=50)
        layout.add_widget(Label(text="Screen 3", font_size=20))
        layout.add_widget(slider)
        layout.add_widget(back_btn)
        self.add_widget(layout)

    def switch_back(self, instance):
        self.manager.current = 'main'
        
class OtherScreen4(Screen):
    def __init__(self, name="fourth"):
        super().__init__(name=name)
        layout = BoxLayout(orientation='vertical')
        back_btn = Button(text="Back to Main", on_press=self.switch_back)
        scroll_view = ScrollView()
        content = BoxLayout(orientation='vertical')
        for i in range(10):
            content.add_widget(Label(text="Option {}".format(i+1)))
        scroll_view.add_widget(content)
        layout.add_widget(Label(text="Screen 4", font_size=20))
        layout.add_widget(scroll_view)
        layout.add_widget(back_btn)
        self.add_widget(layout)

    def switch_back(self, instance):
        self.manager.current = 'main'

class MyApp(App):
    def build(self):
        screen_manager = ScreenManager()
        main_screen = MainScreen()
        screen1 = OtherScreen1('screen1')
        screen2 = OtherScreen2('screen2')
        screen3 = OtherScreen3('screen3')
        screen4 = OtherScreen4('screen4')

        screen_manager.add_widget(main_screen)
        screen_manager.add_widget(screen1)
        screen_manager.add_widget(screen2)
        screen_manager.add_widget(screen3)
        screen_manager.add_widget(screen4)

        return screen_manager

MyApp().run()

