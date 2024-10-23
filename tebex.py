import requests

API_URL = "https://headless.tebex.io/api/accounts/{token}/packages"
TOKEN = "jint-4f73b83e822f01d33c23f33aee681a9a15844329"

def fetch_latest_packages():
    response = requests.get(API_URL.replace("{token}", TOKEN))
    if response.status_code == 200:
        return response.json()['data'][:8]
    else:
        raise Exception(f"Failed to fetch packages: {response.status_code}")

def main():
    packages = fetch_latest_packages()
    for package in packages:
        print(f"Package: {package['name']} - Price: {package['total_price']} {package['currency']}")

if __name__ == '__main__':
    main()
