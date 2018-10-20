
## Create Appointment
* create_appointment{"dr":"Dr. Scott", "date":"Monday"}
	- confirmed

## Message to Doctor
* message_doctor
	- utter_messageDoctor

## Get a Prescription refill
* get_prescription
	- utter_getPrescription

## Review lab results
* review_labResults
	- utter_reviewLabResults

## Complicated
* create_appointment{"dr":"Dr. Pike", "date":"Friday"}
	- confirmed
* get_prescription
	- utter_getPrescription
* message_doctor
	- utter_messageDoctor
* review_labResults
	- utter_reviewLabResults

## Complicated1
* create_appointment
	- ask_which_dr
* confirm_dr{"dr":"Dr. Blue"}
	- ask_date
* confirm_date {"date":"Wednesday"}
	- confirmed
* message_doctor
	- utter_messageDoctor
* get_prescription
	- utter_getPrescription
* review_labResults
	- utter_reviewLabResults

## Complicated2
* message_doctor{"dr":"Dr. Adams"}
	- ask_message
* note_to_doc{"message":"My knee still hurts"}
	- confirmed
* create_appointment
	- ask_date
* confirm_date {"date":"Tuesday"}
	- confirmed
* review_labResults
	- utter_reviewLabResults
* get_prescription
	- utter_getPrescription

## Creating Appointment
* create_appointment
	- ask_which_dr
* confirm_dr{"dr":"Dr. Adams"}
	- ask_date
* confirm_date {"date":"Tuesday"}
	- confirmed

## MoreComplicated2
* confirm_dr
	- ask_date
* confirm_date
	- confirmed

## MoreComplicated3
* confirm_date
	- confirmed

## MoreComplicated4
