## Generated Story 1474650407612037026
* create_apt
    - utter_ask_which_dr
* confirm_dr{"dr": "Dr. Marino"}
    - slot{"dr": "Dr. Marino"}
    - utter_ask_date
* confirm_date{"date": "Friday"}
    - slot{"date": "Friday"}
    - utter_confirmed
* request_refill
    - utter_ask_medicine
* medicineName{"medicine": "ibuprofen"}
    - slot{"medicine": "ibuprofen"}
    - utter_ask_message
* message_dr
    - utter_ask_message
* note_to_doc{"message": "I am having pain in my bones"}
    - slot{"message": "I am having pain in my bones"}
    - utter_confirmed_message

