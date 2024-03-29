#!/usr/bin/env python3
""" Implementation of the index_range function """
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ Return a tuple containing a start index and an end index
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
