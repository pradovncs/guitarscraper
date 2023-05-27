import csv

def save_csv(results: list[dict], store: str):
    """
    Saves a list of dictionaries to a CSV file.

    Args:
        results (list[dict]): The list of dictionaries to be saved as CSV.
        store (str): The name of the store.

    Returns:
        None
    """
    keys = results[0].keys()

    with open(f'{store}_products.csv', 'w', newline='') as f:
        dict_writer = csv.DictWriter(f, keys)
        dict_writer.writeheader()
        dict_writer.writerows(results)
