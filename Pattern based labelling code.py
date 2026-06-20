import spacy
import re

nlp = spacy.load("en_core_web_sm")

doc = nlp(data)

input_statements = set()
output_statements = set()
condition_statements = set()
precondition_statements = set()
postcondition_statements = set()

# Keywords for each pattern
input_keywords = {"inputs", "enters", "provides", "requests",
                  "input", "submits", "selects"}
output_keywords = {"displays", "sends", "response", "executes",
                   "exploits", "logs", "modifies", "writes",
                   "updates", "deletes", "rejects", "fails",
                   "validates", "detects"}
condition_keywords = {"IF", "THEN", "if", "then"}

system_entities = {"SYSTEM", "MALICIOUS_USER", "DATABASE", "APPLICATION"}

# Prefixes to skip entirely
skip_prefixes = {"btf", "satf", "saf", "rfs", "endfor", "endif",
                 "resume", "foreach", "for", "end", "description",
                 "primary", "misuse", "actor", "basic", "specific"}

# Remove flow labels like "BTF 1.", "SATF A.1", "SAF B.1." from start of line
def remove_flow_label(text):
    # Removes patterns like BTF 1. or SATF A.1. or SAF B.1. from beginning
    cleaned = re.sub(r'^(SATF\s+\w+\.\d*\.?|SAF\s+\w+\.\d*\.?|BTF\s+\d+\.?)\s*', 
                     '', text, flags=re.IGNORECASE)
    return cleaned.strip()

# Split data into lines and process
lines = data.split("\n")
cleaned_lines = []
for line in lines:
    line = line.strip()
    if not line:
        continue
    cleaned_lines.append(remove_flow_label(line))

# Now classify each cleaned line
for line in cleaned_lines:
    if not line:
        continue

    # Get first word for prefix check
    first_word = line.split()[0].lower().rstrip(":")

    # --------------------------------------------------------
    # Precondition
    # --------------------------------------------------------
    if first_word == "precondition":
        precondition_statements.add(line)
        continue

    # --------------------------------------------------------
    # Postcondition
    # --------------------------------------------------------
    if first_word == "postcondition":
        postcondition_statements.add(line)
        continue

    # --------------------------------------------------------
    # Skip irrelevant lines
    # --------------------------------------------------------
    if first_word in skip_prefixes:
        continue

    # Skip header/description lines
    if any(skip in line for skip in ["Misuse Case:", "Primary Actor:",
                                      "Description:", "Basic Threat",
                                      "Specific Alternative", "RFS"]):
        continue

    # --------------------------------------------------------
    # Conditional Sentences (IF...THEN)
    # --------------------------------------------------------
    if re.search(r'\bIF\b|\bIf\b', line) and re.search(r'\bTHEN\b|\bThen\b', line):
        condition_statements.add(line)
        continue

    # --------------------------------------------------------
    # Process remaining lines with spaCy
    # --------------------------------------------------------
    sent_doc = nlp(line)
    contains_system_entity = any(entity in line.upper() 
                                  for entity in system_entities)
    contains_output_action = any(token.lemma_ in output_keywords 
                                  for token in sent_doc)
    contains_input_action = any(token.lemma_ in input_keywords 
                                 for token in sent_doc)

    # Output Statement
    if contains_system_entity and contains_output_action and \
       "SYSTEM" in line.upper():
        output_statements.add(line)

    # Input Statement
    elif contains_input_action and "MALICIOUS_USER" in line.upper():
        input_statements.add(line)


print("\nPattern Based Labeling:")

print("\nPrecondition Statements:")
for s in list(precondition_statements):
    print(" →", s)

print("\nPostcondition Statements:")
for s in list(postcondition_statements):
    print(" →", s)

print("\nInput Statements:")
for s in list(input_statements):
    print(" →", s)

print("\nOutput Statements:")
for s in list(output_statements):
    print(" →", s)

print("\nCondition Statements:")
for s in list(condition_statements):
    print(" →", s)