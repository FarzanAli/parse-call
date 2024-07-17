import json

data = [
    {
        "transcription": "Welcome to Rogers. For English, press 1. Pour le français, faites le 2.",
        "options": {
            "For English, press 1.": "option",
            "Pour le français, faites le 2.": "option"
        },
    },
    {
        "transcription": "Please enter your phone number, then press pound. If new to Rogers, press star.",
        "actions": {
            "Please enter your phone number, then press pound.": "action",
        },
        "options": {
            "If new to Rogers, press star.": "option"
        }
    },
    {
        "transcription": "For billing and payment inquiries, press 1. For technical support, press 2. To add products and services, press 3. For account changes, press 4.",
        "options": {
            "For billing and payment inquiries, press 1.": "option",
            "For technical support, press 2.": "option",
            "To add products and services, press 3.": "option",
            "For account changes, press 4.": "option"
        }
    },
    {
        "transcription": "For account balance, last bill and payment information, press 1. To make a credit card payment, press 2. For payment arrangements, press 3. For usage details, press 4. For travel-related inquiries, including roaming, press 5. For more options, press 6.",
        "options": {
            "For account balance, last bill and payment information, press 1.": "option",
            "To make a credit card payment, press 2.": "option",
            "For payment arrangements, press 3.": "option",
            "For usage details, press 4.": "option",
            "For travel-related inquiries, including roaming, press 5.": "option",
            "For more options, press 6.": "option"
        }
    },
    {
        "transcription": "To review your recent payments, press 1. To set up automatic payments for your account, press 2. To request a copy of your last bill, press 3. For questions concerning your bill, press 4. To return to the previous menu, press 8. To return to the main menu, press 9.",
        "options": {
            "To review your recent payments, press 1.": "option",
            "To set up automatic payments for your account, press 2.": "option",
            "To request a copy of your last bill, press 3.": "option",
            "For questions concerning your bill, press 4.": "option",
            "To return to the previous menu, press 8.": "option",
            "To return to the main menu, press 9.": "option"
        }
    },
    {
        "transcription": "Welcome to TELUS. Calls made to and from TELUS may be recorded for quality assurance and training purposes, to create TELUS offers for you, and to serve you better. For service in English, press 1. Pour français, appuyez sur 2. 粵語,請按3。 普通話,請按4。",
        "options":{
            "For service in English, press 1.": "option",
            "Pour français, appuyez sur 2.": "option",
            "粵語,請按3。": "option",
            "普通話,請按4。": "option",
        }
    },
    {
        "transcription": "To help me get you to the right place, please tell me your 10-digit phone number related to the account you're calling about. If you are an existing customer and don't know your number, say, I don't know my number. Or, if you would like to join TELUS, say, I want to join TELUS.",
        "actions": {
            "To help me get you to the right place, please tell me your 10-digit phone number related to the account you're calling about.": "action",
            "If you are an existing customer and don't know your number, say, I don't know my number.": "action",
            "Or, if you would like to join TELUS, say, I want to join TELUS.": "action",
        }
    },
    {
        "transcription": "I see a business mobility account related to the number you provided. Is this what you're calling about? Sorry, I didn't get that. I see a business mobility account related to the number you provided. Is this what you're calling about? Is this what you're calling about? Let's get your account verified. Providing your PIN now will help enhance your experience. Do you know or have the PIN on the account? No problem. How can I help you today?",
        "actions": {
            "Let's get your account verified. Providing your PIN now will help enhance your experience. Do you know or have the PIN on the account?": "action",
            "No problem. How can I help you today?": "action"
        }
    },
    {
        "transcription": "Welcome to Bell Mobility. For English, press 1. Pour le français, appuyez sur le 2.",
        "options": {
            "For English, press 1.": "option",
            "Pour le français, appuyez sur le 2.": "option"
        }
    },
    {
        "transcription": "Please enter the 10-digit telephone number you're calling about. If you would like to become a Bell customer or are in the process of becoming one, press pound.",
        "actions": {
            "Please enter the 10-digit telephone number you're calling about.": "action",
        },
        "options": {
            "If you would like to become a Bell customer or are in the process of becoming one, press pound.": "option"
        }
    },
    {
        "transcription": "If you are calling about a tablet, mobile internet device, or a connected thing such as a smartwatch, camera, or connected car, press 1. To become a Bell Mobility customer, press 2. If you are calling regarding a recently placed order and would like to modify it or have not yet received your device, press 3. For prepaid pay-as-you-go service, press 4. If you are an existing Bell Mobility customer or for anything else, press 5.",
        "options": {
            "If you are calling about a tablet, mobile internet device, or a connected thing such as a smartwatch, camera, or connected car, press 1.": "option",
            "To become a Bell Mobility customer, press 2.": "option",
            "If you are calling regarding a recently placed order and would like to modify it or have not yet received your device, press 3.": "option",
            "For prepaid pay-as-you-go service, press 4.": "option",
            "If you are an existing Bell Mobility customer or for anything else, press 5.": "option"
        }
    },
    {
        "transcription": "For billing or changes on your account, press 1. For technical support, press 2. To go back to the main menu, press 8.",
        "options": {
            "For billing or changes on your account, press 1.": "option",
            "For technical support, press 2.": "option",
            "To go back to the main menu, press 8.": "option",
        }
    },
    {
        "transcription": "Calls are recorded and used for training and quality assurance purposes and to help serve you better in accordance with our privacy policy, available at bell.ca slash privacy.",
    },
    {
        "transcription": "Thank you for calling TD EasyLine. Merci d'avoir appelé le service Bantel de la TD. Pour le service en français, appuyez sur le 2.",
        "options": {
            "Pour le service en français, appuyez sur le 2.": "option"
        }
    },
    {
        "transcription": "Please enter your access card number. If you need a moment to locate your card, press the pound key. If you don't have one, press 2. To hear the options again, press 6.",
        "actions": {
            "Please enter your access card number.": "action",
            "If you need a moment to locate your card, press the pound key.": "action",
        },
        "options": {
            "If you don't have one, press 2.": "option",
            "To hear the options again, press 6.": "option"
        }
    },
    {
        "transcription": "At any time during your call, press 6 to repeat the options you just heard, 8 to go back to the previous menu, or star to return to the main EasyLine options. To open a new personal bank account, press 1 for TD credit products, 2 to dispute a transaction, or to report a lost or stolen card, 3 for saving and investing, 4 for small. Business banking, 5 for anything else. Press 0.",
        "options": {
            "press 6 to repeat the options you just heard": "option",
            "8 to go back to the previous menu": "option",
            "star to return to the main EasyLine options": "option",
            "To open a new personal bank account, press 1 for TD credit products": "option",
            "2 to dispute a transaction, or to report a lost or stolen card": "option",
            "3 for saving and investing": "option",
            "4 for small.": "option",
            "Business banking, 5": "option",
            "for anything else. Press 0.": "option"
        }
    },
    {
        "transcription": "Please enter your 3-digit pin. Please enter your 4 digit pin. Please enter your security code. Please enter your phone number. Please say or enter your credit card number. Please say your first name. Press 1 for front desk. For timings press 2. Please say your last name. Please enter your pin number.",
        "actions": {
            "Please enter your 3-digit pin.": "action",
            "Please enter your 4 digit pin.": "action",
            "Please enter your security code.": "action",
            "Please enter your phone number.": "action",
            "Please say or enter your credit card number.": "action",
            "Please say your first name.": "action",
            "Please say your last name.": "action",
            "Please enter your pin number.": "action",
        },
        "options": {
            "Press 1 for front desk.": "option",
            "For timings press 2.": "option",
        }
    }
]

TRAIN_DATA = []

for entry in data:
    transcription = entry['transcription']
    entities = []
    for option, label in entry.get('options', {}).items():
        start_idx = transcription.find(option)
        if start_idx != -1:
            end_idx = start_idx + len(option)
            entities.append((start_idx, end_idx, label))
    for action, label in entry.get("actions", {}).items():
        start_idx = transcription.find(action)
        if start_idx != -1:
            end_idx = start_idx + len(action)
            entities.append((start_idx, end_idx, label))
    TRAIN_DATA.append((transcription, {"entities": entities}))

with open('train_data.json', 'w') as f:
    json.dump(TRAIN_DATA, f, indent=4)
