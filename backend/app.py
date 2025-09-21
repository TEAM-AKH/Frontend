import os
from flask import Flask, render_template, request, redirect, url_for, flash, send_from_directory, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_mail import Mail, Message
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from datetime import datetime
import uuid

UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', 'images')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

from flask_cors import CORS
import os
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_admin.model.fields import InlineFormField
from flask_admin.form.upload import FileUploadField
from werkzeug.datastructures import FileStorage
from flask_login import current_user

app = Flask(__name__, static_folder=os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'static'))
CORS(app) # Enable CORS for all routes

# Flask-Mail configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME') # Use environment variable
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD') # Use environment variable
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('MAIL_USERNAME')
app.config['UPLOAD_FOLDER'] = os.path.join(os.path.dirname(__file__), 'static', 'images')
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 # 16MB Max upload size
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

mail = Mail(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)
    is_admin = db.Column(db.Boolean, default=False) # Add this line

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    image_url = db.Column(db.String(200))
    social_media_link = db.Column(db.String(200))

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    details = db.Column(db.Text)
    image_url = db.Column(db.String(200))
    social_media_link = db.Column(db.String(200))

app.secret_key = os.environ.get('SECRET_KEY', 'a_very_secret_key') # Use environment variable or a default

class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('login', next=request.url))

class MyCustomAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated

admin = Admin(app, name='Acknowledgement', template_mode='bootstrap4', index_view=MyAdminIndexView())
admin.add_view(ModelView(User, db.session))
# admin.add_view(ModelView(Event, db.session))

class ProductAdminView(ModelView):
    column_list = ('id', 'name', 'details', 'image_url', 'social_media_link')
    form_columns = ('name', 'details', 'social_media_link', 'image_url', 'image_file')

    form_extra_fields = {
        'image_file': FileUploadField('Image', base_path=app.config['UPLOAD_FOLDER'], relative_path='')
    }

    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin

    def on_model_change(self, form, model, is_created):
        if form.image_file.data and isinstance(form.image_file.data, FileStorage):
            file = form.image_file.data
            filename = secure_filename(file.filename)
            if filename:
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(file_path)
                model.image_url = '/static/images/' + filename


admin.add_view(ProductAdminView(Product, db.session))

class EventAdminView(ModelView):
    column_list = ('id', 'title', 'description', 'image_url', 'social_media_link')
    form_columns = ('title', 'description', 'social_media_link', 'image_url', 'image_file')

    form_extra_fields = {
        'image_file': FileUploadField('Image', base_path=app.config['UPLOAD_FOLDER'], relative_path='')
    }

    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin

    def on_model_change(self, form, model, is_created):
        if form.image_file.data and isinstance(form.image_file.data, FileStorage):
            file = form.image_file.data
            filename = secure_filename(file.filename)
            if filename:
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(file_path)
                model.image_url = '/static/images/' + filename

admin.add_view(EventAdminView(Event, db.session))

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

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('admin.index'))
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('admin.index'))
        return 'Invalid username or password'
    return '''
        <form method="post">
            <p><input type="text" name="username"></p>
            <p><input type="password" name="password"></p>
            <p><input type="submit" value="Login"></p>
        </form>
    '''

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    products_data = [{'id': product.id, 'name': product.name, 'details': product.details, 'image_url': url_for('static', filename='images/' + os.path.basename(product.image_url)) if product.image_url else None, 'social_media_link': product.social_media_link} for product in products]
    return jsonify(products_data)

@app.route('/events', methods=['GET'])
def get_events():
    events = Event.query.all()
    events_data = [{'id': event.id, 'title': event.title, 'description': event.description, 'image_url': url_for('static', filename='images/' + os.path.basename(event.image_url)) if event.image_url else None, 'social_media_link': event.social_media_link} for event in events]
    return jsonify(events_data)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload_image', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({'message': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'message': 'No selected file'}), 400
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return jsonify({'image_url': url_for('static', filename='images/' + filename)}), 200
    return jsonify({'message': 'File type not allowed'}), 400


@app.route('/home.html')
def home():
    return send_from_directory(os.path.abspath(os.path.join(app.root_path, os.pardir)), 'home.html')

@app.route('/about.html')
def about():
    return send_from_directory(os.path.abspath(os.path.join(app.root_path, os.pardir)), 'about.html')

@app.route('/aiml.html')
def aiml():
    return send_from_directory(os.path.abspath(os.path.join(app.root_path, os.pardir)), 'aiml.html')

@app.route('/cloud.html')
def cloud():
    return send_from_directory(os.path.abspath(os.path.join(app.root_path, os.pardir)), 'cloud.html')

@app.route('/customsap.html')
def customsap():
    return send_from_directory(os.path.abspath(os.path.join(app.root_path, os.pardir)), 'customsap.html')

@app.route('/event.html')
def event():
    return send_from_directory(os.path.abspath(os.path.join(app.root_path, os.pardir)), 'event.html')

@app.route('/expertise.html')
def expertise():
    return send_from_directory(os.path.abspath(os.path.join(app.root_path, os.pardir)), 'expertise.html')

@app.route('/fullstack.html')
def fullstack():
    return send_from_directory(os.path.abspath(os.path.join(app.root_path, os.pardir)), 'fullstack.html')

@app.route('/mobile.html')
def mobile():
    return send_from_directory(os.path.abspath(os.path.join(app.root_path, os.pardir)), 'mobile.html')

@app.route('/ongoing.html')
def ongoing():
    return send_from_directory(os.path.abspath(os.path.join(app.root_path, os.pardir)), 'ongoing.html')

@app.route('/optimization.html')
def optimization():
    return send_from_directory(os.path.abspath(os.path.join(app.root_path, os.pardir)), 'optimization.html')

@app.route('/products.html')
def products():
    return send_from_directory(os.path.abspath(os.path.join(app.root_path, os.pardir)), 'products.html')

@app.route('/sap.html')
def sap():
    return send_from_directory(os.path.abspath(os.path.join(app.root_path, os.pardir)), 'sap.html')

@app.route('/services.html')
def services():
    return send_from_directory(os.path.abspath(os.path.join(app.root_path, os.pardir)), 'services.html')

@app.route('/training.html')
def training():
    return send_from_directory(os.path.abspath(os.path.join(app.root_path, os.pardir)), 'training.html')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        if not User.query.filter_by(username='admin').first():
            admin_user = User(username='admin', is_admin=True) # Set is_admin to True
            admin_user.set_password('adminpass')
            db.session.add(admin_user)
            db.session.commit()
        app.run(debug=True, port=5000)