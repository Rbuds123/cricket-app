from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.uix.anchorlayout import AnchorLayout

class NetRunCalc(Screen):
    def __init__(self, **kwargs):
        super(NetRunCalc, self).__init__(**kwargs)
        
        # Create the main layout using BoxLayout
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10,
                                size_hint=(None, None), size=(300, 400))
        
        # Create widgets
        self.runs_scored_label = Label(text="Total Runs Scored:", size_hint=(1, None), height=30)
        self.runs_scored_input = TextInput(multiline=False, size_hint=(1, None), height=30)
        
        self.overs_faced_label = Label(text="overs faced:", size_hint=(1, None), height=30)
        self.overs_faced_input = TextInput(multiline=False, size_hint=(1, None), height=30)

        self.runs_conceded_label = Label(text="runs conceded:", size_hint=(1, None), height=30)
        self.runs_conceded_input = TextInput(multiline=False, size_hint=(1, None), height=30)

        self.overs_bowled_label = Label(text="overs bowled:", size_hint=(1, None), height=30)
        self.overs_bowled_input = TextInput(multiline=False, size_hint=(1, None), height=30)
        
        self.calculate_button = Button(text="Calculate net Run Rate", size_hint=(1, None), height=40)
        self.calculate_button.bind(on_press=self.calculate_run_rate)
        
        self.result_label = Label(text="Net Run Rate: -", size_hint=(1, None), height=30)
        
        self.back_button = Button(text='Back', size_hint=(1, None), height=40)
        self.back_button.bind(on_press=self.go_home)
        
        # Add widgets to layout
        layout.add_widget(self.runs_scored_label)
        layout.add_widget(self.runs_scored_input)
        layout.add_widget(self.overs_faced_label)
        layout.add_widget(self.overs_faced_input)
        layout.add_widget(self.runs_conceded_label)
        layout.add_widget(self.runs_conceded_input)
        layout.add_widget(self.overs_bowled_label)
        layout.add_widget(self.overs_bowled_input)
        
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
            runs_scored = float(self.runs_scored_input.text)
            over_faced = float(self.overs_faced_input.text)
            runs_conceded = float(self.runs_conceded_input.text)
            over_bowled = float(self.overs_bowled_input.text)
            net_run_rate = (runs_scored / over_faced) - (runs_conceded / over_bowled)
            self.result_label.text = f"Run Rate: {net_run_rate:.2f}"
        except ValueError:
            self.result_label.text = "Please enter valid numbers for runs and overs."