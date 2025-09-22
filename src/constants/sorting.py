from enum import Enum

"""
AZ - alphabet order
ZA - reversed alphabet order
LOHI - ascending order (low to high)
HILO - descending order (high to low)
"""

class Sorting(Enum):
    AZ = "az"
    ZA = "za"
    LOHI = "lohi"
    HILO = "hilo"