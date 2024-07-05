from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from home_screen import HomeScreen
from runRate import RunRateCalculator
from dlscalc import DuckworthLewisCalculator
from netruncalc import NetRunCalc

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(RunRateCalculator(name='runrate'))
        sm.add_widget(DuckworthLewisCalculator(name='dlscalc'))
        sm.add_widget(NetRunCalc(name='netrunrate'))
        return sm

if __name__ == '__main__':
    MyApp().run()
