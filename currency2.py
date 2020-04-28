import requests

def main():
    base = input("First Currency: ")
    other = input("Second Currency: ")
    res = requests.get("http://data.fixer.io/api/latest",
                       params={"access_key":"e966f003d2d4f31a7288158320c9bd05",
                               "symbols": base +", "+other})
    if res.status_code != 200:
        raise Exception("ERROR: API request unsuccessful.")
    data = res.json()
    rate = data["rates"][other]
    print(f"1 EUR is equal to {rate} {other}")

if __name__ == "__main__":
    main()
