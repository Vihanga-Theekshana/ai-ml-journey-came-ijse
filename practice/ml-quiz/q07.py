import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix


df = pd.read_csv("customer_churn.csv")
X = df.drop(columns=['churn'])
y = df['churn']


X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=0.25, stratify=y, random_state=42)

scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_test_s = scaler.transform(X_test)


model = LogisticRegression(max_iter=1000)
model.fit(X_train_s, y_train)


share_churned = y_train.mean()
print(f"{share_churned:.4f}")


y_pred = model.predict(X_test_s)
acc = accuracy_score(y_test, y_pred)
print(f"{acc:.4f}")


prec = precision_score(y_test, y_pred)
rec = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
print(f"{prec:.4f}", f"{rec:.4f}", f"{f1:.4f}")


tn, fp, fn, tp = confusion_matrix(y_test, y_pred).ravel()
print(tn, fp, fn, tp)
