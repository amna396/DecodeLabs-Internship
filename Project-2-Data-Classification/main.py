# ==========================================================
# Project: Data Classification Using AI
# Algorithm: Decision Tree Classifier
# Dataset: Iris Flower Dataset
# ==========================================================

# ==========================
# Import Required Libraries
# ==========================

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt


# ==========================
# Load the Iris Dataset
# ==========================

iris = load_iris()

# Features (Flower Measurements)
X = iris.data

# Labels (Flower Species)
y = iris.target


# ==========================
# Display Dataset Information
# ==========================

print("=" * 50)
print("IRIS DATASET INFORMATION")
print("=" * 50)

print(f"Total Samples : {len(X)}")
print(f"Total Features: {len(iris.feature_names)}")

print("\nFeature Names:")
for feature in iris.feature_names:
    print(f"• {feature}")

print("\nTarget Classes:")
for index, flower in enumerate(iris.target_names):
    print(f"{index} : {flower}")

print("=" * 50)


# ==========================
# Split Dataset
# ==========================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

print("\nDataset Split")
print("-" * 30)
print(f"Training Samples : {len(X_train)}")
print(f"Testing Samples  : {len(X_test)}")


# ==========================
# Create Decision Tree Model
# ==========================

model = DecisionTreeClassifier(random_state=42)

print("\nTraining AI Model...")
model.fit(X_train, y_train)
print("Model Trained Successfully!")


# ==========================
# Make Predictions
# ==========================

y_pred = model.predict(X_test)

print("\nPredicted Labels:")
print(y_pred)


# ==========================
# Evaluate Model
# ==========================

accuracy = accuracy_score(y_test, y_pred)

print("\n" + "=" * 50)
print("MODEL PERFORMANCE")
print("=" * 50)

print(f"Model Accuracy : {accuracy * 100:.2f}%")

print("\nClassification Report")
print("-" * 50)
print(classification_report(
    y_test,
    y_pred,
    target_names=iris.target_names
))


# ==========================
# Data Visualization
# ==========================

plt.figure(figsize=(8, 6))

scatter = plt.scatter(
    X[:, 2],
    X[:, 3],
    c=y,
    cmap="viridis",
    edgecolors="black"
)

plt.xlabel("Petal Length (cm)", fontsize=11)
plt.ylabel("Petal Width (cm)", fontsize=11)
plt.title("Iris Dataset: Petal Length vs Petal Width", fontsize=13)

plt.colorbar(scatter, label="Flower Species")

plt.grid(alpha=0.3)

plt.show()


