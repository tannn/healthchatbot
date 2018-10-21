## Request refill
* None
    - utter_ask_medicine   <!-- predicted: utter_ask_which_dr -->
* request_refill
    - utter_prescription_refill


## Generated Story 1474650407612037026
* None
    - utter_ask_which_dr
* confirm_dr
    - slot{"dr": "Dr. Marino"}
    - utter_ask_date
* confirm_date
    - slot{"date": "Friday"}
    - utter_confirmed
* None
    - utter_ask_medicine   <!-- predicted: utter_ask_which_dr -->
* request_refill
    - slot{"medicine": "ibuprofen"}
    - utter_prescription_refill
* None
    - utter_ask_message   <!-- predicted: utter_ask_which_dr -->
* message_dr
    - slot{"message": "I am having pain in my bones"}
    - utter_confirmed_message   <!-- predicted: utter_ask_which_dr -->


## Generated Story -633546204153406052
* None
    - utter_greet   <!-- predicted: utter_ask_which_dr -->
* None
    - utter_ask_which_dr
* confirm_dr
    - slot{"dr": "Dr. Howard"}
    - utter_ask_date
* confirm_date
    - slot{"date": "Tuesday"}
    - utter_confirmed
* None
    - utter_ask_message   <!-- predicted: utter_ask_which_dr -->
* note_to_doc
    - slot{"message": "My knee is still swollen and in severe pain can you please chop it off"}
    - utter_confirmed_message
* None
    - utter_reviewLabResults   <!-- predicted: utter_bills -->
* None
    - utter_ask_medicine   <!-- predicted: utter_bills -->
* request_refill
    - slot{"medicine": "Adderrall"}
    - utter_prescription_refill


## Message to Doc
* None
    - utter_ask_which_dr
* confirm_dr
    - utter_ask_message   <!-- predicted: utter_ask_date -->
* message_dr
    - utter_confirmed_message


## Complicated2
* None
    - utter_greet   <!-- predicted: utter_ask_which_dr -->
* confirm_dr
    - utter_ask_message
* message_dr
    - utter_confirmed_message
* None
    - utter_ask_date   <!-- predicted: utter_confirmed_message -->
* confirm_date
    - utter_confirmed
* None
    - utter_reviewLabResults   <!-- predicted: utter_bills -->
* request_refill
    - utter_prescription_refill   <!-- predicted: utter_ask_medicine -->
* None
    - utter_bills   <!-- predicted: utter_ask_which_dr -->


## Get a Prescription refill
* request_refill
    - utter_prescription_refill   <!-- predicted: utter_ask_medicine -->


## new story
* None
    - utter_ask_which_dr
* confirm_dr
    - slot{"dr": "Dr. Marino"}
    - utter_ask_message   <!-- predicted: utter_ask_date -->
* message_dr
    - slot{"message": "I am having a lot of nightmares"}
    - utter_confirmed_message
* None
    - utter_ask_medicine   <!-- predicted: utter_confirmed_message -->
* request_refill
    - slot{"medicine": "Adderall"}
    - utter_prescription_refill


## Message to Doctor2, no message, yes doctor
* None
    - utter_greet   <!-- predicted: utter_ask_which_dr -->
* confirm_dr
    - utter_ask_message
* message_dr
    - utter_confirmed_message


## Create Appointment
* None
    - utter_greet   <!-- predicted: utter_ask_which_dr -->
* confirm_dr
    - utter_confirmed   <!-- predicted: utter_ask_message -->


## Generated Story -6285518583485324959
* greeting
    - utter_greet
* message_dr
    - slot{"message": "I want to message my doctor"}
    - utter_ask_which_dr
* confirm_dr
    - slot{"dr": "Dr. Smith"}
    - utter_ask_message
* message_dr
    - slot{"message": "How can I relief my bone pain?"}
    - utter_confirmed_message
* None
    - utter_ask_medicine   <!-- predicted: utter_confirmed_message -->
* prescription_complaint
    - slot{"medicine": "acetaminophen"}
    - utter_prescription_refill


## Complicated
* confirm_dr
    - utter_confirmed   <!-- predicted: utter_ask_message -->
* request_refill
    - utter_prescription_refill   <!-- predicted: utter_ask_medicine -->
* confirm_dr
    - utter_ask_message
* message_dr
    - utter_confirmed_message
* None
    - utter_reviewLabResults   <!-- predicted: utter_confirmed_message -->
* None
    - utter_bills   <!-- predicted: utter_ask_which_dr -->


## Generated Story -2477838826319677261
* None
    - utter_bills   <!-- predicted: utter_ask_which_dr -->
* confirm_dr
    - slot{"date": "Saturday"}
    - slot{"dr": "Dr. Squarepants"}
    - utter_confirmed   <!-- predicted: utter_ask_message -->
* None
    - utter_ask_message   <!-- predicted: utter_confirmed_message -->
* message_dr
    - slot{"message": "My eye popped out!"}
    - utter_confirmed_message   <!-- predicted: utter_ask_which_dr -->
* None
    - utter_ask_medicine   <!-- predicted: utter_confirmed_message -->
* request_refill
    - slot{"medicine": "NyQuil"}
    - utter_prescription_refill


## Generated Story -3749622341900304991
* None
    - utter_greet   <!-- predicted: utter_ask_which_dr -->
* None
    - utter_ask_medicine   <!-- predicted: utter_ask_which_dr -->
* request_refill
    - slot{"medicine": "aspirin"}
    - utter_prescription_refill


## Note to Doctor
* None
    - utter_ask_which_dr
* confirm_dr
    - slot{"dr": "Dr. Norris"}
    - utter_ask_message   <!-- predicted: utter_ask_date -->
* message_dr
    - slot{"message": "I want my scar to not be that visible"}
    - utter_confirmed_message


## Review lab results
* None
    - utter_reviewLabResults   <!-- predicted: utter_ask_which_dr -->


## Generated Story -3251722074745246924
* request_refill
    - slot{"medicine": "Galzin"}
    - utter_prescription_refill   <!-- predicted: utter_ask_medicine -->


## Billing
* None
    - utter_bills   <!-- predicted: utter_ask_which_dr -->


## Complicated1
* None
    - utter_bills   <!-- predicted: utter_ask_which_dr -->
* None
    - utter_ask_which_dr   <!-- predicted: utter_bills -->
* confirm_dr
    - utter_ask_date
* confirm_date
    - utter_confirmed
* None
    - utter_bills
* None
    - utter_ask_message   <!-- predicted: utter_bills -->
* message_dr
    - utter_confirmed_message   <!-- predicted: utter_ask_which_dr -->
* None
    - utter_ask_medicine   <!-- predicted: utter_confirmed_message -->
* request_refill
    - utter_prescription_refill
* None
    - utter_reviewLabResults   <!-- predicted: utter_ask_which_dr -->


