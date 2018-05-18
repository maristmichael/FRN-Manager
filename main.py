import kivy
kivy.require('1.10.0')
import os
import webbrowser
from pathlib import Path
from kivy.app import App
from Roster import Roster
from kivy.lang import Builder
from Volunteer import Volunteer
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen

class HomeScreen(Screen):
    def screen_switch_dirScreen(self):
        self.manager.transition.direction = 'left'
        self.manager.current = '_DirScreen_'

    def close(self):
        App.get_running_app().stop()

class DirScreen(Screen):
    home = str(Path.home())

    def open(self, path, filename):
        with open(os.path.join(path, filename[0])) as f:
            print (f.read())

    def selected(self, filename):
        print ("selected: %s" % filename[0])

    def screen_switch_previous(self):
        self.manager.transition.direction = 'right'
        self.manager.current = self.manager.previous()

    def screen_switch_RostScreen(self):
        self.manager.transition.direction = 'left'
        self.manager.current = '_RosterScreen_'

class ScrollButton(Button):
    pass

class RosterScreen(Screen):

    def build_roster(self,path,filename):
        file = os.path.join(path, filename[0])
        add_members(file)
        roster_list = get_roster()
        build_ros_screen(roster_list)

    #def build_ros_screen(self, list):
    #    container = self.ids.roster
    #    for members in list:
    #        container.add_widget(ScrollButton(text=members.get_volunteer())




class FoodRecoveryManager(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name='_HomeScreen_'))
        sm.add_widget(DirScreen(name='_DirScreen_'))
        sm.add_widget(DirScreen(name='_RosterScreen_'))

        return Builder.load_file('editor.kv')

if __name__ == '__main__':
    FoodRecoveryManager().run()
