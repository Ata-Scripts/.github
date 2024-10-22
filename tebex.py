import requests
import datetime

API_URL = 'https://plugin.tebex.io/packages'
README_TEMPLATE = """
# Latest Products and Packages

This is an automatically updated list of the latest products and packages from our [Tebex Store](https://your-store.tebex.io).

## Latest Releases

| Product Name  | Description | Price | Release Date |
| ------------- | ----------- | ----- | ------------ |
{products_list}

> Note: This list is updated based on the latest releases from our store.

---

For more details, visit our [Tebex Store](https://ata.tebex.io).
"""

def fetch_latest_products():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()['data'][:8]
    else:
        raise Exception(f"Failed to fetch data: {response.status_code}")

def generate_markdown(products):
    product_lines = []
    for product in products:
        name = product['name']
        description = product['description'][:50] + '...' if len(product['description']) > 50 else product['description']
        price = product['price']['formatted']
        release_date = datetime.datetime.fromtimestamp(product['created_at']).strftime('%Y-%m-%d')
        link = f"https://ata.tebex.io/package/{product['id']}"
        product_lines.append(f"| [{name}]({link}) | {description} | {price} | {release_date} |")
    return "\n".join(product_lines)

def update_readme(products_list):
    markdown_content = README_TEMPLATE.format(products_list=products_list)
    with open('README.md', 'w', encoding='utf-8') as readme_file:
        readme_file.write(markdown_content)

def main():
    products = fetch_latest_products()
    products_list = generate_markdown(products)
    update_readme(products_list)

if __name__ == '__main__':
    main()
