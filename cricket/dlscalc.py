from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class DuckworthLewisCalculator(Screen):
    def calculate_dls_target(self, instance):
        try:
            current_score = float(self.current_score_input.text)
            overs_remaining = float(self.overs_remaining_input.text)
            overs_to_be_played = float(self.overs_to_be_played_input.text)

            par_score = (current_score / overs_remaining) * overs_to_be_played
            self.result_label.text = f"Duckworth-Lewis Target: {par_score:.2f}"
        except ValueError:
            self.result_label.text = "Invalid input! Please enter numbers."

    def go_back(self, instance):
        self.manager.current = 'home'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # Main layout using BoxLayout with responsive size_hint
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10,
                                size_hint=(None, None), size=(300, 400))
        
        # Adding widgets to main layout
        main_layout.add_widget(Label(text='Duckworth-Lewis Calculator', size_hint=(1, None), height=30))
        
        self.error_label = Label(text='Current Score', size_hint=(1, None), height=30)
        main_layout.add_widget(self.error_label)

        self.current_score_input = TextInput(multiline=False, size_hint=(1, None), height=30)
        main_layout.add_widget(self.current_score_input)

        self.error_label = Label(text='Overs Remaining', size_hint=(1, None), height=30)
        main_layout.add_widget(self.error_label)

        self.overs_remaining_input = TextInput(multiline=False, size_hint=(1, None), height=30)
        main_layout.add_widget(self.overs_remaining_input)

        self.error_label = Label(text='Overs to be Played', size_hint=(1, None), height=30)
        main_layout.add_widget(self.error_label)

        self.overs_to_be_played_input = TextInput(multiline=False, size_hint=(1, None), height=30)
        main_layout.add_widget(self.overs_to_be_played_input)

        calculate_button = Button(text='Calculate DLS Target', size_hint=(1, None), height=40)
        calculate_button.bind(on_press=self.calculate_dls_target)
        main_layout.add_widget(calculate_button)

        self.result_label = Label(text='', size_hint=(1, None), height=30)
        main_layout.add_widget(self.result_label)

        back_button = Button(text='Back', size_hint=(1, None), height=40)
        back_button.bind(on_press=self.go_back)
        main_layout.add_widget(back_button)
        
        # AnchorLayout to center the BoxLayout vertically and horizontally
        anchor_layout = AnchorLayout(anchor_x='center', anchor_y='center')
        anchor_layout.add_widget(main_layout)
        
        self.add_widget(anchor_layout)

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(DuckworthLewisCalculator(name='dlscalc'))
        return sm

if __name__ == '__main__':
    MyApp().run()
