import requests
import sys

TOKEN = sys.argv[1]

def get_next_destination(destination):
    url = "https://challenge-server.code-check.io/api/kidnapper/deliver"
    params = {
        "token": TOKEN,
        "to": destination
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data.get("goto")

def main():
    url = "https://challenge-server.code-check.io/api/kidnapper/start"
    params = {
        "token": TOKEN
    }
    response = requests.get(url, params=params)
    data = response.json()
    next_destination = []
    next_destination.append(data.get("goto"))
    while True:
        if next_destination[-1] is not None:
            next_destination.append(get_next_destination(next_destination[-1]))
        else:
            print(next_destination[-2])
            break
            

if __name__ == "__main__":
    main()

