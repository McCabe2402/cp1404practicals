from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty


class ConvertMilesToKilometersApp(BoxLayout):
    km_output = StringProperty("0 km")  # StringProperty for label text

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.miles = 0

    def change_miles(self, change):
        self.miles += change
        self.ids.miles_input.text = str(self.miles)
        self.update_km()

    def update_km(self):
        kilometers = self.miles * 1.60934
        self.km_output = f"{kilometers:.2f} km"  # Update the StringProperty


class MilesToKilometersApp(App):
    def build(self):
        return ConvertMilesToKilometersApp()


if __name__ == '__main__':
    MilesToKilometersApp().run()
