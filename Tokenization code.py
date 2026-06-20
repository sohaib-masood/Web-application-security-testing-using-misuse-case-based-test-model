import spacy

nlp = spacy.load("en_core_web_sm")

# Tokenization using spaCy's nlp() function
doc = nlp(data)

print("STEP 1: TOKENIZATION")
print("-" * 40)
for token in doc:
    print(token.text)