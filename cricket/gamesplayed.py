from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class GameStatsScreen(Screen):
    def __init__(self, **kwargs):
        super(GameStatsScreen, self).__init__(**kwargs)
        
        # Create a ScrollView
        scroll_view = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
        
        # Create a BoxLayout to hold the content vertically
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10,
                                size_hint_y=None)
        self.layout.bind(minimum_height=self.layout.setter('height'))
        
        self.games_label = Label(text="Number of games played:", size_hint=(1, None), height=30)
        self.games_input = TextInput(multiline=False, size_hint=(1, None), height=30)
        self.games_input.bind(on_text_validate=self.generate_game_inputs)
        
        self.layout.add_widget(self.games_label)
        self.layout.add_widget(self.games_input)
        
        scroll_view.add_widget(self.layout)  # Add BoxLayout to ScrollView
        
        anchor_layout = AnchorLayout(anchor_x='center', anchor_y='center')
        anchor_layout.add_widget(scroll_view)  # Add ScrollView to AnchorLayout
        
        self.add_widget(anchor_layout)
        
        # Create total labels and add them to the layout
        self.total_runs_scored_label = Label(text="Total Runs Scored: 0", size_hint=(1, None), height=30)
        self.total_overs_faced_label = Label(text="Total Overs Faced: 0", size_hint=(1, None), height=30)
        self.total_runs_conceded_label = Label(text="Total Runs Conceded: 0", size_hint=(1, None), height=30)
        self.total_overs_bowled_label = Label(text="Total Overs Bowled: 0", size_hint=(1, None), height=30)
        
        self.layout.add_widget(self.total_runs_scored_label)
        self.layout.add_widget(self.total_overs_faced_label)
        self.layout.add_widget(self.total_runs_conceded_label)
        self.layout.add_widget(self.total_overs_bowled_label)
        
        # Add the button at the bottom to trigger totals calculation
        self.calculate_button = Button(text="Calculate Totals", size_hint=(1, None), height=50)
        self.calculate_button.bind(on_press=self.update_totals)
        self.layout.add_widget(self.calculate_button)
    
    def generate_game_inputs(self, instance):
        try:
            num_games = int(self.games_input.text)
            self.clear_game_inputs()  # Clear existing inputs
            
            for i in range(num_games):
                self.add_game_inputs(i + 1)
        except ValueError:
            pass  # Handle invalid input
    
    def clear_game_inputs(self):
        # Clear existing input fields
        self.layout.clear_widgets()
        self.layout.add_widget(self.games_label)
        self.layout.add_widget(self.games_input)
        
        # Reset totals
        self.total_runs_scored_label.text = "Total Runs Scored: 0"
        self.total_overs_faced_label.text = "Total Overs Faced: 0"
        self.total_runs_conceded_label.text = "Total Runs Conceded: 0"
        self.total_overs_bowled_label.text = "Total Overs Bowled: 0"
        
        # Re-add total labels
        self.layout.add_widget(self.total_runs_scored_label)
        self.layout.add_widget(self.total_overs_faced_label)
        self.layout.add_widget(self.total_runs_conceded_label)
        self.layout.add_widget(self.total_overs_bowled_label)
        
        # Re-add the calculate button
        self.layout.add_widget(self.calculate_button)
    
    def add_game_inputs(self, game_number):
        # Create a GridLayout for each game's inputs
        game_layout = GridLayout(cols=2, padding=5, spacing=5,
                                 size_hint_y=None, height=140)
        
        runs_scored_label = Label(text=f"Game {game_number} - Total Runs Scored:", size_hint=(1, None), height=30)
        runs_scored_input = TextInput(multiline=False, size_hint=(1, None), height=30)
        runs_scored_input.bind(text=self.update_totals)
        
        overs_faced_label = Label(text=f"Game {game_number} - Total Overs Faced:", size_hint=(1, None), height=30)
        overs_faced_input = TextInput(multiline=False, size_hint=(1, None), height=30)
        overs_faced_input.bind(text=self.update_totals)
        
        runs_conceded_label = Label(text=f"Game {game_number} - Total Runs Conceded:", size_hint=(1, None), height=30)
        runs_conceded_input = TextInput(multiline=False, size_hint=(1, None), height=30)
        runs_conceded_input.bind(text=self.update_totals)
        
        overs_bowled_label = Label(text=f"Game {game_number} - Total Overs Bowled:", size_hint=(1, None), height=30)
        overs_bowled_input = TextInput(multiline=False, size_hint=(1, None), height=30)
        overs_bowled_input.bind(text=self.update_totals)
        
        # Add labels and inputs to game_layout
        game_layout.add_widget(runs_scored_label)
        game_layout.add_widget(runs_scored_input)
        game_layout.add_widget(overs_faced_label)
        game_layout.add_widget(overs_faced_input)
        game_layout.add_widget(runs_conceded_label)
        game_layout.add_widget(runs_conceded_input)
        game_layout.add_widget(overs_bowled_label)
        game_layout.add_widget(overs_bowled_input)

        # Add game_layout to self.layout
        self.layout.add_widget(game_layout, index=2)
        
        self.games_input.focus = True  # Return focus to games_input after adding inputs
    
    def update_totals(self, instance=None, *args):
        total_runs_scored = 0
        total_overs_faced = 0
        total_runs_conceded = 0
        total_overs_bowled = 0

        print("Updating totals...")  # Debugging print
        
        for child in self.layout.children:
            if isinstance(child, GridLayout):
                runs_scored_input = child.children[1]
                overs_faced_input = child.children[3]
                runs_conceded_input = child.children[5]
                overs_bowled_input = child.children[7]
                
                try:
                    print(f"Runs Scored Input: {runs_scored_input.text}")  # Debugging print
                    print(f"Overs Faced Input: {overs_faced_input.text}")  # Debugging print
                    print(f"Runs Conceded Input: {runs_conceded_input.text}")  # Debugging print
                    print(f"Overs Bowled Input: {overs_bowled_input.text}")  # Debugging print

                    total_runs_scored += int(runs_scored_input.text) if runs_scored_input.text else 0
                    total_overs_faced += int(overs_faced_input.text) if overs_faced_input.text else 0
                    total_runs_conceded += int(runs_conceded_input.text) if runs_conceded_input.text else 0
                    total_overs_bowled += int(overs_bowled_input.text) if overs_bowled_input.text else 0
                except ValueError:
                    pass
        
        print(f"Total Runs Scored: {total_runs_scored}")  # Debugging print
        print(f"Total Overs Faced: {total_overs_faced}")  # Debugging print
        print(f"Total Runs Conceded: {total_runs_conceded}")  # Debugging print
        print(f"Total Overs Bowled: {total_overs_bowled}")  # Debugging print
        
        self.total_runs_scored_label.text = f"Total Runs Scored: {total_runs_scored}"
        self.total_overs_faced_label.text = f"Total Overs Faced: {total_overs_faced}"
        self.total_runs_conceded_label.text = f"Total Runs Conceded: {total_runs_conceded}"
        self.total_overs_bowled_label.text = f"Total Overs Bowled: {total_overs_bowled}"

class MyApp(App):
    def build(self):
        screen_manager = ScreenManager()
        screen_manager.add_widget(GameStatsScreen(name='game_stats'))
        return screen_manager

if __name__ == '__main__':
    MyApp().run()
