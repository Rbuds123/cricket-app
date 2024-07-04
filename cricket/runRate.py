from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen

class RunRateCalculator(Screen):
    def __init__(self, **kwargs):
        super(RunRateCalculator, self).__init__(**kwargs)
        self.title = "Cricket Run Rate Calculator"
        
        # Create the main layout
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Create widgets
        self.runs_label = Label(text="Total Runs Scored:")
        self.runs_input = TextInput(multiline=False)
        
        self.overs_label = Label(text="Total Overs Faced:")
        self.overs_input = TextInput(multiline=False)
        
        self.calculate_button = Button(text="Calculate Run Rate")
        self.calculate_button.bind(on_press=self.calculate_run_rate)
        
        self.result_label = Label(text="Run Rate: -")
        
        # Add widgets to layout
        layout.add_widget(self.runs_label)
        layout.add_widget(self.runs_input)
        layout.add_widget(self.overs_label)
        layout.add_widget(self.overs_input)
        layout.add_widget(self.calculate_button)
        layout.add_widget(self.result_label)
        
        self.add_widget(layout)
    
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
