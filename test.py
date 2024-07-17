import spacy

nlp = spacy.load("custom_ner_model")
doc = nlp("An absolute mess. Pour le français, faites le 2. If you would like to proceed in English, press 1. Or please enter your 6 digit pin")

for ent in doc.ents:
    print(ent.label_)
    print(ent.text)
    # if ent.label_ == "option" and any(char.isdigit() for char in ent.text):
    #     print(f"Recognized Option: '{ent.text}'")
    # elif ent.label_ == "action" and any(char.isdigit() for char in ent.text):
    #     print(f"Recognized Action: '{ent.text}'")