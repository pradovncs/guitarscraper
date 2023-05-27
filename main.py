from scrapers import get_product_links, parse_products
from csv_utils import save_csv
from pathlib import Path
import logging
import time
import sys
import os

BASE_DIR = Path(__file__).parent
if os.path.exists(os.path.join(BASE_DIR, 'scraping.log')):
    os.remove(os.path.join(BASE_DIR, 'scraping.log'))

logging.basicConfig(filename='scraping.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.INFO)
console_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(console_formatter)
logging.getLogger().addHandler(console_handler)

def main():
    """
    Main function to run the scraping and CSV saving process.
    """
    try:
        start_time = time.time()

        logging.info('Getting Musicale product links.')
        musicale_products_url = get_product_links(page=1,
                                base_url='https://musicalle.com.br/cordas/guitarra?page=',
                                products_selector='div.main-products div.product-grid-item')

        logging.info('Getting Megasom product links.')
        megasom_product_urls = get_product_links(page=1,
                                base_url='https://www.megasom.com.br/cordas/guitarra?pg=',
                                products_selector='.product a.space-image')

        logging.info('Scrapping Musicale products.')
        musicale_products = []
        for prod_url in musicale_products_url:
            tmp = parse_products(url=prod_url,
                                 title_selector='h1',
                                 price_selector='.product-price',
                                 img_selector='img#image')
            musicale_products.append(tmp)
        save_csv(results=musicale_products, store='musicale')

        logging.info('Scrapping Megasom products.')
        megasom_products = []
        for prod_url in megasom_product_urls:
            tmp = parse_products(url=prod_url,
                                 title_selector="h1",
                                 price_selector=".preco-avista.precoAvista",
                                 img_selector=".zoom img")
            megasom_products.append(tmp)
        save_csv(results=megasom_products, store='megasom')

        total_time = time.time() - start_time
        logging.info(f'Total time scraping {len(megasom_products)+len(musicale_products)} products in seconds is: {total_time}')

    except Exception as e:
        logging.exception(f'An error occurred: {str(e)}')

if __name__ == "__main__":
    main()
