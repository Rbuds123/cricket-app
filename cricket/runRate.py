from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.uix.anchorlayout import AnchorLayout

class RunRateCalculator(Screen):
    def __init__(self, **kwargs):
        super(RunRateCalculator, self).__init__(**kwargs)
        
        # Create the main layout using BoxLayout
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10,
                                size_hint=(None, None), size=(300, 400))
        
        # Create widgets
        self.runs_label = Label(text="Total Runs Scored:", size_hint=(1, None), height=30)
        self.runs_input = TextInput(multiline=False, size_hint=(1, None), height=30)
        
        self.overs_label = Label(text="Total Overs Faced:", size_hint=(1, None), height=30)
        self.overs_input = TextInput(multiline=False, size_hint=(1, None), height=30)
        
        self.calculate_button = Button(text="Calculate Run Rate", size_hint=(1, None), height=40)
        self.calculate_button.bind(on_press=self.calculate_run_rate)
        
        self.result_label = Label(text="Run Rate: -", size_hint=(1, None), height=30)
        
        self.back_button = Button(text='Back', size_hint=(1, None), height=40)
        self.back_button.bind(on_press=self.go_home)
        
        # Add widgets to layout
        layout.add_widget(self.runs_label)
        layout.add_widget(self.runs_input)
        layout.add_widget(self.overs_label)
        layout.add_widget(self.overs_input)
        layout.add_widget(self.calculate_button)
        layout.add_widget(self.result_label)
        layout.add_widget(self.back_button)
        
        # AnchorLayout to center the BoxLayout vertically and horizontally
        anchor_layout = AnchorLayout(anchor_x='center', anchor_y='center')
        anchor_layout.add_widget(layout)
        
        self.add_widget(anchor_layout)
    
    def on_pre_enter(self):
        pass
    
    def go_home(self, instance):
        self.manager.current = 'home'
    
    def calculate_run_rate(self, instance):
        try:
            runs = float(self.runs_input.text)
            overs = float(self.overs_input.text)
            
            if overs == 0:
                self.result_label.text = "Overs faced cannot be zero."
            else:
                run_rate = runs / overs
                self.result_label.text = f"Run Rate: {run_rate:.2f}"
        except ValueError:
            self.result_label.text = "Please enter valid numbers for runs and overs."