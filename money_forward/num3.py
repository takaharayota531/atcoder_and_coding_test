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
    next_destination = data.get("goto")

    while True:
        if next_destination == " put_the_bag":
            print(next_destination + ": in the trash")
            break
        elif next_destination == "changed_my_mind":
            print("Oops, the kidnapper changed their mind. Test case failed.")
            break
        else:
            print(next_destination)
            next_destination = get_next_destination(next_destination)

if __name__ == "__main__":
    main()
