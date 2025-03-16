from flask import Flask
from flask_cors import CORS
from routes.github_routes import github_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(github_bp)

if __name__ == '__main__':
    app.run(debug=True)
