## Message to Doc
* None{"medicine": "message_dr"}
    - slot{"medicine": "message_dr"}
    - utter_ask_which_dr   <!-- predicted: utter_prescription_refill -->
* confirm_dr
    - utter_ask_message
* medicineName
    - utter_confirmed_message


## Note to Doctor
* None{"medicine": "message_dr"}
    - slot{"medicine": "message_dr"}
    - utter_ask_which_dr   <!-- predicted: utter_prescription_refill -->
* confirm_dr
    - slot{"dr": "Dr. Norris"}
    - utter_ask_message
* message_dr
    - slot{"message": "I want my scar to not be that visible"}
    - utter_confirmed_message


## Generated Story -3749622341900304991
* None
    - utter_greet   <!-- predicted: utter_ask_which_dr -->
* None
    - utter_ask_medicine   <!-- predicted: utter_ask_which_dr -->
* prescription_complaint
    - slot{"medicine": "aspirin"}
    - utter_prescription_refill


## Message to Doctor, yes message, and doc
* confirm_dr
    - utter_ask_message   <!-- predicted: utter_ask_which_dr -->
* note_to_doc
    - utter_confirmed_message


## new story
* None{"medicine": "message_dr"}
    - slot{"medicine": "message_dr"}
    - utter_ask_which_dr   <!-- predicted: utter_prescription_refill -->
* confirm_dr{"dr": "\"Dr Marino\"}"}
    - slot{"dr": "\"Dr Marino\"}"}
    - slot{"dr": "Dr. Marino"}
    - utter_ask_message
* note_to_doc
    - slot{"message": "I am having a lot of nightmares"}
    - utter_confirmed_message
* None
    - utter_ask_medicine   <!-- predicted: utter_greet -->
* prescription_complaint
    - slot{"medicine": "Adderrall"}
    - utter_prescription_refill   <!-- predicted: utter_greet -->


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
    - utter_ask_medicine   <!-- predicted: utter_ask_message -->
* prescription_complaint
    - slot{"medicine": "acetaminophen"}
    - utter_prescription_refill   <!-- predicted: utter_greet -->


## Create Appointment
* None
    - utter_greet   <!-- predicted: utter_ask_which_dr -->
* confirm_dr
    - utter_confirmed   <!-- predicted: utter_ask_which_dr -->


## Creating Appointment
* None{"medicine": "create_apt"}
    - slot{"medicine": "create_apt"}
    - utter_ask_which_dr   <!-- predicted: utter_prescription_refill -->
* confirm_dr
    - utter_ask_date   <!-- predicted: utter_ask_message -->
* confirm_date{"medicine": "confirm_date{\"date\":\"Thursday\"}"}
    - slot{"medicine": "confirm_date{\"date\":\"Thursday\"}"}
    - utter_confirmed   <!-- predicted: utter_prescription_refill -->


## Billing
* None
    - utter_greet   <!-- predicted: utter_ask_which_dr -->
* None{"medicine": "viewBills"}
    - slot{"medicine": "viewBills"}
    - utter_bills   <!-- predicted: utter_prescription_refill -->


## Review lab results
* None
    - utter_reviewLabResults   <!-- predicted: utter_ask_which_dr -->


## Generated Story -633546204153406052
* None
    - utter_greet   <!-- predicted: utter_ask_which_dr -->
* None{"medicine": "create_apt"}
    - slot{"medicine": "create_apt"}
    - utter_ask_which_dr   <!-- predicted: utter_prescription_refill -->
* confirm_dr
    - slot{"dr": "Dr. Howard"}
    - utter_ask_date   <!-- predicted: utter_ask_message -->
* confirm_date
    - slot{"date": "Tuesday"}
    - utter_confirmed
* None{"medicine": "message_dr"}
    - slot{"medicine": "message_dr"}
    - utter_ask_message   <!-- predicted: utter_prescription_refill -->
* note_to_doc
    - slot{"message": "My knee is still swollen and in severe pain can you please chop it off"}
    - utter_confirmed_message
* None
    - utter_reviewLabResults   <!-- predicted: utter_greet -->
* None
    - utter_ask_medicine   <!-- predicted: utter_ask_which_dr -->
