import requests
response = requests.get('https://official-joke-api.appspot.com/random_joke')
data = response.json()
while True:
    print("😂 Joke of the Day")
    print(data['setup'])
    print(data['punchline'])
    print("Do you want to see another joke? (y/n)")
    response = requests.get('https://official-joke-api.appspot.com/random_joke')
    data = response.json()
    choice = input().lower()
    if choice == 'n':
        print("Thank you for using the Joke of the Day app!")
        break
    elif choice != 'y':
        print("Invalid input. Please enter 'y' or 'n'.")