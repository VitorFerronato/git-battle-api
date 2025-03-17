import requests
from models.developer import Developer

def get_github_data(username: str):
    response = requests.get(f"https://api.github.com/users/{username}")

    if response.status_code == 404:
        return None

    if response.status_code != 200:
        return {"error": "Erro ao buscar dados do GitHub."}

    user_data = response.json()

    repos_response = requests.get(user_data.get('repos_url', ''))
    repos = repos_response.json() if repos_response.status_code == 200 else []

    total_stars = sum(repo.get('stargazers_count', 0) for repo in repos)
    total_forks = sum(repo.get('forks_count', 0) for repo in repos)

    return Developer(
        username=user_data["login"],
        avatar=user_data["avatar_url"],
        followers=user_data["followers"],
        public_repos=user_data["public_repos"],
        total_stars=total_stars,
        total_forks=total_forks
    )
