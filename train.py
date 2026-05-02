import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from preprocess import load_and_preprocess

df = load_and_preprocess("data/churn.csv")

X = df.drop("Churn", axis=1)
y = df["Churn"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

joblib.dump(model, "models/model.pkl")

print("Model trained and saved!")
