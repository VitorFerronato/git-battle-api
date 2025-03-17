from flask import Blueprint, jsonify, request
from services import get_github_data

github_bp = Blueprint('github', __name__)

@github_bp.route('/compare', methods=['GET'])
def compare_devs():
    dev1 = request.args.get("dev1")
    dev2 = request.args.get("dev2")

    if not dev1 or not dev2:
        return jsonify({"error": "Dois usuários são necessários"}), 400

    data1 = get_github_data(dev1)
    data2 = get_github_data(dev2)

    if data1 is None or data2 is None:
        return jsonify({"error": "Usuário(s) não encontrado(s)"}), 404

    # 🔥 Aqui estava o erro: data1 e data2 estavam como dict, agora garantimos que sejam objetos
    if isinstance(data1, dict) or isinstance(data2, dict):
        return jsonify({"error": "Erro ao buscar dados do GitHub"}), 500

    winner = data1 if data1.score > data2.score else data2

    return jsonify({
        "dev1": data1.to_dict(),
        "dev2": data2.to_dict(),
        "winner": winner.to_dict()
    })
