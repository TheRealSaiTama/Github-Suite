import requests
import json
from datetime import datetime, timedelta
import plotly.graph_objects as go
import numpy as np
import subprocess


def fetch_repositories(username, token):
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json',
    }

    url = f'https://api.github.com/users/{username}/repos'
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    return []

def fetch_commits(username, repo, token):
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json',
    }

    url = f'https://api.github.com/repos/{username}/{repo}/commits'
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    return []

def fetch_pushes(username, repo, token):
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json',
    }

    url = f'https://api.github.com/repos/{username}/{repo}/events'
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        pushes = [event for event in response.json() if event['type'] == 'PushEvent']
        return pushes
    return []

def fetch_contributions(username, token):
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json',
    }

    today = datetime.now()
    last_year = today - timedelta(days=365)

    contributions = {}
    for day in range(365):
        date = (last_year + timedelta(days=day)).strftime('%Y-%m-%d')
        contributions[date] = 0

    url = f'https://api.github.com/users/{username}/events'
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        events = response.json()
        for event in events:
            event_date = event['created_at'][:10]
            if event_date in contributions:
                contributions[event_date] += 1

    return contributions

def format_contributions(contributions):
    formatted_data = []
    for date, count in contributions.items():
        formatted_data.append((date, count))
    return formatted_data

def generate_interactive_heatmap(formatted_data, username):
    dates = [data[0] for data in formatted_data]
    counts = [data[1] for data in formatted_data]

    dates = [datetime.strptime(date, '%Y-%m-%d') for date in dates]
    min_date = min(dates)
    max_date = max(dates)

    date_range = (max_date - min_date).days + 1
    heatmap_data = np.zeros((7, date_range // 7 + 1))

    for date, count in zip(dates, counts):
        week = (date - min_date).days // 7
        day_of_week = date.weekday()
        heatmap_data[day_of_week, week] = count

    fig = go.Figure(data=go.Heatmap(
        z=heatmap_data,
        x=[(min_date + timedelta(days=i)).strftime('%Y-%m-%d') for i in range(0, date_range, 7)],
        y=['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
        colorscale='YlGn'
    ))
    fig.update_layout(
        title=f'GitHub Contributions Heatmap for {username}',
        xaxis_title='Date',
        yaxis_title='Day of Week'
    )
    fig.show()

def check_dependencies():
    result = subprocess.run(['safety', 'check', '--json'], capture_output=True, text=True)
    if result.returncode != 0 or not result.stdout:
        print("Error or no vulnerabilities found.")
        return []

    try:
        vulnerabilities = json.loads(result.stdout)
    except json.JSONDecodeError:
        print("Failed to parse JSON output from safety.")
        return []

    return vulnerabilities

def fetch_activity(username, token):
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json',
    }

    url = f'https://api.github.com/users/{username}/events/public'
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    return []

def generate_activity_dashboard(activity_data, username):
    event_types = {}

    for event in activity_data:
        event_type = event['type']
        if event_type not in event_types:
            event_types[event_type] = 0
        event_types[event_type] += 1

    event_labels = list(event_types.keys())
    event_counts = list(event_types.values())

    fig = go.Figure(data=[go.Bar(x=event_labels, y=event_counts)])
    fig.update_layout(
        title=f'GitHub Activity Dashboard for {username}',
        xaxis_title='Event Type',
        yaxis_title='Count'
    )
    fig.show()

def terminal_menu():
    while True:
        print("Choose an option:")
        print("1. Generate GitHub Contributions Heatmap")
        print("2. Check Dependencies")
        print("3. Generate GitHub Activity Dashboard")
        print("4. List User's Repositories")
        print("5. Show All Commits for Each Repository")
        print("6. Show All Pushes for Each Repository")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            username = input("Enter GitHub username: ")
            token = input("Enter GitHub token: ")
            contributions = fetch_contributions(username, token)
            formatted_data = format_contributions(contributions)
            generate_interactive_heatmap(formatted_data, username)
        elif choice == '2':
            vulnerabilities = check_dependencies()
            if vulnerabilities:
                print("Vulnerabilities found:")
                for vulnerability in vulnerabilities:
                    print(f"- {vulnerability['name']} ({vulnerability['version']}): {vulnerability['advisory']}")
            else:
                print("No vulnerabilities found.")
        elif choice == '3':
            username = input("Enter GitHub username: ")
            token = input("Enter GitHub token: ")
            activity_data = fetch_activity(username, token)
            generate_activity_dashboard(activity_data, username)
        elif choice == '4':
            username = input("Enter GitHub username: ")
            token = input("Enter GitHub token: ")
            repos = fetch_repositories(username, token)
            if repos:
                print("Repositories found:")
                for repo in repos:
                    print(f"- {repo['name']}")
            else:
                print("No repositories found.")
        elif choice == '5':
            username = input("Enter GitHub username: ")
            token = input("Enter GitHub token: ")
            repos = fetch_repositories(username, token)
            for repo in repos:
                commits = fetch_commits(username, repo['name'], token)
                print(f"Commits for {repo['name']}:")
                for commit in commits:
                    print(f"- {commit['commit']['message']} by {commit['commit']['author']['name']}")
        elif choice == '6':
            username = input("Enter GitHub username: ")
            token = input("Enter GitHub token: ")
            repos = fetch_repositories(username, token)
            for repo in repos:
                pushes = fetch_pushes(username, repo['name'], token)
                print(f"Pushes for {repo['name']}:")
                for push in pushes:
                    print(f"- Push by {push['actor']['login']} with {len(push['payload']['commits'])} commits")
        elif choice == '7':
            break
        else:
            print("Invalid choice, please try again.")

terminal_menu()