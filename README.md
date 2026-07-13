# Web Application Security Testing Using Misuse Case Based Test Model

This repository contains the source code and Natural Language Processing (NLP) implementation developed for the study "Web Application Security Testing Using Misuse Case Based Test Model." The proposed approach takes misuse case specifications written in Restricted Misuse Case Modeling notation as input. The misuse case descriptions are processed using Natural Language Processing (NLP) techniques, including tokenization, keyword extraction, and part-of-speech tagging, to extract security-relevant information. The extracted information is then mapped to the corresponding class model to automatically generate Object Constraint Language (OCL) constraints, which are subsequently used for web application security test case generation.

## Contents

- `Raw Data for Web Application Security Testing.xlsx` – Curated raw data containing the misuse case specifications used in this study.
- `tokenization.py` – Performs tokenization of misuse case specifications.
- `Keywords matcher.py` – Identifies security-related keywords from misuse case descriptions.
- `POS tagging.py` – Performs Part-of-Speech (POS) tagging using spaCy.
- `Pattern based labelling code.py` – Labels extracted information using predefined linguistic patterns.
- `Algorithms described in manuscript.md` – Algorithms presented in the research paper.
- `Case Study 1 login page source code.php` – Source code used in the first case study.
- `Case Study 2 user model source code.php` – Source code used in the second case study.

## Dataset Information

This repository includes the curated raw data used in the study. The file **Raw Data for Web Application Security Testing.xlsx** contains two misuse case specifications:
- **Bypass Authorization** – A hypothetical misuse case used to illustrate the proposed methodology.
- **Injection Attack** – The misuse case used for the case study and evaluation presented in the manuscript.
These misuse case specifications serve as the input to the proposed NLP-based framework.

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

1. Download the repository.
2. Open **Raw Data for Web Application Security Testing.xlsx** and select a misuse case specification.
3. Copy the selected misuse case specification into the `data` variable in the Python scripts.
4. Install Python and spaCy.
5. Download the English language model for spaCy.
6. Execute the Python scripts in the following order:
   - `tokenization.py`
   - `Keywords matcher.py`
   - `POS tagging.py`
   - `Pattern based labelling code.py`
7. Review the extracted information and use it as described in the manuscript.
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

This repository accompanies the manuscript entitled *Web Application Security Testing Using Misuse Case Based Test Model*. If you use the source code or raw dataset provided in this repository for academic or research purposes, please cite the corresponding published article.

---
## License

This repository is provided for academic and research purposes only.
