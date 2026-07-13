import spacy

nlp = spacy.load("en_core_web_sm")

doc = nlp(data)

# STEP 2: KEYWORD DETECTION
# All words written in CAPITAL LETTERS are keywords

print("STEP 2: KEYWORD DETECTION")
print("-" * 40)

keywords = []
for token in doc:
    # Remove underscore and check if remaining text is all uppercase alphabetic
    cleaned = token.text.replace("_", "")
    if cleaned.isupper() and cleaned.isalpha():
        if token.text not in keywords:
            keywords.append(token.text)

print("Keywords:", keywords)
