#!/usr/bin/env python3
""" Implementation of the Server class """
import csv
from math import ceil
from typing import Any, Dict, List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Return a tuple containing a start index and an end index
    corresponding to the range of indexes to return in a list
    for those particular pagination parameters.

    Note: Page numbers are 1-indexed, i.e. the first page is page 1.
    """

    # Compute the start index (remember page numbers are 1-indexed)
    start = (page - 1) * page_size

    # Compute the end index
    end = start + page_size

    # Return the index range tuple
    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Use index_range to find the correct indexes to
        paginate the dataset correctly and return the
        appropriate page of the dataset (i.e. the correct list of rows).

        If the input arguments are out of range for the dataset,
        an empty list should be returned.
        """

        # Verify that both arguments are integers greater than 0
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0

        # Feed dataset
        dataset = self.dataset()

        # Compute the index range
        start, end = index_range(page, page_size)

        # Return [] if the index range is out of range
        total_pages = len(dataset)
        # if start > total_pages or end > total_pages + 1:
        if start > total_pages - 1:
            return []

        # Look for the appropriate page of the dataset
        if end <= total_pages - 1:
            page = dataset[start: end]
        else:
            page = dataset[start:]

        # Return the page
        return page

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """Call get_page and returns a dictionary
        containing the following key-value pairs:

            page_size: the length of the returned dataset page
            page: the current page number
            data: the dataset page (equivalent to return from previous task)
            next_page: number of the next page, None if no next page
            prev_page: number of the previous page, None if no previous page
            total_pages: the total number of pages in the dataset as an integer
        """

        # Get appropriate page
        returned_page = self.get_page(page, page_size)

        # Compute the total number of pages in tha dataset
        total_pages = ceil(len(self.__dataset) / page_size)

        # Define next and previous pages
        next_page = page + 1 if page < total_pages - 1 else None
        prev_page = page - 1 if page > 1 else None

        # Construct the Hypermedia dictionary
        hypermedia_dict = {
                'page_size': len(returned_page),
                'page': page,
                'data': returned_page,
                'next_page': next_page,
                'prev_page': prev_page,
                'total_pages': total_pages
        }

        # Return the Hypermedia dictionary
        return hypermedia_dict
