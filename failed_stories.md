## Complicated2
* None
    - utter_greet   <!-- predicted: utter_ask_which_dr -->
* confirm_dr
    - utter_ask_message
* note_to_doc
    - utter_confirmed_message
* None
    - utter_ask_date   <!-- predicted: utter_ask_which_dr -->
* confirm_date
    - utter_confirmed
* None
    - utter_reviewLabResults   <!-- predicted: utter_ask_message -->
* prescription_complaint
    - utter_prescription_refill   <!-- predicted: utter_ask_which_dr -->


## Message to Doctor, yes message, and doc
* confirm_dr
    - utter_ask_message   <!-- predicted: utter_ask_date -->
* prescription_complaint
    - utter_confirmed_message


## Complicated1
* None
    - utter_ask_which_dr
* confirm_dr
    - utter_ask_date
* confirm_date
    - utter_confirmed
* None
    - utter_ask_message
* note_to_doc
    - utter_confirmed_message
* None
    - utter_ask_medicine   <!-- predicted: utter_ask_which_dr -->
* prescription_complaint
    - utter_prescription_refill   <!-- predicted: utter_ask_which_dr -->
* None
    - utter_reviewLabResults   <!-- predicted: utter_ask_which_dr -->


## Generated Story -633546204153406052
* None
    - utter_greet   <!-- predicted: utter_ask_which_dr -->
* None
    - utter_ask_which_dr
* confirm_dr{"dr": "\"Dr Howard\"}"}
    - slot{"dr": "\"Dr Howard\"}"}
    - slot{"dr": "Dr. Howard"}
    - utter_ask_date   <!-- predicted: utter_ask_message -->
* confirm_date
    - slot{"date": "Tuesday"}
    - utter_confirmed
* None
    - utter_ask_message
* note_to_doc
    - slot{"message": "My knee is still swollen and in severe pain can you please chop it off"}
    - utter_confirmed_message
* None
    - utter_reviewLabResults   <!-- predicted: utter_ask_which_dr -->
* None
    - utter_ask_medicine   <!-- predicted: utter_ask_which_dr -->
* prescription_complaint
    - slot{"medicine": "Adderrall"}
    - utter_prescription_refill


## Review lab results
* None
    - utter_reviewLabResults   <!-- predicted: utter_ask_which_dr -->


## Generated Story -6285518583485324959
* None
    - utter_greet   <!-- predicted: utter_ask_which_dr -->
* message_dr
    - slot{"message": "I want to message my doctor"}
    - utter_ask_which_dr
* confirm_dr{"dr": "\"Dr Smith\"}"}
    - slot{"dr": "\"Dr Smith\"}"}
    - slot{"dr": "Dr. Smith"}
    - utter_ask_message
* message_dr
    - slot{"message": "How can I relief my bone pain?"}
    - utter_confirmed_message
* None
    - utter_ask_medicine   <!-- predicted: utter_ask_message -->
* prescription_complaint
    - slot{"medicine": "acetaminophen"}
    - utter_prescription_refill


## Get a Prescription refill
* prescription_complaint
    - utter_prescription_refill   <!-- predicted: utter_ask_which_dr -->


## Generated Story -3749622341900304991
* None
    - utter_greet   <!-- predicted: utter_ask_which_dr -->
* None
    - utter_ask_medicine   <!-- predicted: utter_ask_which_dr -->
* prescription_complaint
    - slot{"medicine": "aspirin"}
    - utter_prescription_refill


## Generated Story 1474650407612037026
* None
    - utter_ask_which_dr
* confirm_dr{"dr": "\"Dr Marino\"}"}
    - slot{"dr": "\"Dr Marino\"}"}
    - slot{"dr": "Dr. Marino"}
    - utter_ask_date   <!-- predicted: utter_ask_message -->
* confirm_date
    - slot{"date": "Friday"}
    - utter_confirmed
* None
    - utter_ask_medicine   <!-- predicted: utter_ask_message -->
* prescription_complaint
    - slot{"medicine": "ibuprofen"}
    - utter_prescription_refill
* None
    - utter_ask_message   <!-- predicted: utter_ask_which_dr -->
* prescription_complaint
    - slot{"message": "I am having pain in my bones"}
    - utter_confirmed_message


## Billing
* None
    - utter_greet   <!-- predicted: utter_ask_which_dr -->
* None
    - utter_bills   <!-- predicted: utter_ask_which_dr -->


## Request refill
* None
    - utter_ask_medicine   <!-- predicted: utter_ask_which_dr -->
* prescription_complaint
    - utter_prescription_refill   <!-- predicted: utter_ask_which_dr -->


## Message to Doc
* None
    - utter_ask_which_dr
* confirm_dr
    - utter_ask_message   <!-- predicted: utter_ask_date -->
* message_dr
    - utter_confirmed_message


## new story
* None
    - utter_ask_which_dr
* confirm_dr{"dr": "\"Dr Marino\"}"}
    - slot{"dr": "\"Dr Marino\"}"}
    - slot{"dr": "Dr. Marino"}
    - utter_ask_message
* note_to_doc
    - slot{"message": "I am having a lot of nightmares"}
    - utter_confirmed_message
* None
    - utter_ask_medicine   <!-- predicted: utter_ask_which_dr -->
* prescription_complaint
    - slot{"medicine": "Adderrall"}
    - utter_prescription_refill


## Message to Doctor2, no message, yes doctor
* None
    - utter_greet   <!-- predicted: utter_ask_which_dr -->
* confirm_dr
    - utter_ask_message
* note_to_doc
    - utter_confirmed_message


## Create Appointment
* None
    - utter_greet   <!-- predicted: utter_ask_which_dr -->
* confirm_dr
    - utter_confirmed   <!-- predicted: utter_ask_message -->


## Complicated
* confirm_dr
    - utter_confirmed   <!-- predicted: utter_ask_date -->
* prescription_complaint
    - utter_prescription_refill   <!-- predicted: utter_ask_date -->
* confirm_dr
    - utter_ask_message   <!-- predicted: utter_ask_date -->
* prescription_complaint
    - utter_confirmed_message
* None
    - utter_reviewLabResults   <!-- predicted: utter_ask_which_dr -->


