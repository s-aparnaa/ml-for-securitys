# 🕵️‍♀️ PII Masking Tool — AI for Privacy Protection

Welcome to this practical NLP project that detects and masks **Personally Identifiable Information (PII)** in text using the **AI4Privacy dataset**.

This project is ideal for **students, security analysts, and data scientists** looking to explore privacy-preserving AI tools.

---

## 📦 Dataset

We use the **AI4Privacy PII-Masking 200K** dataset available on Kaggle:  
🔗 [AI4Privacy Dataset](https://www.kaggle.com/datasets/verracodeguacas/ai4privacy-pii)

> ⚠️ Please **download the dataset manually** from Kaggle.  
> After downloading:
> - Extract the ZIP file
> - Use `english_pii_43k.jsonl` from the dataset
> - Upload it to your Google Drive in a folder named `PII`



## 📚 What This Project Does

✅ Loads and parses real-world privacy-labeled text  
✅ Detects and replaces PII with standard tags like `[NAME]`, `[AGE]`, `[ADDRESS]`  
✅ Saves clean, anonymized output to `.csv`  
✅ Includes a **lite audit** (shape, missing values, datatypes)


---

## 🧠 How to Run

### 1. Clone this repo (or open in Google Colab):
```bash
git clone https://github.com/your-username/pii-masking-tool.git
cd pii-masking-tool
```bash


### 2. Install required Python libraries:
```bash

pip install pandas
```
### 3. Download the dataset from Kaggle:
Download the dataset from [AI4Privacy Dataset](https://www.kaggle.com/datasets/verracodeguacas/ai4privacy-pii)


Extract it and place ```english_pii_43k.jsonl``` in the ```PII/``` folder of this project.

### 4. Run the script:
```bash

python notebooks/pii_masking.py
```
## 🔍 Project Highlights
* 🔐 Supports PII types like NAME, AGE, IMEI, VEHICLE, PASSWORD, etc.

* 🔄 Converts raw PII labels like [FIRSTNAME_1] to [NAME]

* 📊 Quick data audit (shape, missing, preview)

* 💾 Outputs masked text for secure sharing and analysis

* 📈 Sample Code Snippet
```python

def standardize_placeholder(original_tag):
    clean = original_tag.strip('[]')
    base = clean.split('_')[0]
    return f'[{tag_map.get(base, base)}]'

def mask_pii_standard(unmasked_text, privacy_mask_json):
    pii_map = json.loads(privacy_mask_json.replace("'", '"'))
    for tag, actual in pii_map.items():
        standardized = standardize_placeholder(tag)
        unmasked_text = unmasked_text.replace(actual, standardized)
    return unmasked_text

```
------

🧩 Contributing
This is a beginner-friendly repo. Feel free to:

* Add support for more PII tag types

* Build a Streamlit UI for document redaction

* Extend to multilanguage masking (French, German, etc.)

* Integrate with spaCy or Transformers for live NER detection




## ⭐ Credits
Maintained by [@s-aparnaa](https://github.com/s-aparnaa)
Dataset from Kaggle -  [AI4Privacy Dataset](https://www.kaggle.com/datasets/verracodeguacas/ai4privacy-pii)



