# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
import time
import webbrowser
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_tell_discounts"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        test_carousel = {
        "type": "template",
        "payload": {
            "template_type": "generic",
            "elements": [
                {
                "title": "Adidas 2A - JackShoes",
                "subtitle": "Adidas black beast.",
                "image_url": "https://rukminim1.flixcart.com/image/714/857/kh9gbrk0-0/shoe/d/t/o/kzi38-7-adidas-black-original-imafxbjfzkzxqxtx.jpeg?q=50",
                "buttons": [
                    {
                    "title": "Purchase on website 🌐",
                    "url": "https://adidas.com",
                    "type": "web_url"
                    },
                    {
                        "title": "I want this! 😁",
                        "type": "postback",
                        "payload": "/greet"
                    },
                    {
                        "title": "Features? 🤔",
                        "type": "postback",
                        "payload": "/greet"
                    },
                ]
            },
                {
                    "title": "Nike Dope Z-Series",
                    "subtitle": "The style of life",
                    "image_url": "https://4.imimg.com/data4/LD/AL/MY-13802834/nike-air-max-2017-mens-black-orange-imported-sport-shoes-500x500.jpg",
                    "buttons": [
                    {
                    "title": "Purchase on website 🌐",
                    "url": "https://nike.com",
                    "type": "web_url"
                    },
                    {
                        "title": "I want this! 😁",
                        "type": "postback",
                        "payload": "/greet"
                    },
                    {
                        "title": "Features? 🤔",
                        "type": "postback",
                        "payload": "/greet"
                    },
                    ]
                },
                {
                    "title": "Jack Ticon",
                    "subtitle": "NOthing better!",
                    "image_url": "https://media.istockphoto.com/photos/running-shoes-picture-id1249496770?b=1&k=20&m=1249496770&s=170667a&w=0&h=_SUv4odBqZIzcXvdK9rqhPBIenbyBspPFiQOSDRi-RI=",
                    "buttons": [
                        {
                    "title": "Purchase on website 🌐",
                    "url": "https://adidas.com",
                    "type": "web_url"
                    },
                    {
                        "title": "I want this! 😁",
                        "type": "postback",
                        "payload": "/greet"
                    },
                    {
                        "title": "Features? 🤔",
                        "type": "postback",
                        "payload": "/greet"
                    },
                    ]
                },
            ]
          }
        }

        dispatcher.utter_message(text="You caught it 👀. ", attachment=test_carousel)

        return []

class ActionSavageSeries(Action):

    def name(self) -> Text:
        return "action_savage_series"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="The Savage series is here 😎. Only few pieces are left so let's fly fast 🚀...")
        time.sleep(3)
        webbrowser.open('https://www.nike.com/in/t/air-zoom-alphafly-next-road-racing-shoes-13jzhr/CI9925-300')
        
        return []