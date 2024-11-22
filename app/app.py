from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)

# Define the directory and file paths
DATA_DIR = '/data'
DATA_FILE = os.path.join(DATA_DIR, 'form_data.json')

# Ensure the directory and file exist
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'w') as f:
        json.dump([], f)

@app.route('/')
def index():
    """Render the form template."""
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    """Handle form submission."""
    try:
        # Retrieve form data from the submitted form
        form_data = {
            'name': request.form.get('name'),
            'date': request.form.get('date'),
            'hobbies': request.form.get('hobbies'),
            'slimbook': request.form.get('slimbook'),
            'dream_destination': request.form.get('dream_destination'),
            'life_motto': request.form.get('life_motto'),
            'funny_memory': request.form.get('funny_memory')
        }

        # Validate that required fields are not empty
        if not form_data['name'] or not form_data['date']:
            return jsonify({"error": "Name and Date are required fields!"}), 400

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

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    # Run the Flask application on all interfaces
    app.run(debug=True, host='0.0.0.0', port=5000)
