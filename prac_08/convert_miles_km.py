from kivy.app import App
from kivy.lang import Builder

MILES_TO_KM = 1.60934

class MilesConverterApp(App):
    """MilesConverterApp is a Kivy App that converts miles to kilometers."""
    def build(self):
        """Build app using and loading the kv file."""
        self.title = "Convert Miles to KM"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def calculate_output(self):
        """Calculates the output to label widget."""
        value = self.valid_miles()
        result = value * MILES_TO_KM
        self.root.ids.output_label.text = str(round(result, 3))

    def increment_value(self, change):
        """Handle the up/down button pressing."""
        value = self.valid_miles() + change
        self.root.ids.input_miles.text = str(value)  # Update TextInput
        self.calculate_output()  # Recalculate the result

    def valid_miles(self):
        """Get text input and convert to float."""
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0

MilesConverterApp().run()
