from flask import Flask, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

GITHUB_USERNAME = "deepikapaneer"

@app.route('/')
def home():
    return jsonify({
        "message": "Deepika's DevOps Portfolio API",
        "github": f"https://github.com/{GITHUB_USERNAME}",
        "endpoints": ["/projects", "/skills", "/health"]
    })

@app.route('/health')
def health():
    return jsonify({"status": "ok"})

@app.route('/projects')
def projects():
    res = requests.get(f'https://api.github.com/users/{GITHUB_USERNAME}/repos')
    repos = res.json()
    return jsonify({
        "projects": [
            {
                "name": repo["name"],
                "description": repo["description"],
                "url": repo["html_url"],
                "stars": repo["stargazers_count"],
                "language": repo["language"]
            }
            for repo in repos
        ]
    })

@app.route('/skills')
def skills():
    return jsonify({
        "name": "Deepika Paneer Selvam",
        "role": "Aspiring DevOps & Cloud Engineer",
        "skills": [
            "Docker",
            "GitHub Actions",
            "Flask",
            "PostgreSQL",
            "Linux",
            "AWS",
            "CI/CD"
        ]
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)