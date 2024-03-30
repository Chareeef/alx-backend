#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""
import csv
from typing import Dict, List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()

            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Take an `index` and `page_size` arguments,
        and return the following dictionary:
                - index: the current start index of the return page,
                         e.g: the index of the first item in the current page

                - next_index: the next index to query with,
                              e.g: the index of the first item after
                              the last item on the current page

                - page_size: the current page size

                - data: the actual page of the dataset
        """

        # Get the indexed dataset
        indexed_dataset = self.__indexed_dataset

        # Initial total items
        initial_total = len(self.__dataset)

        # Verify that index is in valid range and valid page_size
        assert type(index) == int and type(page_size) == int
        assert index >= 0 and index < initial_total and page_size > 0

        # Get actual data
        data = []
        i = index

        # Loop through the dataset until the actual data is filled
        while len(data) < page_size and i < initial_total:
            # Ensure current data at index `i` was not deleted
            new_data = indexed_dataset.get(i)

            if new_data:
                data.append(new_data)

            # Increment `i`
            i += 1

        # Since data is now filled, the next_index is then `i` or None
        next_index = i if i < initial_total else None

        # Construct our dictionary
        hypermedia_del_dict = {
                'index': index,
                'data': data,
                'page_size': page_size,
                'next_index': next_index
        }

        # Return the dictionary
        return hypermedia_del_dict
