from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class DynamicLabelsApp(App):
    def build(self):
        self.root = Builder.load_file('dynamic_labels.kv')

        names = ["Alice", "Bob", "Charlie", "Diana"]

        main_layout = self.root.ids.main

        for name in names:
            label = Label(text=name)
            main_layout.add_widget(label)

        return self.root

if __name__ == "__main__":
    DynamicLabelsApp().run()
