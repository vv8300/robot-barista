import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report

# 1. Load data
df = pd.read_csv(r"C:\Users\mvign\Downloads\matches.csv")

# 2. Drop rows where winner is missing
df = df.dropna(subset=['winner'])

# 3. Select features (inputs for our model)
features = ['team1', 'team2', 'toss_winner', 'toss_decision', 'venue']
df = df[features + ['winner']].dropna()

# 4. Encode text columns into numbers
le = LabelEncoder()
for col in features + ['winner']:
    df[col] = le.fit_transform(df[col])

# 5. Split into input (X) and output (y)
X = df[features]
y = df['winner']

# 6. Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 7. Train the model
# Try different number of trees
for trees in [50, 100, 200, 500]:
    model = RandomForestClassifier(n_estimators=trees, random_state=10008)
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    acc = accuracy_score(y_test, pred)
    print(f"Trees: {trees} → Accuracy: {acc*100:.2f}%")
 
# 8. Evaluate
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)

print("=" * 40)
print(f"✅ Model trained successfully!")
print(f"🎯 Accuracy: {accuracy * 100:.2f}%")
print("=" * 40)

# 9. Feature importance
importances = pd.Series(
    model.feature_importances_, index=features
).sort_values(ascending=False)

print("\n📊 What matters most for predicting a winner:")
print(importances)