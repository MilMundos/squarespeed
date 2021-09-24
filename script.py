# Interact with the Squarespace API to get info about new orders

import os
from squarespace_commerce import Squarespace


# This API Key is read-only for Inventory, Orders and Transactions
def main():
    order = Squarespace(os.getenv("SQUARESPACE_API_KEY"))
    print(order.get_orders())


if __name__ == "__main__":
    main()
