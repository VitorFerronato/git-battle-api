from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

GITHUB_API_URL = "https://api.github.com/users/"

def get_github_data(username):
    """Busca dados do usuário no GitHub"""
    response = requests.get(f"{GITHUB_API_URL}{username}")
    
    if response.status_code == 200:
        user_data = response.json()
        
        repos_response = requests.get(user_data['repos_url'])
        repos = repos_response.json() if repos_response.status_code == 200 else []
        
        # Contar total de estrelas e forks nos repositórios do usuário
        total_stars = sum(repo['stargazers_count'] for repo in repos)
        total_forks = sum(repo['forks_count'] for repo in repos)

        return {
            "username": user_data["login"],
            "avatar": user_data["avatar_url"],
            "followers": user_data["followers"],
            "public_repos": user_data["public_repos"],
            "total_stars": total_stars,
            "total_forks": total_forks
        }
    return None

@app.route('/compare', methods=['GET'])
def compare_devs():
    """Rota que compara dois desenvolvedores"""
    dev1 = request.args.get('dev1')
    dev2 = request.args.get('dev2')
    
    print('dev1',dev1)
    print('dev2',dev2)
    
    if not dev1 or not dev2:
        return jsonify({"error": "É necessário fornecer dois usuários!"}), 400

    data1 = get_github_data(dev1)
    data2 = get_github_data(dev2)
    
    print('data1',data1)
    print('data2',data2)


    if not data1 or not data2:
        return jsonify({"error": "Usuário(s) não encontrado(s)!"}), 404

    # Definir a pontuação de cada dev com base nas métricas
    data1["score"] = (data1["followers"] * 2) + (data1["public_repos"] * 1.5) + (data1["total_stars"] * 2) + (data1["total_forks"] * 1)
    data2["score"] = (data2["followers"] * 2) + (data2["public_repos"] * 1.5) + (data2["total_stars"] * 2) + (data2["total_forks"] * 1)

    winner = data1 if data1["score"] > data2["score"] else data2
    data1["winner"] = data1 == winner
    data2["winner"] = data2 == winner

    return jsonify({"dev1": data1, "dev2": data2, "winner": winner["username"]})

if __name__ == '__main__':
    app.run(debug=True)
