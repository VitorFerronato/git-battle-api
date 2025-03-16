class Developer:
    """Represents a github developer"""

    def __init__(self, username: str, avatar: str, followers: int, public_repos: int, total_stars: int, total_forks: int):
        self.username = username
        self.avatar = avatar
        self.followers = followers
        self.public_repos = public_repos
        self.total_stars = total_stars
        self.total_forks = total_forks
        self.score = self.calculate_score()

    def calculate_score(self) -> float:
        return (self.followers * 2) + (self.public_repos * 1.5) + (self.total_stars * 2) + (self.total_forks * 1)

    def to_dict(self):
        return {
            "username": self.username,
            "avatar": self.avatar,
            "followers": self.followers,
            "public_repos": self.public_repos,
            "total_stars": self.total_stars,
            "total_forks": self.total_forks,
            "score": self.score
        }
