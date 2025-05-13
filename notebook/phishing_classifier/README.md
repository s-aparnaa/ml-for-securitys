# 🛡️ Phishing Email Classifier — Machine Learning for Beginners

Welcome to this beginner-friendly machine learning project that detects phishing emails using **Natural Language Processing (NLP)** and **Logistic Regression**.

This project is designed for **new developers and students** to practice ML using real-world data.

---

## 📦 Dataset

We use the public dataset available on Kaggle:  
🔗 [Phishing Emails Dataset](https://www.kaggle.com/datasets/subhajournal/phishingemails?resource=download)

### ⚠️ Important:
Please **download the CSV manually** from the Kaggle link above.  
After downloading:
- Extract the ZIP file
- Locate `Phishing_Email.csv`
- Place it in your local project folder (e.g., `ml-for-security/data/`)


## 📚 What This Project Does

✅ Loads and cleans real-world email data  
✅ Uses **TF-IDF vectorization** for text features  
✅ Trains a **Logistic Regression** model  
✅ Outputs evaluation metrics and classification report  

---


## 📚 What This Project Does
✅ Loads and cleans real-world email data
✅ Uses TF-IDF vectorization for text features
✅ Trains a Logistic Regression model
✅ Outputs evaluation metrics and classification report

## 🧠 How to Run
### 1. Clone the repository:
```bash

git clone https://github.com/s-aparnaa/ml-for-security.git
cd ml-for-security
```
### 2. Install required Python libraries:
```bash

pip install pandas scikit-learn matplotlib seaborn
```
### 3. Download the dataset from Kaggle:
Download the dataset from [Kaggle - Phishing Emails](https://www.kaggle.com/datasets/subhajournal/phishingemails?resource=download)


Extract it and place ```Phishing_Email.csv``` in the ```data/``` folder of this project.

### 4. Run the script:
```bash

python notebooks/phishing_email_classifier.py
```
## 🔍 Project Highlights
* 📊 Cleans and normalizes raw email text

* 🧼 Drops missing or irrelevant entries

* 💡 Explores data distribution and word counts

* 🤖 Builds a text classifier using scikit-learn

* 📈 Prints precision, recall, and F1-score

📈 Sample Code Snippet
```python

vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)
X_train_vec = vectorizer.fit_transform(X_train)

model = LogisticRegression()
model.fit(X_train_vec, y_train)
```
------

🧩 Contributing
This is a beginner-friendly repo. Feel free to:

* Add new models (e.g., Random Forest, XGBoost)

* Visualize more metrics or model comparisons

* Wrap this into a simple Streamlit or Flask web app

Create step-by-step Jupyter notebooks for educational walkthroughs


## ⭐ Credits
Maintained by [@s-aparnaa](https://github.com/s-aparnaa)
Dataset from Kaggle - [subhajournal](https://www.kaggle.com/datasets/subhajournal/phishingemails)

## 🧠 How to Run

### 1. Clone the repository:
```bash
git clone https://github.com/s-aparnaa/ml-for-security.git
cd ml-for-security
```
Update the following line in your Python code to point to the correct path on your machine:

```python
file_path = 'C:/your/path/to/Phishing_Email.csv'
```

