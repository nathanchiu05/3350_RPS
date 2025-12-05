# Dependencies
In the SUBMISSION_AISE_3350A_20.ipynb, when choosing a kernal, select "+ CREATE PYTHON ENVIORNMENT" --> "VENV" --> Python 3.10.18
- It is important to use a python 3.9 - python 3.12 enviornment becuase MediaPipe Hands only supports python 3.9 - python 3.12

# Feature Extraction
Using images from https://www.kaggle.com/datasets/drgfreeman/rockpaperscissors, the script feature_extraction.ipynb uses OpenCV's MediaPipe hand landmarkers to identify 21 X and 21 Y-coordinates for each sample in the dataset. These coordinates are then normalized by subtracting the wrist coordinates from the rest of the landmark coordinates. This sets the wrist coordinates (X0, Y0) to 0.0. A CSV dataset is created with this normalized data, where the first row contains the labels ('rock', 'paper', or 'scissors'), and the following rows contain X0, Y0, X1, Y1... X20, Y20. This CSV dataset can be found here: https://www.kaggle.com/datasets/nathanchiu2005/rock-paper-scissors-landmarks

# Random Forest Classifier
Random forest classifier was the chosen model to classify hands as either 'rock', 'paper', or 'scissors'. The dataset was split 80/20 training/testing. The model architecture consists of: 100 trees, max depth 10, n_jobs=-1 using all CPU cores. 

# Identifying Player's Hands
The detailed logic for identifying players can be found in the PDF document:

[View Identifying Players Logic PDF](./identifying_players_logic.pdf)
