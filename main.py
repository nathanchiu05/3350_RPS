import pickle
from sklearn.ensemble import RandomForestClassifier #DEPENDENCY: pip install scikit-learn==1.2.2
import numpy as np

from hands_track import get_landmarks
from identify_player import identify_hands

IMAGE_FILES = ['sample_photos/TEST4.jpg']
landmarks, wrist_coords = get_landmarks(IMAGE_FILES)

MODEL_FILENAME = 'rps_classifier_V1.pkl'
store_predictions = []

print (wrist_coords)

try:
    with open(MODEL_FILENAME, 'rb') as file: #rb means read binary
        rps_classifier = pickle.load(file)
    
    for i in range(len(landmarks)):
        prediction = rps_classifier.predict(np.array(landmarks[i]).reshape(1,-1)) #landmarks is a list of lists. Convert to numpy array for prediction
        # print(f"Hand {i+1} Predicted Gesture: {prediction[0].upper()}") #prediction is an array, so get first element
        store_predictions.append(prediction[0])

except FileNotFoundError:
    print(f"Error: Model file '{MODEL_FILENAME}' not found.")
except Exception as e:
    print(f"Error during prediction: {e}")

hands = identify_hands(wrist_coords, store_predictions)
print (hands)

