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
input_keywords = {
    "enter", "provide", "request", "input",
    "submit", "select", "modify"
}

output_keywords = {
    "display", "send", "response", "execute",
    "exploit", "log", "write", "update",
    "delete", "reject", "fail",
    "validate", "detect",
    "grant", "deny", "generate", "process" "authenticate"
}

system_entities = {
    "SYSTEM",
    "MALICIOUS_USER",
    "DATABASE",
    "APPLICATION"
}

skip_prefixes = {
    "btf", "satf", "saf", "rfs",
    "endfor", "endif",
    "resume", "foreach",
    "for", "end",
    "description",
    "primary",
    "misuse",
    "actor",
    "basic",
    "specific"
}

# ---------------------------------------------------
# Remove flow labels
# ---------------------------------------------------
def remove_flow_label(text):
    cleaned = re.sub(
        r'^(SATF\s+\w+\.\d*\.?|SAF\s+\w+\.\d*\.?|BTF\s+\d+\.?)\s*',
        '',
        text,
        flags=re.IGNORECASE
    )
    return cleaned.strip()

# ---------------------------------------------------
# Clean lines
# ---------------------------------------------------
lines = data.split("\n")

cleaned_lines = []

for line in lines:

    line = line.strip()

    if not line:
        continue

    cleaned_lines.append(remove_flow_label(line))

# ---------------------------------------------------
# Pattern Based Labeling
# ---------------------------------------------------

current_section = None

for line in cleaned_lines:

    if not line:
        continue

    first_word = line.split()[0].lower().rstrip(":")

    # -------------------------
    # Precondition Section
    # -------------------------
    if first_word == "precondition":
        current_section = "precondition"
        precondition_statements.add(line)
        continue

    # Continue collecting precondition until next section
    if current_section == "precondition":

        if (
            line.startswith("Basic Threat Flow")
            or line.startswith("Specific Alternative")
            or line.startswith("Postcondition")
        ):
            current_section = None
        else:
            precondition_statements.add(line)
            continue

    # -------------------------
    # Postcondition
    # -------------------------
    if first_word == "postcondition":
        postcondition_statements.add(line)
        continue

    # -------------------------
    # Skip headers
    # -------------------------
    if first_word in skip_prefixes:
        continue

    if any(skip in line for skip in [
        "Misuse Case:",
        "Primary Actor:",
        "Description:",
        "Basic Threat",
        "Specific Alternative",
        "RFS"
    ]):
        continue

    # -------------------------
    # Conditions
    # -------------------------
    if re.search(r"\bIF\b|\bIf\b", line) and re.search(r"\bTHEN\b|\bThen\b", line):
        condition_statements.add(line)
        continue

    # -------------------------
    # spaCy processing
    # -------------------------
    sent_doc = nlp(line)

    contains_system_entity = any(
        entity in line.upper()
        for entity in system_entities
    )

    contains_output_action = any(
        token.lemma_.lower() in output_keywords
        for token in sent_doc
    )

    contains_input_action = any(
        token.lemma_.lower() in input_keywords
        for token in sent_doc
    )

    # -------------------------
    # Output Statements
    # -------------------------
    if (
        "SYSTEM" in line.upper()
        and contains_output_action
    ):
        output_statements.add(line)

    # -------------------------
    # Input Statements
    # -------------------------
    elif (
        "MALICIOUS_USER" in line.upper()
        and contains_input_action
    ):
        input_statements.add(line)

# ---------------------------------------------------
# Display Results
# ---------------------------------------------------

print("\nPattern Based Labeling:")

print("\nPrecondition Statements:")
for s in sorted(precondition_statements):
    print(" →", s)

print("\nPostcondition Statements:")
for s in sorted(postcondition_statements):
    print(" →", s)

print("\nInput Statements:")
for s in sorted(input_statements):
    print(" →", s)

print("\nOutput Statements:")
for s in sorted(output_statements):
    print(" →", s)

print("\nCondition Statements:")
for s in sorted(condition_statements):
    print(" →", s)
