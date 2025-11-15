# Resume Crafter

## Description

Resume Crafter is an AI-powered web application that helps users create professional resumes tailored to their career stage. The platform offers a personalized resume generation experience based on user type (Student, Intern, or Professional) and allows users to edit and download their resumes as PDFs.

### Key Features

- **User Authentication**: Secure sign-up and sign-in system with password hashing
- **User Type Selection**: Choose between Student, Intern, or Professional categories
- **AI-Powered Resume Generation**: Generate professional resume templates using OpenAI's GPT-4o-mini model
- **Resume Editing**: Edit generated resumes directly in the browser
- **PDF Download**: Export resumes as PDF files for printing or sharing
- **Category-Specific Templates**: Resumes are customized based on the selected user type
- **Input Validation**: Error handling for invalid or irrelevant inputs

## Technologies Used

### Backend
- **Python 3.12**: Programming language
- **Flask 3.1.1**: Web framework for building the application
- **Flask-SQLAlchemy 3.1.1**: ORM for database management
- **Flask-Bcrypt 1.0.1**: Password hashing and security
- **SQLite**: Lightweight database for user data storage
- **OpenAI API 1.93.2**: GPT-4o-mini model for AI-powered resume generation

### Frontend
- **HTML5**: Markup language for page structure
- **CSS3**: Styling with responsive design and modern UI
- **JavaScript**: Client-side interactivity and API calls
- **Jinja2**: Template engine (included with Flask)

### Development Tools
- **Virtual Environment**: Python virtual environment for dependency management
- **Debug Mode**: Flask debug mode for development

## Installation & Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set up your OpenAI API key in `app.py` or as an environment variable

3. Run the application:
```bash
python app.py
```

4. Access the application at `http://localhost:5001`

## Project Structure

```
resume-crafter-yt/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── templates/          # HTML templates
│   ├── welcome.html
│   ├── signup.html
│   ├── signin.html
│   ├── user_type.html
│   └── dashboard.html
├── static/            # Static files
│   └── style.css
└── instance/          # Database files
    └── users.db
```

## Usage

1. **Sign Up**: Create a new account with username, email, and password
2. **Sign In**: Log in with your credentials
3. **Select User Type**: Choose Student, Intern, or Professional
4. **Generate Resume**: Enter your background, skills, and goals
5. **Edit & Download**: Customize your resume and download as PDF

## Security Features

- Password hashing using bcrypt
- Session management for user authentication
- Input validation and error handling
- Secure database storage

