from flask import Blueprint, request, jsonify
from services.github_service import get_github_data

github_bp = Blueprint('github_bp', __name__)

@github_bp.route('/compare', methods=['GET'])
def compare_devs():
    dev1 = request.args.get('dev1')
    dev2 = request.args.get('dev2')

    if not dev1 or not dev2:
        return jsonify({"error": "É necessário fornecer dois usuários!"}), 400

    data1 = get_github_data(dev1)
    data2 = get_github_data(dev2)

    if not data1 or not data2:
        return jsonify({"error": "Um ou ambos os usuários não foram encontrados."}), 404

    winner = data1 if data1.score > data2.score else data2
    data1_dict = data1.to_dict()
    data2_dict = data2.to_dict()
    
    data1_dict["winner"] = data1 == winner
    data2_dict["winner"] = data2 == winner

    return jsonify({"dev1": data1_dict, "dev2": data2_dict, "winner": winner.username})
