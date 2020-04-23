# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction

from covidapi import Covidapi
from rasa_sdk.events import SlotSet, UserUtteranceReverted

# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction

from covidapi import Covidapi
from rasa_sdk.events import SlotSet, UserUtteranceReverted


#
#
from mailtosend import sendemail

from covidapi import world_info

from covidapi import indiastate


class ActionCustomFallback(Action):

    def name(self) -> Text:
        return "action_custom_fallback"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_template("utter_custom", tracker)

        return [UserUtteranceReverted()]




class ActionFormInfo(FormAction):
    def name(self) -> Text:
        """Unique identifier of the form"""

        return "form_info"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["NAME",  "EMAIL", "NUMBER", "ZIP"]
        # return ["NAME", "EMAIL"]

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        # utter submit template
        dispatcher.utter_message(template="utter_submit",
                                 name=tracker.get_slot('NAME'),
                                 number=tracker.get_slot('NUMBER'),
                                 email=tracker.get_slot('EMAIL'),
                                 zip=tracker.get_slot('ZIP'))
        return []

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "name": [self.from_entity(entity="NAME", intent='my_name_is')],
            "number": [self.from_entity(entity="NUMBER", intent='mobile_number')],
            "email": [self.from_entity(entity="EMAIL", intent='email_addr')],
            "zip": [self.from_entity(entity="ZIP", intent='pin')],
        }

    @staticmethods
    def is_int(string: Text) -> bool:
        """Check if a string is an integer"""

        try:
            int(string)
            return True
        except ValueError:
            return False

    def validate_NUMBER(
            self,
            value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate number value."""

        if self.is_int(value) and int(value) > 0:
            return {"NUM": value}
        else:
            dispatcher.utter_message(template="utter_wrong_NUMBER")
            # validation failed, set slot to None
            return {"NUM": None}


    def validate_ZIP(
            self,
            value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate zip value."""

        if self.is_int(value) and int(value) > 0:
            return {"ZIP": value}
        else:
            dispatcher.utter_message(template="utter_wrong_ZIP")
            # validation failed, set slot to None
            return {"ZIP": None}




class ActionCovidCountry(Action):

    def name(self) -> Text:
        return "action_covid_country"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        country = tracker.get_slot('location')
        response = Covidapi(country)

        dispatcher.utter_message(response)
        return [SlotSet('location', country)]

class ActionCovidWorld(Action):

    def name(self) -> Text:
        return "action_covid_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        universe = tracker.get_slot('world')
        respo = world_info()

        dispatcher.utter_message(respo)
        return [SlotSet('world', universe)]


class ActionSendEmail(Action):

    def name(self) -> Text:
        return "action_send_email"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        to_email = tracker.get_slot('EMAIL')
        response = sendemail(to_email)

        dispatcher.utter_message(response)
        return [SlotSet('EMAIL', to_email)]


class ActionCovidIndia(Action):

    def name(self) -> Text:
        return "action_covid_state"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        statess = tracker.get_slot('states')
        respo = indiastate(statess)

        dispatcher.utter_message(respo)
        return [SlotSet('states', statess)]
from mailtosend import sendemail

from covidapi import world_info

from covidapi import indiastate


class ActionCustomFallback(Action):

    def name(self) -> Text:
        return "action_custom_fallback"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_template("utter_custom", tracker)

        return [UserUtteranceReverted()]




class ActionFormInfo(FormAction):
    def name(self) -> Text:
        """Unique identifier of the form"""

        return "form_info"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        # return ["NAME",  "EMAIL", "NUMBER", "ZIP"]
        return ["NAME", "EMAIL"]

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        # utter submit template
        dispatcher.utter_message(template="utter_submit",
                                 name=tracker.get_slot('NAME'),
                                 # number=tracker.get_slot('NUMBER'),
                                 email=tracker.get_slot('EMAIL'))
                                 # zip=tracker.get_slot('ZIP'))
        return []

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "name": [self.from_entity(entity="NAME", intent='my_name_is')],
            # "number": [self.from_entity(entity="NUMBER", intent='mobile_number')],
            "email": [self.from_entity(entity="EMAIL", intent='email_addr')],
            # "zip": [self.from_entity(entity="ZIP", intent='pin')],
        }

    @staticmethod
    def is_int(string: Text) -> bool:
        """Check if a string is an integer"""

        try:
            int(string)
            return True
        except ValueError:
            return False

    def validate_NUMBER(
            self,
            value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate number value."""

        if self.is_int(value) and int(value) > 0:
            return {"NUM": value}
        else:
            dispatcher.utter_message(template="utter_wrong_NUMBER")
            # validation failed, set slot to None
            return {"NUM": None}


    def validate_ZIP(
            self,
            value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate zip value."""

        if self.is_int(value) and int(value) > 0:
            return {"ZIP": value}
        else:
            dispatcher.utter_message(template="utter_wrong_ZIP")
            # validation failed, set slot to None
            return {"ZIP": None}




class ActionCovidCountry(Action):

    def name(self) -> Text:
        return "action_covid_country"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        country = tracker.get_slot('location')
        response = Covidapi(country)

        dispatcher.utter_message(response)
        return [SlotSet('location', country)]

class ActionCovidWorld(Action):

    def name(self) -> Text:
        return "action_covid_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        universe = tracker.get_slot('world')
        respo = world_info()

        dispatcher.utter_message(respo)
        return [SlotSet('world', universe)]


class ActionSendEmail(Action):

    def name(self) -> Text:
        return "action_send_email"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        to_email = tracker.get_slot('EMAIL')
        response = sendemail(to_email)

        dispatcher.utter_message(response)
        return [SlotSet('EMAIL', to_email)]


class ActionCovidIndia(Action):

    def name(self) -> Text:
        return "action_covid_state"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        statess = tracker.get_slot('states')
        respo = indiastate(statess)

        dispatcher.utter_message(respo)
        return [SlotSet('states', statess)]