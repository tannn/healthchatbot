
## Create Appointment
* greeting
	- utter_greet
* create_apt{"dr":"Dr. Scott", "date":"Monday"}
	- utter_confirmed

## Creating Appointment
* create_apt
	- utter_ask_which_dr
* confirm_dr{"dr":"Dr. Adams"}
	- utter_ask_date
* confirm_date{"date":"Thursday"}
	- utter_confirmed

## Message to Doc
* message_dr
	- utter_ask_which_dr
* confirm_dr{"dr":"Dr. Smith"}
	- utter_ask_message
* note_to_doc{"message":"I keep throwing up"}
	- utter_confirmed_message

## Message to Doctor, yes message, and doc
* message_dr{"dr":"dr jordan"}
	- utter_ask_message
* note_to_doc{"message":"I am having secondary emotional effects"}
	- utter_confirmed_message

## Message to Doctor2, no message, yes doctor
* greeting
	- utter_greet
* message_dr{"dr":"Dr Young"}
	- utter_ask_message
* note_to_doc{"message":"My knee still hurts"}
	- utter_confirmed_message

## Get a Prescription refill
* request_refill{"medicine":"Ibuprofen"}
	- utter_prescription_refill

## Review lab results
* review_labResults
	- utter_reviewLabResults

## Complicated
* create_apt{"dr":"Dr. Pike", "date":"Friday"}
	- utter_confirmed
* request_refill{"medicine":"Benadryl"}
	- utter_prescription_refill
* message_dr{"dr":"Dr. Mario"}
	- utter_ask_message
* note_to_doc{"message":"I am having diarrhea"}
	- utter_confirmed_message
* review_labResults
	- utter_reviewLabResults
* viewBills
  	-	utter_bills

## Request refill
* request_refill
	- utter_ask_medicine
* medicineName{"medicine":"vicodin"}
	- utter_prescription_refill

## Complicated1
* viewBills
    - utter_bills
* create_apt
	- utter_ask_which_dr
* confirm_dr{"dr":"Doctor Blue"}
	- utter_ask_date
* confirm_date {"date":"Wednesday"}
	- utter_confirmed
* viewBills
  	-	utter_bills
* message_dr
	- utter_ask_message
* note_to_doc{"message":"My knee still hurts"}
	- utter_confirmed_message
* request_refill
	- utter_ask_medicine
* medicineName{"medicine":"Benzonatate"}
	- utter_prescription_refill
* review_labResults
	- utter_reviewLabResults

## Complicated2
* greeting
	- utter_greet
* message_dr{"dr":"Dr. Adams"}
	- utter_ask_message
* note_to_doc{"message":"My knee still hurts"}
	- utter_confirmed_message
* create_apt
	- utter_ask_date
* confirm_date{"date":"Tuesday"}
	- utter_confirmed
* review_labResults
	- utter_reviewLabResults
* request_refill{"medicine":"Mirena"}
	- utter_prescription_refill
* viewBills
  	-	utter_bills

## Generated Story -633546204153406052
* greeting
    - utter_greet
* create_apt
    - utter_ask_which_dr
* confirm_dr{"dr": "Dr. Howard"}
    - slot{"dr": "Dr. Howard"}
    - utter_ask_date
* confirm_date{"date": "Tuesday"}
    - slot{"date": "Tuesday"}
    - utter_confirmed
* message_dr
    - utter_ask_message
* note_to_doc{"message": "My knee is still swollen and in severe pain can you please chop it off"}
    - slot{"message": "My knee is still swollen and in severe pain can you please chop it off"}
    - utter_confirmed_message
* review_labResults
    - utter_reviewLabResults
* request_refill
    - utter_ask_medicine
* medicineName{"medicine": "Adderall"}
    - slot{"medicine": "Adderrall"}
    - utter_prescription_refill

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
    - utter_prescription_refill
* message_dr
    - utter_ask_message
* note_to_doc{"message": "I am having pain in my bones"}
    - slot{"message": "I am having pain in my bones"}
    - utter_confirmed_message

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

## Generated Story -3749622341900304991
* greeting
    - utter_greet
* request_refill
    - utter_ask_medicine
* medicineName{"medicine": "aspirin"}
    - slot{"medicine": "aspirin"}
    - utter_prescription_refill

## Generated Story -2477838826319677261
* viewBills
    - utter_bills
* create_apt{"dr": "Dr. Squarepants", "date": "Saturday"}
    - slot{"date": "Saturday"}
    - slot{"dr": "Dr. Squarepants"}
    - utter_confirmed
* message_dr
    - utter_ask_message
* note_to_doc{"message": "My eye popped out!"}
    - slot{"message": "My eye popped out!"}
    - utter_confirmed_message
* request_refill
    - utter_ask_medicine
* medicineName{"medicine": "NyQuil"}
    - slot{"medicine": "NyQuil"}
    - utter_prescription_refill

## Generated Story -3251722074745246924
* request_refill{"medicine": "Galzin"}
    - slot{"medicine": "Galzin"}
    - utter_prescription_refill

## new story
* message_dr
    - utter_ask_which_dr
* confirm_dr{"dr": "Dr. Marino"}
    - slot{"dr": "Dr. Marino"}
    - utter_ask_message
* note_to_doc{"message": "I am having a lot of nightmares"}
    - slot{"message": "I am having a lot of nightmares"}
    - utter_confirmed_message
* request_refill
    - utter_ask_medicine
* medicineName{"medicine": "Adderall"}
    - slot{"medicine": "Adderall"}
    - utter_prescription_refill

## Note to Doctor
* message_dr
    - utter_ask_which_dr
* confirm_dr{"dr": "Dr. Norris"}
    - slot{"dr": "Dr. Norris"}
    - utter_ask_message
* note_to_doc{"message": "I want my scar to not be that visible"}
    - slot{"message": "I want my scar to not be that visible"}
    - utter_confirmed_message

## Billing
* viewBills
  	-	utter_bills
