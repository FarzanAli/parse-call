import spacy
from spacy.training.example import Example
import json

nlp = spacy.blank("en")

ner = nlp.add_pipe("ner", last=True)

f = open('train_data.json')
TRAIN_DATA = json.load(f)

for _, annotations in TRAIN_DATA:
    for ent in annotations.get('entities'):
        ner.add_label(ent[2])

other_pipes = [pipe for pipe in nlp.pipe_names if pipe != 'ner']
with nlp.disable_pipes(*other_pipes):
    optimizer = nlp.begin_training()
    for i in range(100):
        for text, annotations in TRAIN_DATA:
            example = Example.from_dict(nlp.make_doc(text), annotations)
            nlp.update([example], drop=0.35, sgd=optimizer)

nlp.to_disk('custom_ner_model')

nlp = spacy.load("custom_ner_model")
doc = nlp("A random sentence. Pour le français, faites le 2. If you would like to proceed in English, press 1. ")

for ent in doc.ents:
    if ent.label_ == "option" and any(char.isdigit() for char in ent.text):
        print(f"Recognized Option: '{ent.text}'")
    elif ent.label_ == "action" and any(char.isdigit() for char in ent.text):
        print(f"Recognized Action: '{ent.text}'")
# entities = {}
# for ent in doc.ents:
#     if ent.label_ not in entities:
#         entities[ent.label_] = []
#     entities[ent.label_].append(ent.text)

# for label, texts in entities.items():
#     print(f"{label}: {texts}")