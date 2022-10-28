from typing import List


def split_product_links_into_batches(links: List[str], number_of_links_per_batch: int) -> List:
    return [links[i:i + number_of_links_per_batch] for i in
            range(0, len(links), number_of_links_per_batch)]
