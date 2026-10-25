# ==============================================================================
# Section B — Practical Assessment (20 Marks)
# ==============================================================================

# ------------------------------------------------------------------------------
# Task 1 — Data Handling with Pandas (5 Marks)
# ------------------------------------------------------------------------------
import pandas as pd

print("=== TASK 1: Data Handling with Pandas ===")
data = {
    "Student": ["Ali", "Sara", "Usman", "Hina"],
    "Marks": [75, None, 61, 90],
    "Attendance": [80, 92, 67, 95]
}

df = pd.DataFrame(data)

print("--- Initial DataFrame (First Rows) ---")
print(df.head())
print("\n--- DataFrame Shape ---")
print(df.shape)

mean_marks = df["Marks"].mean()
df["Marks"] = df["Marks"].fillna(mean_marks)

print("\n--- Cleaned DataFrame (Missing Value Imputed) ---")
print(df)
print("\n" + "="*60 + "\n")


# ------------------------------------------------------------------------------
# Task 2 — Train and Evaluate a Classifier (5 Marks)
# ------------------------------------------------------------------------------
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

print("=== TASK 2: Train and Evaluate a Classifier ===")
# (a) Separate features and labels
iris = load_iris()
X = iris.data
y = iris.target

# (b) Create an 80/20 train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42
)

# (c) Train a DecisionTreeClassifier
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train, y_train)

# (d) Print test accuracy
y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Test Accuracy: {accuracy:.4f} ({accuracy * 100:.2f}%)")
print("\n" + "="*60 + "\n")


# ------------------------------------------------------------------------------
# Task 3 — Parse an OCR JSON Response (5 Marks)
# ------------------------------------------------------------------------------
print("=== TASK 3: Parse an OCR JSON Response ===")
ocr_response = {
    "result": {
        "words_block_list": [
            {"words": "INVOICE 1024"},
            {"words": "Total: 5,200"},
            {"words": "Date: 2026-10-20"}
        ]
    }
}

word_blocks = ocr_response["result"]["words_block_list"]
for block in word_blocks:
    print(block["words"])
print("\n" + "="*60 + "\n")


# ------------------------------------------------------------------------------
# Task 4 — Improve a Prompt (5 Marks)
# ------------------------------------------------------------------------------
print("=== TASK 4: Improve a Prompt ===")
improved_prompt = (
    "Act as an AI instructor teaching beginner HCCDA-AI students who have basic "
    "programming knowledge but no prior machine learning experience. Explain the "
    "core concepts of Artificial Intelligence, specifically contrasting Machine "
    "Learning (ML) and Deep Learning (DL) with one real-world industry example "
    "for each. Keep the total response under 200 words and avoid complex "
    "mathematical formulas or heavy academic jargon. Present your response as a "
    "brief introductory paragraph followed by a Markdown comparison table with "
    "columns for 'Concept', 'Simple Definition', and 'Real-World Example'."
)

print("Improved Prompt:\n", improved_prompt)
print("\nLabeled Key Parts:")
print("- Audience: Beginner HCCDA-AI students with basic programming knowledge but no prior ML experience.")
print("- Task/Context: Act as an AI instructor explaining AI core concepts, contrasting ML and DL with industry examples.")
print("- Constraint: Under 200 words, no complex math formulas or heavy academic jargon.")
print("- Output Format: Introductory paragraph followed by a 3-column Markdown comparison table.")
