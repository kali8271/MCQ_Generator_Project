import spacy
import json

# Load Spacy Model
nlp = spacy.load("en_core_web_sm")

def extract_named_entities():
    with open("summarized_news.json", "r", encoding="utf-8") as f:
        summaries = json.load(f)

    entity_data = []
    for summary in summaries:
        doc = nlp(summary)
        entities = {ent.text: ent.label_ for ent in doc.ents}
        entity_data.append(entities)

    return entity_data

if __name__ == "__main__":
    entities = extract_named_entities()
    with open("named_entities.json", "w", encoding="utf-8") as f:
        json.dump(entities, f, indent=4)
    print("Extracted named entities and saved to named_entities.json")
