import requests

def main():
    res = requests.get("http://data.fixer.io/api/latest?access_key=e966f003d2d4f31a7288158320c9bd05&symbols=USD,COP")
    if res.status_code != 200:
        raise Exception("ERROR: API request unsuccessful.")
    data = res.json()
    print(data)

if __name__ == "__main__":
    main()
