from flask import Flask, request, render_template_string
import joblib
import numpy as np

# Load the model
pipeline = joblib.load('hari_spam_model.pkl')
print("Model loaded successfully")  # This prints to console when app starts

# Example input data for demonstration (emails and their true labels: 1=spam, 0=ham)
example_emails = [
    "Win a free iPhone now! Click here to claim your prize.",
    "Hey, this is a test email. Are you free for a meeting?",
    "Buy cheap meds online. Lowest prices guaranteed!",
    "Reminder: Our team meeting is scheduled for tomorrow at 10 AM.",
    "Congratulations! You've won a lottery. Send your details to claim."
]
example_labels = [1, 0, 1, 0, 1]  # True labels for accuracy calculation

# Predict on example emails and calculate accuracy
example_predictions = pipeline.predict(example_emails)
accuracy = np.mean(example_predictions == np.array(example_labels)) * 100

# Initialize Flask app
app = Flask(__name__)

# HTML template for the webpage (simple form and results display)
html_template = '''
<!doctype html>
<html lang="en">
<head>
    <title>Email Spam Classifier</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        h1 { color: #333; }
        form { margin-bottom: 20px; }
        textarea { width: 400px; height: 100px; }
        .result { font-weight: bold; color: green; }
        .spam { color: red; }
    </style>
</head>
<body>
    <h1>Email Spam Classifier</h1>
    <p>Enter an email text below to classify it as Spam or Ham (not spam).</p>
    <form method="post">
        <label for="email">Email Text:</label><br>
        <textarea id="email" name="email" required></textarea><br><br>
        <input type="submit" value="Classify">
    </form>

    {% if prediction is defined %}
        <h2>Prediction Result:</h2>
        <p class="{% if prediction == 'Spam' %}spam{% else %}result{% endif %}">
            This email is classified as: {{ prediction }}
        </p>
    {% endif %}

    <h2>Model Accuracy on Example Data</h2>
    <p>The model was tested on 5 example emails with an accuracy of {{ accuracy }}% (match level).</p>
    <h3>Example Predictions:</h3>
    <ul>
        {% for email, pred in examples %}
            <li>
                <strong>Email:</strong> {{ email }}<br>
                <strong>Predicted:</strong> {{ pred }}<br>
                <strong>True Label:</strong> {{ true_labels[loop.index0] }}
            </li>
        {% endfor %}
    </ul>
</body>
</html>
'''

# Route for the homepage and form handling
@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    examples = []
    true_labels = ['Spam' if label == 1 else 'Ham' for label in example_labels]

    if request.method == 'POST':
        email_text = request.form['email']
        pred = pipeline.predict([email_text])[0]
        prediction = 'Spam' if pred == 1 else 'Ham (Not Spam)'

    # Prepare example predictions for display
    for i, email in enumerate(example_emails):
        pred = 'Spam' if example_predictions[i] == 1 else 'Ham'
        examples.append((email, pred))

    return render_template_string(html_template, prediction=prediction, accuracy=round(accuracy, 2), examples=examples, true_labels=true_labels)

if __name__ == '__main__':
    app.run(debug=True)