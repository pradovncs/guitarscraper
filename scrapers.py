from requests_html import HTMLSession

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
}

s = HTMLSession()
s.headers = headers

def get_product_links(page:str, base_url:str, products_selector:str):
    links = []
    while True:
        r = s.get(f"{base_url}{page}")
        products = r.html.find(products_selector)
        if not products:
            break
        for item in products:
            links.append(item.find("a", first=True).attrs["href"])
        page += 1
    return links

def parse_products(url: str, title_selector: str, price_selector: str, img_selector: str):
    r = s.get(url)
    try:
        title_element = r.html.find(title_selector, first=True)
        title = title_element.text.strip() if title_element else None
    except AttributeError:
        title = None

    try:
        price_element = r.html.find(price_selector, first=True)
        price = price_element.text.strip().replace('.', '').replace(',', '.').replace('R$', '') if price_element else None
    except AttributeError:
        price = None

    try:
        img_element = r.html.find(img_selector, first=True)
        img = img_element.attrs["src"] if img_element else None
    except AttributeError:
        img = None
    except:
        img = r.html.find(img_selector, first=True).attrs.get("data-src") if img_element else None

    product = {
        "title": title,
        "price": price,
        "img": img,
    }
    return product
