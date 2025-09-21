from flask import Flask, request, jsonify
from flask_mail import Mail, Message
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app) # Enable CORS for all routes

# Flask-Mail configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME') # Use environment variable
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD') # Use environment variable
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('MAIL_USERNAME')

mail = Mail(app)

@app.route('/submit_form', methods=['POST'])
def submit_form():
    try:
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')

        if not all([name, email]):
            return jsonify({'message': 'Name and Email are required.'}), 400

        msg = Message(
            'New Contact Form Submission',
            sender=app.config['MAIL_USERNAME'],
            body=f"""
Name: {name}
Email: {email}

"""
        )
        msg.recipients = ["rahulvarmaviit@gmail.com"]
        msg.cc = ["akh@akitscounsulting.com", "triveniguntuboyina@akitssconsulting.com"]
        mail.send(msg)

        return jsonify({'message': 'Form submitted successfully!'}), 200
    except Exception as e:
        return jsonify({'message': f'An error occurred: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)