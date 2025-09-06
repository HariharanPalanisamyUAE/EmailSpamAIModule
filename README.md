Email Spam Classifier Web App
Illustration of AI-powered email spam detection with a protective shield and neural networks.

[![Python](https://img.shields.io/badge/Pythono/badge/scikitcensepplication built with Flask that classifies emails as spam or ham (not spam) using a pre-trained Naive Bayes model (with TF-IDF vectorization) from scikit-learn. The model is loaded from a saved .pkl file and can predict on user-input email text via a web form. It also demonstrates model accuracy on a set of example emails.

The app was developed as part of a tutorial series on building, saving, and deploying ML models locally. It's lightweight, runs offline (after setup), and serves as a starting point for text classification projects.

Features
User Input Form: Enter email text and get instant spam/ham classification.

Model Accuracy Display: Shows accuracy (match level) on predefined example emails, including predictions and true labels.

Simple UI: Basic HTML with styling for spam/ham results.

Offline Use: Runs locally with no external dependencies beyond Python libraries.

Extensible: Easy to integrate with larger apps or replace the model.

Prerequisites
Python 3.8 or higher.

The saved model file (hari_spam_model.pkl or your custom model) in the project directory.

Basic knowledge of running Python scripts and web servers.

Installation
Clone the Repository:

text
git clone https://github.com/yourusername/email-spam-classifier.git
cd email-spam-classifier
Install Dependencies:
Use the provrequirements.txt to install required packages:

text
pip install -r requirements.txt
This installs Flask, scikit-learn, joblib, and numpy.

Prepare the Model:

Ensure hari_spam_model.pkl (or your model file) is in the root directory. If you don't have it, train and save one using the code from the blog post (linked below).

Usage
Set Environment Variable:

On macOS/Linux:

text
export FLASK_APP=app.py
On Windows (Command Prompt):

text
set FLASK_APP=app.py
On Windows (PowerShell):

text
$env:FLASK_APP = "app.py"
Run the App:

text
flask run
The app will start on http://127.0.0.1:5000 (localhost:5000).

Open this URL in your browser.

Classify Emails:

Enter an email text in the form (e.g., "Win a free iPhone now!").

Submit to see the prediction (Spam or Ham).

View model accuracy and example predictions at the bottom of the page.

Example Input Data:
The app includes these examples for accuracy demonstration (editablapp.py):

"Win a free iPhone now! Click here to claim your prize." → Spam

"Hey, this is a test email. Are you free for a meeting?" → Ham

"Buy cheap meds online. Lowest prices guaranteed!" → Spam

"Reminder: Our team meeting is scheduled for tomorrow at 10 AM." → Ham

"Congratulations! You've won a lottery. Send your details to claim." → Spam

Accuracy is calculated as the percentage of correct predictions on these examples.

Stop the Server:
Press Ctrl+C in the term
