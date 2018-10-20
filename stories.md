
## Create Appointment
* greeting
	- greet
* create_apt{"dr":"Dr. Scott", "date":"Monday"}
	- confirmed

## Creating Appointment
* create_apt
	- ask_which_dr
* confirm_dr{"dr":"Dr. Adams"}
	- ask_date
* confirm_date{"date":"Thursday"}
	- confirmed

## Message to Doctor, yes message, and doc
* message_dr{"dr":"Dr. Marino"}
	- ask_message
* note_to_doc{"message":"I am having secondary emotional effects"}
	- confirmed_message

## Message to Doctor2, no message, yes doctor
* greeting
	- greet
* message_dr{"dr":"Dr. Young"}
	- ask_message
* note_to_doc{"message":"My knee still hurts"}
	- confirmed_message

## Get a Prescription refill
* request_refill{"medicine":"Ibuprofen"}
	- utter_prescription_refill

## Review lab results
* review_labResults
	- utter_reviewLabResults

## Complicated
* create_apt{"dr":"Dr. Pike", "date":"Friday"}
	- confirmed
* request_refill{"medicine":"Benadryl"}
	- utter_prescription_refill
* message_dr{"dr":"Dr. Mario"}
	- ask_message
* note_to_doc{"message":"I am having diarrhea}
	- confirmed_message
* review_labResults
	- utter_reviewLabResults

## Complicated1
* create_apt
	- ask_which_dr
* confirm_dr{"dr":"Dr. Blue"}
	- ask_date
* confirm_date {"date":"Wednesday"}
	- confirmed
* message_dr
	- ask_message
* note_to_doc{"message":"My knee still hurts"}
	- confirmed_message
* request_refill
	- utter_ask_medicine
* medicineName{"medicine":"Benzonatate"}
	- utter_prescription_refill
* review_labResults
	- utter_reviewLabResults

## Complicated2
* greeting
	- greet
* message_dr{"dr":"Dr. Adams"}
	- ask_message
* note_to_doc{"message":"My knee still hurts"}
	- confirmed
* create_apt
	- ask_date
* confirm_date{"date":"Tuesday"}
	- confirmed
* review_labResults
	- utter_reviewLabResults
* request_refill{"medicine":"Mirena"}
	- utter_prescription_refill