* prescription_complaint
    - slot{"medicine": "Adderrall"}
    - utter_prescription_refill   <!-- predicted: utter_greet -->


## Complicated
* confirm_dr
    - utter_confirmed   <!-- predicted: utter_ask_which_dr -->
* prescription_complaint{"medicine": "request_refill{\"medicine\":\"Benadryl\"}"}
    - slot{"medicine": "request_refill{\"medicine\":\"Benadryl\"}"}
    - utter_prescription_refill
* confirm_dr
    - utter_ask_message
* note_to_doc
    - utter_confirmed_message
* None
    - utter_reviewLabResults   <!-- predicted: utter_greet -->


## Request refill
* None
    - utter_ask_medicine   <!-- predicted: utter_ask_which_dr -->
* prescription_complaint{"medicine": "medicineName{\"medicine\":\"vicodin\"}"}
    - slot{"medicine": "medicineName{\"medicine\":\"vicodin\"}"}
    - utter_prescription_refill


## Message to Doctor2, no message, yes doctor
* None
    - utter_greet   <!-- predicted: utter_ask_which_dr -->
* confirm_dr
    - utter_ask_message   <!-- predicted: utter_ask_which_dr -->
* note_to_doc
    - utter_confirmed_message


## Complicated2
* None
    - utter_greet   <!-- predicted: utter_ask_which_dr -->
* confirm_dr
    - utter_ask_message   <!-- predicted: utter_ask_which_dr -->
* note_to_doc
    - utter_confirmed_message
* None{"medicine": "create_apt"}
    - slot{"medicine": "create_apt"}
    - utter_ask_date   <!-- predicted: utter_prescription_refill -->
* confirm_date{"medicine": "confirm_date{\"date\":\"Tuesday\"}"}
    - slot{"medicine": "confirm_date{\"date\":\"Tuesday\"}"}
    - utter_confirmed   <!-- predicted: utter_prescription_refill -->
* None
    - utter_reviewLabResults   <!-- predicted: utter_greet -->
* prescription_complaint{"medicine": "request_refill{\"medicine\":\"Mirena\"}"}
    - slot{"medicine": "request_refill{\"medicine\":\"Mirena\"}"}
    - utter_prescription_refill


## Complicated1
* None{"medicine": "create_apt"}
    - slot{"medicine": "create_apt"}
    - utter_ask_which_dr   <!-- predicted: utter_prescription_refill -->
* confirm_dr
    - utter_ask_date   <!-- predicted: utter_ask_message -->
* confirm_date
    - utter_confirmed
* None{"medicine": "message_dr"}
    - slot{"medicine": "message_dr"}
    - utter_ask_message   <!-- predicted: utter_prescription_refill -->
* note_to_doc
    - utter_confirmed_message
* None
    - utter_ask_medicine   <!-- predicted: utter_greet -->
* prescription_complaint{"medicine": "medicineName{\"medicine\":\"Benzonatate\"}"}
    - slot{"medicine": "medicineName{\"medicine\":\"Benzonatate\"}"}
    - utter_prescription_refill
* None
    - utter_reviewLabResults   <!-- predicted: utter_ask_which_dr -->


## Generated Story 1474650407612037026
* None{"medicine": "create_apt"}
    - slot{"medicine": "create_apt"}
    - utter_ask_which_dr   <!-- predicted: utter_prescription_refill -->
* confirm_dr{"dr": "\"Dr Marino\"}"}
    - slot{"dr": "\"Dr Marino\"}"}
    - slot{"dr": "Dr. Marino"}
    - utter_ask_date   <!-- predicted: utter_ask_message -->
* medicineName
    - slot{"date": "Friday"}
    - utter_confirmed
* None
    - utter_ask_medicine   <!-- predicted: utter_greet -->
* prescription_complaint
    - slot{"medicine": "ibuprofen"}
    - utter_prescription_refill   <!-- predicted: utter_greet -->
* None{"medicine": "message_dr"}
    - slot{"medicine": "message_dr"}
    - utter_ask_message   <!-- predicted: utter_prescription_refill -->
* note_to_doc
    - slot{"message": "I am having pain in my bones"}
    - utter_confirmed_message


