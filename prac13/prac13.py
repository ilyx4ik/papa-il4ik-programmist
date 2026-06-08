import urllib.request
import json

def fetch_github_user(username):
    url = f"https://api.github.com/users/{username}"
    req = urllib.request.Request(url, headers={'User-Agent': 'Python-Script'})
    with urllib.request.urlopen(req) as response:
        return json.loads(response.read().decode())

def fetch_github_repos(username):
    url = f"https://api.github.com/users/{username}/repos"
    req = urllib.request.Request(url, headers={'User-Agent': 'Python-Script'})
    with urllib.request.urlopen(req) as response:
        return json.loads(response.read().decode())

def main():
    username = "octocat"
    
    user_data = fetch_github_user(username)
    print(f"{'Поле':<15} | {'Значення'}")
    print("-" * 30)
    print(f"{'Login':<15} | {user_data.get('login')}")
    print(f"{'ID':<15} | {user_data.get('id')}")
    print(f"{'Public Repos':<15} | {user_data.get('public_repos')}")
    
    print("\n")
    
    repos = fetch_github_repos(username)
    print(f"{'Назва репозиторія':<20} | {'Watchers':<8} | {'Issues':<6} | {'Forks':<6}")
    print("-" * 50)
    
    max_forks_repo = None
    max_forks = -1
    
    for repo in repos:
        name = repo.get('name')
        watchers = repo.get('watchers_count', 0)
        issues = repo.get('open_issues_count', 0)
        forks = repo.get('forks_count', 0)
        print(f"{name:<20} | {watchers:<8} | {issues:<6} | {forks:<6}")
        
        if forks > max_forks:
            max_forks = forks
            max_forks_repo = repo
            
    if max_forks_repo:
        print(f"\nРепозиторій з найбільшою кількістю форків: {max_forks_repo.get('name')} ({max_forks} форків)")

if __name__ == "__main__":
    main()