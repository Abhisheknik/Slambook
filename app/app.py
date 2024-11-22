from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)

# Define where to store the form data (in the volume)
DATA_FILE = '/data/form_data.json'  # This is where the volume will store the data

# Ensure data file exists
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'w') as f:
        json.dump([], f)

@app.route('/')
def index():
    # Render the form template (now with slambook-style fields)
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Retrieve form data from the submitted form
    name = request.form.get('name')
    date = request.form.get('date')
    hobbies = request.form.get('hobbies')
    slimbook = request.form.get('slimbook')
    dream_destination = request.form.get('dream_destination')
    life_motto = request.form.get('life_motto')
    funny_memory = request.form.get('funny_memory')

    # Create a dictionary to store the form data
    form_data = {
        'name': name,
        'date': date,
        'hobbies': hobbies,
        'slimbook': slimbook,
        'dream_destination': dream_destination,  # New field
        'life_motto': life_motto,        # New field
        'funny_memory': funny_memory       # New field
    }

    # Load existing data from the JSON file
    with open(DATA_FILE, 'r') as f:
        data = json.load(f)

    # Append the new form data
    data.append(form_data)

    # Save the updated data back to the JSON file
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

    # Respond with a success message
    return jsonify({"message": "Data saved successfully!"})

if __name__ == '__main__':
    # Run the Flask application on all interfaces
    app.run(debug=True, host='0.0.0.0')
