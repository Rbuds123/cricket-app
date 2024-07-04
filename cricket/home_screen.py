from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        label = Label(text="Welcome to the Home Screen", font_size='20sp')
        layout.add_widget(label)
        
        btn1 = Button(text="Run Rate Calculator", font_size='20sp')
        btn1.bind(on_press=self.go_to_run_rate_calculator)
        layout.add_widget(btn1)
        
        btn2 = Button(text="Duckworth-Lewis-Stern Calculator", font_size='20sp')
        btn2.bind(on_press=self.go_to_dls_calculator)
        layout.add_widget(btn2)
        
        self.add_widget(layout)

    def go_to_run_rate_calculator(self, instance):
        self.manager.current = 'runrate'

    def go_to_dls_calculator(self, instance):
        self.manager.current = 'dlscalc'
