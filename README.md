# Cardiovascular Disease Prediction using Artificial Neural Networks (ANN)
This project aims to predict the likelihood of cardiovascular disease (CVD) in patients using machine learning techniques, specifically an Artificial Neural Network (ANN). The model is trained on a dataset containing various health parameters such as age, gender, cholesterol levels, blood pressure, and other clinical features to predict whether a patient has a cardiovascular disease.<br><br><br>

*Features*<br>

Data Preprocessing: Cleaning and transforming the raw data into a suitable format for model training, including handling missing values, feature scaling, and encoding categorical variables.

*Exploratory Data Analysis (EDA)*: Analyzing and visualizing the data to uncover underlying patterns, correlations, and important features that influence CVD predictions.

*Model Training*: Building and training an ANN to predict the presence or absence of cardiovascular disease based on the provided input features.

*Evaluation*: Evaluating the model’s performance using accuracy, precision, recall, F1-score, and ROC-AUC to ensure reliable predictions.

*Deployment*: A backend Flask API that serves the trained model for real-time predictions via a web interface.

<br><br><br>
Input Data
To make predictions through the web interface, input the following patient features:

Age,
Gender,
Chest pain type,
Resting blood pressure,
Serum cholesterol,
Fasting blood sugar,
Resting ECG results,
Max heart rate achieved,
Exercise-induced angina,
Old peak (depression induced by exercise),
Slope of the peak exercise ST segment,
Number of major vessels colored by fluoroscopy,

<br><br><br>
How the Model Works
Data Preprocessing: The raw data is cleaned by removing missing values, normalizing numerical features, and encoding categorical variables.

Exploratory Data Analysis: Key features influencing cardiovascular disease risk are identified through visualizations such as histograms, correlation matrices, and boxplots.

Training the ANN: The model is trained using an artificial neural network to learn patterns from the data and predict the likelihood of CVD.

Prediction: Users can input health parameters via the web app to receive a real-time prediction (CVD: Percentage of positive case of CVD).

<br><br><br>
Model Evaluation<br>
The trained ANN model is evaluated using various metrics:

Accuracy: Percentage of correctly classified instances.

Precision: The proportion of positive predictions that are actually correct.

Recall: The proportion of actual positive cases that are correctly identified.

F1-Score: The harmonic mean of precision and recall.

ROC-AUC: The area under the receiver operating characteristic curve.

<br><br><br>
Results

The model achieves 97% accuracy in predicting the likelihood of cardiovascular disease based on clinical data. The prediction results are presented as a probability score, where higher values indicate a higher likelihood of the disease.
<br><br>
Prerequisites
Python 3.x
Libraries: pandas, numpy, matplotlib, seaborn, tensorflow, flask, scikit-learn
Git (for version control and repository management)
