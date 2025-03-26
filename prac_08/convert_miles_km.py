"""
EST: 1hr
ACT:
python codes for converting miles to kilometers
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class ConvertMiles(App):
    """ConvertMiles is kivy app for converting miles to kilometers"""
    def build(self):
        """build the Kivy app from the kv file"""
        Window.size = (300,200)
        self.title = 'Convert Miles to Kilometers'
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root



ConvertMiles().run()