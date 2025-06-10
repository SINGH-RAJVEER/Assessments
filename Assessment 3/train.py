import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder, StandardScaler
import joblib

df = pd.read_csv('iris.csv')
df['species_label'] = LabelEncoder().fit_transform(df['species'])
X = df[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]
y = df['species_label']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

model = LogisticRegression(max_iter=200)
model.fit(X_scaled, y)

joblib.dump(model, 'iris_model.joblib')
joblib.dump(scaler, 'iris_scaler.joblib')