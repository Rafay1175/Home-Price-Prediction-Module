import pickle
import os

# Locate the path to the model_pickle file relative to this script
pickle_path = os.path.join(os.path.dirname(__file__), "model_pickle")

# Open the pickle file using the correct path
with open(pickle_path, "rb") as f:
    model = pickle.load(f)

def predict(area):
    """
    Function to Predict home price based on input area.
    """
    if isinstance(area, int):
        return round(model.predict([[area]])[0], 2)
    else:
        return "Invalid Input!"


def predict_loop():
    while True:
        print("""1. Check the price of a home based on the input area.
    0. Exit the program.""")
        choice = int(input("Enter a choice: "))
        if choice == 1:
            area = int(input("Enter the area: "))
            print(f"The Price for the Area is: {predict(area)}")
        elif choice == 0:
            break
        else:
            print("Invalid Command!")
