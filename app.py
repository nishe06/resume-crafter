from flask import Flask, render_template, request, redirect, url_for, session, jsonify, flash
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import openai
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure key in production

# Database setup
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def __init__(self, username, email, password_hash, **kwargs):
        super().__init__(**kwargs)
        self.username = username
        self.email = email
        self.password_hash = password_hash

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

openai.api_key = "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"  # Set this in your environment

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/auth')
def auth():
    return render_template('auth.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        # Check if user exists
        user_by_username = User.query.filter_by(username=username).first()
        user_by_email = User.query.filter_by(email=email).first()
        if user_by_username or user_by_email:
            flash('An account with this username or email already exists. Please sign in instead.')
            return render_template('signup.html')
        # Hash password and create user
        password_hash = bcrypt.generate_password_hash(password).decode('utf-8')
        new_user = User(username=username, email=email, password_hash=password_hash)
        db.session.add(new_user)
        db.session.commit()
        flash('Account created! Please sign in.')
        return redirect(url_for('signin'))
    return render_template('signup.html')

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        if not user:
            flash('No account found with this username. Please sign up instead.')
        elif user.check_password(password):
            session['user_id'] = user.id
            return redirect(url_for('user_type'))
        else:
            flash('Invalid password. Please try again or sign up if you don\'t have an account.')
    return render_template('signin.html')

@app.route('/user-type', methods=['GET', 'POST'])
def user_type():
    if request.method == 'POST':
        user_type = request.form.get('user_type')
        session['user_type'] = user_type
        return redirect(url_for('dashboard'))
    return render_template('user_type.html')

@app.route('/dashboard')
def dashboard():
    user_type = session.get('user_type', 'student')
    return render_template('dashboard.html', user_type=user_type)

@app.route('/generate_resume', methods=['POST'])
def generate_resume():
    data = request.get_json()
    user_input = data.get('input', '')
    user_type = session.get('user_type', 'student')

    # Call OpenAI API
    response = openai.chat.completions.create(
        model="gpt-4o-mini-2024-07-18",  # or "gpt-4" if you have access
        messages=[
            {"role": "system", "content": (
                f"You are a helpful assistant that creates professional resume templates. "
                f"The user has selected the '{user_type}' category. "
                "Only generate resumes for this category. "
                "If the user's prompt asks for a resume for a different category (e.g., a student asking for a professional resume), respond with: "
                f"'You have selected the {user_type} category. Please go to the correct category page to generate a resume for a different background.' "
                "If the user's input is completely meaningless (e.g., random letters, numbers, or empty), respond with: "
                "'Please provide a more relevant background for your resume.' "
                "If the input is short but plausible (e.g., 'college student'), generate a basic resume template for that background, but only if it matches the selected category. "
                "Otherwise, generate a resume template tailored to the user's input, but only for the selected category."
            )},
            {"role": "user", "content": f"Create a resume template for: {user_input}"}
        ],
        max_tokens=500
    )
    
    ai_resume = response.choices[0].message.content if response.choices[0].message.content else ""
    formatted_resume = ai_resume.replace('\n', '<br>')
    return jsonify({'resume': formatted_resume})


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='0.0.0.0', port=5001) 