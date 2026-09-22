# Iris Flower Classifier
# A beginner machine learning project using scikit-learn.

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


def main():
    # 1. Load the Iris dataset
    iris = load_iris()

    X = iris.data
    y = iris.target

    # 2. Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    # 3. Create the machine learning model
    model = DecisionTreeClassifier(random_state=42)

    # 4. Train the model
    model.fit(X_train, y_train)

    # 5. Make predictions
    predictions = model.predict(X_test)

    # 6. Calculate accuracy
    accuracy = accuracy_score(y_test, predictions)

    print("=" * 45)
    print("       IRIS FLOWER CLASSIFIER")
    print("=" * 45)

    print(f"\nTraining samples: {len(X_train)}")
    print(f"Testing samples: {len(X_test)}")
    print(f"Model accuracy: {accuracy * 100:.2f}%")

    print("\nExample Predictions:")

    for i in range(5):
        actual = iris.target_names[y_test[i]]
        predicted = iris.target_names[predictions[i]]

        print(
            f"Actual: {actual:<12} "
            f"Predicted: {predicted}"
        )

    print("\nModel training completed successfully!")


if name == "main":
    main()
