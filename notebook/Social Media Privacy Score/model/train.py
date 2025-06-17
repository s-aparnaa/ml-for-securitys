# model/train.py
"""
Training script for Social Media Privacy Risk Scorer.
Loads labeled data, trains regression models, saves artifacts for deployment.
"""
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error, r2_score
import joblib


def train_and_serialize(data_csv: str = 'data/social_posts_with_scores.csv', output_dir: str = 'model/artifacts'):
    os.makedirs(output_dir, exist_ok=True)
    # Load
    df = pd.read_csv(data_csv)
    X = df[['text']]
    y = df['risk_score']
    # Split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    # Preprocessor
    text_pipe = Pipeline([
        ('tfidf', TfidfVectorizer(max_features=5000, ngram_range=(1,2)))
    ])
    pre = ColumnTransformer([
        ('text', text_pipe, 'text')
    ])
    # Models
    models = {
        'random_forest': RandomForestRegressor(random_state=42),
        'gradient_boosting': GradientBoostingRegressor(random_state=42)
    }
    results = {}
    for name, model in models.items():
        pipe = Pipeline([('pre', pre), ('model', model)])
        pipe.fit(X_train, y_train)
        preds = pipe.predict(X_test)
        mse = mean_squared_error(y_test, preds)
        r2 = r2_score(y_test, preds)
        results[name] = {'pipeline': pipe, 'mse': mse, 'r2': r2}
        print(f"{name}: MSE={mse:.2f}, R2={r2:.2f}")

    # Hyperparameter tune best model
    best_name = min(results, key=lambda k: results[k]['mse'])
    best_pipe = results[best_name]['pipeline']
    print(f"Tuning {best_name}...")
    param_grid = {
        'model__n_estimators': [50, 100],
        'model__max_depth': [None, 10]
    }
    grid = GridSearchCV(best_pipe, param_grid, scoring='neg_mean_squared_error', cv=3)
    grid.fit(X_train, y_train)
    tuned = grid.best_estimator_
    tuned_preds = tuned.predict(X_test)
    print(f"Best params: {grid.best_params_}")
    print(f"Tuned MSE: {mean_squared_error(y_test, tuned_preds):.2f}")

    # Serialize
    artifact_path = os.path.join(output_dir, f"{best_name}_tuned.joblib")
    joblib.dump(tuned, artifact_path)
    print(f"Serialized model to {artifact_path}")
    return artifact_path


if __name__ == '__main__':
    train_and_serialize()



