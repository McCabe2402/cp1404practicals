from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Update the label with a greeting message."""
        name = self.root.ids.input_name.text  # Get the text from the TextInput
        self.root.ids.output_label.text = f"Hello, {name}!"  # Update the label with the name

    def handle_clear(self):
        """Reset the TextInput and Label to blank."""
        self.root.ids.input_name.text = ''  # Clear the text input field
        self.root.ids.output_label.text = ''  # Clear the label


BoxLayoutDemo().run()
