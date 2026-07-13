# Web Application Security Testing Using Misuse Case Based Test Model

This repository contains the source code and Natural Language Processing (NLP) implementation developed for the study "Web Application Security Testing Using Misuse Case Based Test Model." The proposed approach takes misuse case specifications written in Restricted Misuse Case Modeling notation as input. The misuse case descriptions are processed using Natural Language Processing (NLP) techniques, including tokenization, keyword extraction, and part-of-speech tagging, to extract security-relevant information. The extracted information is then mapped to the corresponding class model to automatically generate Object Constraint Language (OCL) constraints, which are subsequently used for web application security test case generation.

## Contents

- `tokenization.py` – Performs tokenization of misuse case specifications.
- `Keywords matcher.py` – Identifies security-related keywords from misuse case descriptions.
- `POS tagging.py` – Performs Part-of-Speech (POS) tagging using spaCy.
- `Pattern based labelling code.py` – Labels extracted information using predefined linguistic patterns.
- `Algorithms described in manuscript.docx` – Algorithms presented in the research paper.
- `Case Study 1 login page source code.docx` – Source code used in the first case study.
- `Case Study 2 user model source code.docx` – Source code used in the second case study.

## Dataset Information

This study does not use a machine learning training dataset. The proposed framework processes misuse case specifications using Natural Language Processing (NLP) techniques. The misuse case specifications processed using NLP are already presented in Manuscript.

## Code Information

The source code implements the NLP-based preprocessing of the misuse case specifications presented in the manuscript. The implementation includes tokenization, keyword extraction, Part-of-Speech (POS) tagging, and pattern-based labeling. The extracted information is manually mapped to the class model to support the proposed misuse case-based security testing framework.

## Requirements

- Python 3.x
- spaCy
- Google Colab (optional)

Required Python package:

```bash
pip install spacy
python -m spacy download en_core_web_sm
```

---

## Usage Instructions

1. Install Python and spaCy.
2. Download the English language model for spaCy.
3. Execute the Python scripts in the following order:
   - `tokenization.py`
   - `Keywords matcher.py`
   - `POS tagging.py`
   - `Pattern based labelling code.py`
4. Review the extracted information.
5. Use the generated information to construct Object Constraint Language (OCL) constraints and security test cases as described in the paper.

---

## Methodology

The proposed framework consists of the following steps:

1. Input misuse case specifications written in Restricted Misuse Case Modeling notation.
2. Perform tokenization of the misuse case descriptions.
3. Extract security-related keywords.
4. Apply Part-of-Speech (POS) tagging.
5. Label the extracted information using predefined patterns.
6. Generate Object Constraint Language (OCL) constraints.
7. Generate a test model graph from the misuse case specification.
8. Generate test sequences from the test model graph.
9. Generate test cases from the generated test sequences.
---

## Citation

This repository accompanies the manuscript "Web Application Security Testing Using Misuse Case Based Test Model." Please cite the published article if you use this repository after publication.

---

## License
This repository is provided for academic and research purposes only.
