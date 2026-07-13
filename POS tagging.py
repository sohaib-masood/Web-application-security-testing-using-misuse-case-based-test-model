import spacy
from spacy.tokens import Token
from spacy.matcher import PhraseMatcher

nlp = spacy.load("en_core_web_sm")

Token.set_extension("custom_pos", default=None, force=True)

# Define custom pronouns from detected keywords
custom_pronouns = ["MALICIOUS_USER", "SYSTEM"]

matcher = PhraseMatcher(nlp.vocab)
patterns = [nlp.make_doc(term) for term in custom_pronouns]
matcher.add("CUSTOM_PRONOUN", patterns)

doc = nlp(data)

# Apply custom POS to matched terms
matches = matcher(doc)
for match_id, start, end in matches:
    span = doc[start:end]
    for token in span:
        token.pos_ = "PRON"
        token._.custom_pos = "PRON"

# STEP 3: POS TAGGING
print("STEP 3: POS TAGGING")
print("-" * 50)
print(f"{'Token':<25} {'POS':<10} {'Dependency'}")
print("-" * 50)
for token in doc:
    if not token.is_space:
        pos = token._.custom_pos if token._.custom_pos else token.pos_
        print(f"{token.text:<25} {pos:<10} {token.dep_}")
