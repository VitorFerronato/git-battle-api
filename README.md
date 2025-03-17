# Git Battle API

<div style="display:flex;">
  <img align="center" alt="vuejs" src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue" />
  <img align="center" alt="vuejs" src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" />
</div>

## 💻 The project 
This is an API built with Flask that allows you to compare two GitHub developers based on some criteria, such as number of followers, public repositories, stars, and forks. The API returns the data for these developers and indicates which one is the "winner" based on the score calculated from these criteria.

## 🚀 Technologies Used
- **Python**
- **Flask** - Python web framework
- **Flask-CORS** - Allows the API to be accessed from different sources
- **Requests** - Library for making HTTP requests
- **GitHub API** - To fetch user data from GitHub
- **Gunicorn** - WSGI server to run the application in production

## 🛠 How to run the project

### Prerequisites:
- Python 3.x
- pip 

Clone the repository:
```bash
git clone https://github.com/VitorFerronato/git-battle-api.git
cd git-battle-api
```

Create a virtual environment (optional, but recommended):
```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

Install the dependences:
```bash
pip install -r requirements.txt
```

Run
```bash
python app.py
```

### 🌐 API URL
https://git-battle-api.onrender.com




