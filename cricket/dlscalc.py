from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class DuckworthLewisCalculator(Screen):
    def calculate_dls_target(self, instance):
        try:
            # Get input values from text inputs
            current_score = float(self.current_score_input.text)
            overs_remaining = float(self.overs_remaining_input.text)
            resources_used = float(self.resources_used_input.text)

            # Implement Duckworth-Lewis formula (simplified for demonstration)
            par_score = (current_score / overs_remaining) * resources_used

            # Update the result label
            self.result_label.text = f"Duckworth-Lewis Target: {par_score:.2f}"
        
        except ValueError:
            self.result_label.text = "Invalid input! Please enter numbers."

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')

        layout.add_widget(Label(text='Duckworth-Lewis Calculator'))
        self.error_label = Label(text='current score')
        layout.add_widget(self.error_label)

        self.current_score_input = TextInput(multiline=False)
        layout.add_widget(self.current_score_input)

        self.error_label = Label(text='overs remaining')
        layout.add_widget(self.error_label)

        self.overs_remaining_input = TextInput(multiline=False)
        layout.add_widget(self.overs_remaining_input)

        self.error_label = Label(text='resources used')
        layout.add_widget(self.error_label)
        
        self.resources_used_input = TextInput(multiline=False)
        layout.add_widget(self.resources_used_input)

        calculate_button = Button(text='Calculate DLS Target')
        calculate_button.bind(on_press=self.calculate_dls_target)
        layout.add_widget(calculate_button)

        self.result_label = Label(text='')
        layout.add_widget(self.result_label)

        self.add_widget(layout)
