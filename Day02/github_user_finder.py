import requests

input_username = input("Enter a GitHub username: ")

try:
    response = requests.get(f"https://api.github.com/users/{input_username}")

    # Raises an HTTPError for 4xx and 5xx responses
    response.raise_for_status()

    data = response.json()

    print("Name ->", data["name"])
    print("Bio ->", data["bio"])
    print("Public Repos ->", data["public_repos"])
    print("Followers ->", data["followers"])
    print("Following ->", data["following"])

except requests.exceptions.HTTPError:
    print("User not found. Please check the username and try again.")

except requests.exceptions.ConnectionError:
    print("No internet connection.")

except requests.exceptions.Timeout:
    print("The request timed out.")

except requests.exceptions.RequestException as e:
    print("Something went wrong:", e)