import sqlite3
from models import Orders

ORDERS = [
    {
      "timestamp": 1684513128264,
      "metalId": 1,
      "sizeId": 1,
      "styleId": 1,
      "typeId": 1,
      "id": 1
    },
    {
      "timestamp": 1684513184661,
      "metalId": 1,
      "sizeId": 1,
      "styleId": 1,
      "typeId": 2,
      "id": 2
    },
    {
      "timestamp": 1684513263009,
      "metalId": 1,
      "sizeId": 1,
      "styleId": 1,
      "typeId": 3,
      "id": 3
    },
    {
      "timestamp": 1684513509513,
      "metalId": 2,
      "sizeId": 2,
      "styleId": 2,
      "typeId": 1,
      "id": 4
    },
    {
      "timestamp": 1684513527521,
      "metalId": 3,
      "sizeId": 3,
      "styleId": 3,
      "typeId": 1,
      "id": 5
    },
    {
      "timestamp": 1684513790680,
      "metalId": 5,
      "sizeId": 5,
      "styleId": 3,
      "typeId": 2,
      "id": 6
    },
    {
      "timestamp": 1684513830825,
      "metalId": 1,
      "sizeId": 1,
      "styleId": 2,
      "typeId": 3,
      "id": 7
    }
  ]

def get_all_orders():
    """GET all"""
    # Open a connection to the database
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            o.id,
            o.timestamp,
            o.metal_id,
            o.size_id,
            o.style_id,
            o.type_id
        FROM Orders o
        """)

        # Initialize an empty list to hold all representations
        all_orders = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # class above.
            order = Orders(row['id'], row['timestamp'], row['metal_id'],
                            row['size_id'], row['style_id'],
                            row['type_id'])

            all_orders.append(order.__dict__)

    return all_orders

def get_single_order(id):
    """Get a single dictionary from the list"""
    # Variable to hold the found order, if it exists
    requested_order = None

    # Iterate the ORDERS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for order in ORDERS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if order["id"] == id:
            requested_order = order

    return requested_order

def create_order(order):
    """Function to add order via POST request"""

    # Get the id value of the last order in the list
    max_id = ORDERS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the order dictionary
    order["id"] = new_id

    # Add the order dictionary to the list
    ORDERS.append(order)

    # Return the dictionary with `id` property added
    return order

def delete_order(id):
    """Delete order from list"""
    # Initial -1 value for order index, in case one isn't found
    order_index = -1

    # Set status of delete to None by default
    delete_status = None

    # Iterate the ORDERS list, but use enumerate() so that you
    # can access the index value of each item
    for index, order in enumerate(ORDERS):
        if order["id"] == id:
            # Found the order. Store the current index.
            order_index = index

    # If the order was found, use pop(int) to remove it from list
    if order_index >= 0:
        ORDERS.pop(order_index)
        delete_status = "success"

    return delete_status

def update_order(id, new_order):
    """Update an order in the list"""
    # Iterate the ORDERS list, but use enumerate() so that
    # you can access the index value of each item.
    update_status = None

    for index, order in enumerate(ORDERS):
        if order["id"] == id:
            # Found the order. Update the value.
            ORDERS[index] = new_order
            update_status = "success"
            break
    return update_status
