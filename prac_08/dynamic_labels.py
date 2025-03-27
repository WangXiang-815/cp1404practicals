"""
EST:20mins
ACT:
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

class DynamicLabels(App):

    def __init__(self, **kwargs):
        """Define the data"""
        super().__init__(**kwargs)
        self.names_dict = {1:'Alice', 2:'Bob', 3:'Tom', 4:'David', 5:'Charlie'}

    def build(self):
        """Build the kivy GUI"""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file("dynamic_labels.kv")

        for key,name in self.names_dict.items():
            temp_label = Label(text=name, font_size=40)
            self.root.ids.main.add_widget(temp_label)

        return self.root



if __name__ == '__main__':
    DynamicLabels().run()