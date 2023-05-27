import csv

def save_csv(results: dict, store: str):
    keys = results[0].keys()

    with open(f'{store}_products.csv', 'w', newline='') as f:
        dict_writer = csv.DictWriter(f, keys)
        dict_writer.writeheader()
        dict_writer.writerows(results)
