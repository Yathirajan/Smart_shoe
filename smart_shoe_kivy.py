from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
import requests

class SmartShoeUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)

        self.weight_label = Label(text="Weight: -- kg", font_size=20)
        self.location_label = Label(text="Location: --", font_size=16)

        self.add_widget(self.weight_label)
        self.add_widget(self.location_label)

        self.fetch_weight_btn = Button(text="Fetch Weight", size_hint=(1, 0.2))
        self.fetch_weight_btn.bind(on_press=self.fetch_weight)
        self.add_widget(self.fetch_weight_btn)

        self.fetch_location_btn = Button(text="Fetch Location", size_hint=(1, 0.2))
        self.fetch_location_btn.bind(on_press=self.fetch_location)
        self.add_widget(self.fetch_location_btn)

        self.alert_btn = Button(text="Send Emergency Alert", size_hint=(1, 0.2), background_color=(1, 0, 0, 1))
        self.alert_btn.bind(on_press=self.send_alert)
        self.add_widget(self.alert_btn)

    def fetch_weight(self, instance):
        try:
            response = requests.get("http://localhost:5000/weight")
            weight = response.json().get("weight", "N/A")
            self.weight_label.text = f"Weight: {weight} kg"
        except Exception as e:
            self.weight_label.text = "Error fetching weight"

    def fetch_location(self, instance):
        try:
            response = requests.get("http://localhost:5000/location")
            location = response.json().get("location", "N/A")
            self.location_label.text = f"Location: {location}"
        except Exception as e:
            self.location_label.text = "Error fetching location"

    def send_alert(self, instance):
        try:
            response = requests.post("http://localhost:5000/alert")
            status = response.json().get("status", "Failed")
            self.alert_btn.text = status
        except Exception as e:
            self.alert_btn.text = "Error sending alert"

class SmartShoeApp(App):
    def build(self):
        return SmartShoeUI()

if __name__ == "__main__":
    SmartShoeApp().run()
