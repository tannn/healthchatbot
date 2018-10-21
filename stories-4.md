## Generated Story -6285518583485324959
* greeting{"greeting": "hi"}
    - utter_greet
* message_dr{"message": "I want to message my doctor"}
    - slot{"message": "I want to message my doctor"}
    - utter_ask_which_dr
* confirm_dr{"dr": "Dr. Smith"}
    - slot{"dr": "Dr. Smith"}
    - utter_ask_message
* note_to_doc{"message": "How can I relief my bone pain?"}
    - slot{"message": "How can I relief my bone pain?"}
    - utter_confirmed_message
* request_refill
    - utter_ask_medicine
* medicineName{"medicine": "acetaminophen"}
    - slot{"medicine": "acetaminophen"}
    - utter_prescription_refill

