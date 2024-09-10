from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionSayPhone(Action):

    def name(self) -> Text:
        return "action_say_phone_number"
    
    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        phone_number = tracker.get_slot("phone_number")
        
        if not phone_number:
            dispatcher.utter_message(text= "Sorry, I don't have your phone number")
        else:
            dispatcher.utter_message(text=f"Your phone number is {phone_number}")
        
        return[]

