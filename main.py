import time
from scrapers import get_product_links, parse_products
from csv_utils import save_csv

def main():
    start_time = time.time()

    musicale_products_url = get_product_links(page=1,
                             base_url='https://musicalle.com.br/cordas/guitarra?page=',
                             products_selector='div.main-products div.product-grid-item')

    megasom_product_urls = get_product_links(page=1,
                             base_url='https://www.megasom.com.br/cordas/guitarra?pg=',
                             products_selector='.product a.space-image')

    musicale_products = []
    for prod_url in musicale_products_url:
        tmp = parse_products(url=prod_url,
                             title_selector='h1',
                             price_selector='.product-price',
                             img_selector='img#image')
        musicale_products.append(tmp)
    save_csv(results=musicale_products, store='musicale')

    megasom_products = []
    for prod_url in megasom_product_urls:
        tmp = parse_products(url=prod_url,
                             title_selector="h1",
                             price_selector=".preco-avista.precoAvista",
                             img_selector=".zoom img")
        megasom_products.append(tmp)
    save_csv(results=megasom_products, store='megasom')
    
    total_time = time.time() - start_time
    print(f'Total time scraping {len(megasom_products)+len(musicale_products)} products in seconds is: {total_time}')

if __name__ == "__main__":
    main()
