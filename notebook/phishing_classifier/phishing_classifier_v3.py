import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

# 📥 Load CSV (adjust path if needed)
file_path = 'C:/myfolder/github/ml-for-security/data/Phishing_Email.csv'
df = pd.read_csv(file_path, usecols=["Email Text", "Email Type"])

print(f"✅ Loaded dataset with shape: {df.shape}")
print(f"📋 Columns: {df.columns.tolist()}")

# 📊 Show original number of rows
original_rows = len(df)
print(f"📦 Original rows: {original_rows}")

# 🔧 Rename columns
df = df.rename(columns={'Email Text': 'text', 'Email Type': 'label'})

# 🧹 Drop rows with missing or blank text or label
df = df.dropna(subset=['text', 'label'])
df = df[df['text'].str.strip() != '']
df = df[df['label'].str.strip() != '']

# 🔁 Normalize label values
df['label'] = df['label'].str.strip()
df['label'] = df['label'].map({
    'Phishing Email': 1,
    'Safe Email': 0
})

# ❌ Drop rows where label mapping failed
df = df.dropna(subset=['label'])

# 📈 Report cleaned dataset stats
cleaned_rows = len(df)
print(f"✅ Cleaned rows: {cleaned_rows}")
print(f"🗑️ Rows dropped during cleaning: {original_rows - cleaned_rows}")
print("✅ Label distribution:\n", df['label'].value_counts())

# 🔀 Split data
X_train, X_test, y_train, y_test = train_test_split(
    df['text'], df['label'], test_size=0.2, random_state=42
)

# 🔡 Vectorize text
vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# 🤖 Train model
model = LogisticRegression()
model.fit(X_train_vec, y_train)

# 📊 Evaluate model
y_pred = model.predict(X_test_vec)
print("\n📊 Classification Report:")
print(classification_report(y_test, y_pred))

