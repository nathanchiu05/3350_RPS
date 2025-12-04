import cv2
import mediapipe as mp
import matplotlib.pyplot as plt
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

def extract_hand_landmark_features(hand_landmarks):  
    landmark_features = []

    #Use the wrist (landmark 0) for normalization reference
    base_x, base_y = hand_landmarks[0].x, hand_landmarks[0].y

    for landmark in hand_landmarks:
        # NORMALIZATION USED DURING TRAINING. POSITION RELATIVE TO WRIST
        landmark_features.append(landmark.x - base_x)
        landmark_features.append(landmark.y - base_y)

    #NORMALIZE AGAIN. USE DISTANCE FROM WRIST TO TIP OF MIDDLE FINGER AS REFERENCE
    X9_norm=landmark_features[18]
    Y9_norm=landmark_features[19]

    L_ref = ((X9_norm)**2 + (Y9_norm)**2)**0.5

    final_features = []
    for coord in landmark_features:
        final_features.append(coord / L_ref)

    return final_features

def plot_hand_landmarks_2d(hand_landmarks, handNum):
    x_coords = [landmark.x for landmark in hand_landmarks]
    y_coords = [landmark.y for landmark in hand_landmarks]

    # Create a scatter plot
    plt.figure(figsize=(6, 6))
    plt.scatter(x_coords, y_coords, c='blue', label='Landmarks')

    # Optionally, connect the landmarks based on HAND_CONNECTIONS
    for connection in mp_hands.HAND_CONNECTIONS:
        start_idx, end_idx = connection
        plt.plot(
            [x_coords[start_idx], x_coords[end_idx]],
            [y_coords[start_idx], y_coords[end_idx]],
            'r-'
        )

    plt.gca().invert_yaxis()  # Invert Y-axis to match image coordinates
    plt.title(f"Hand {handNum} Landmarks (2D)")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.show()

def get_landmarks(IMAGE_FILES):
    normalized_features_list = []
    wrist_coords=[]
    handNum = 1

    with mp_hands.Hands(
        static_image_mode=True, #media pipe setting for static images
        max_num_hands=4,
        min_detection_confidence=0.1) as hands:
        for file in IMAGE_FILES:
            image = cv2.imread(file)
            results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)) #process the image to find hands. Covert to numPy array cuz media pipe uses that format.

            if not results.multi_hand_landmarks: #if no hands detected, skip to next image
                continue
            
            #Iterate over each detected hand
            for hand_landmarks in results.multi_hand_landmarks: #hand_landmarks is a single hand found in the image. multi_hand_landmarks is a list of all hands found. iterate
                print ("-"*40)
                print(f"Hand {handNum}: Wrist coordinates NOT NORMALIZED: (",
                      f"{hand_landmarks.landmark[0].x}, " 
                      f"{hand_landmarks.landmark[0].y})")
                print ("-"*40)
                wrist_coords.append( (hand_landmarks.landmark[0].x, hand_landmarks.landmark[0].y) )
                
                # Extract and print normalized features for the current hand
                normalized_features = extract_hand_landmark_features(hand_landmarks.landmark) #.landmark is a list of 21 landmarks for the hand
                normalized_features_list.append(normalized_features)
                print ("-"*40)
                print(f"Hand {handNum}: {normalized_features}")
                print ("-"*40)

                # Plot the landmarks for the current hand
                plot_hand_landmarks_2d(hand_landmarks.landmark, handNum)

                handNum += 1

    return normalized_features_list, wrist_coords

# def main():
#     get_landmarks()
# if __name__ == "__main__":
#     main()
