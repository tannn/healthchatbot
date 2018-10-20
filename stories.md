
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

## Message to Doctor, yes message, and doc
* message_dr{"dr":"Dr. Marino"}
	- utter_ask_message
* note_to_doc{"message":"I am having secondary emotional effects"}
	- utter_confirmed_message

## Message to Doctor2, no message, yes doctor
* greeting
	- utter_greet
* message_dr{"dr":"Dr. Young"}
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

## Complicated1
* create_apt
	- utter_ask_which_dr
* confirm_dr{"dr":"Dr. Blue"}
	- utter_ask_date
* confirm_date {"date":"Wednesday"}
	- utter_confirmed
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
	- utter_confirmed
* create_apt
	- utter_ask_date
* confirm_date{"date":"Tuesday"}
	- utter_confirmed
* review_labResults
	- utter_reviewLabResults
* request_refill{"medicine":"Mirena"}
	- utter_prescription_refill


