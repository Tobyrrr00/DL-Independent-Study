# School-Projects
Projects completed while a student

## Small Single Files 
#### neuron.py
Implementation of a single neuron in python. As expected there isn't really anyting useful going on.

#### neuralNet.py
A simple neural net that learns to add two small number together. Done from scratch

#### neuralNetTF.py
A simple neural net that learns to add two small number together. 

## Music Genre Classifier

This project contains a Python-based project for classifying music genres. It is composed of two main Python scripts - preprocess.py and genreClassifier.py.

**preprocess.py**
The preprocess.py script is responsible for pre-processing the dataset, where it extracts Mel-frequency cepstral coefficients (MFCC) from each audio track. MFCCs are numerical representations of different properties of an audio signal, serving as the input to our machine learning model. The script splits each track into several segments, and MFCCs are computed for each of these segments.

The calculated features and corresponding labels (i.e., music genres) are stored in a JSON file (data.json). To simplify the training process, the script assigns numerical labels to each genre.

**genreClassifier.py**
The genreClassifier.py script loads the preprocessed data (MFCC features and genre labels) from the JSON file and splits it into training and test sets. It then defines a deep learning model using TensorFlow, which includes four hidden layers with varying numbers of neurons. Dropout layers and L2 regularization are utilized to prevent overfitting.

The model is trained using the Adam optimizer and a sparse categorical cross entropy loss function due to the multi-class nature of the problem. The script evaluates the model's performance by computing its accuracy on a set aside test set.

For visualization purposes, the script also includes a function that plots the model's accuracy and loss over the epochs. This visualization helps to track the model's learning progress over time. Finally, the trained model is saved for future use.

There are two Saved instances. Found in the folders genreClassifier and genreClassifier150. The difference between the two is the amount of epochs. The first was run for 50 and the second for 150 epochs. 

How to Run
To execute this project:

First download the training data. It can be found at:
https://www.kaggle.com/datasets/andradaolteanu/gtzan-dataset-music-genre-classification

Run preprocess.py to extract MFCCs from the audio data and save them in a JSON file.
Run genreClassifier.py to train and evaluate the music genre classifier.
The project requires Python 3.x and depends on several packages, including TensorFlow, NumPy, sklearn, matplotlib, and librosa. Make sure these are installed in your environment before running the scripts.