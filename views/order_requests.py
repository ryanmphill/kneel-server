ORDERS = [
    {
      "timestamp": 1684513128264,
      "orderId": 1,
      "sizeId": 1,
      "styleId": 1,
      "typeId": 1,
      "id": 1
    },
    {
      "timestamp": 1684513184661,
      "orderId": 1,
      "sizeId": 1,
      "styleId": 1,
      "typeId": 2,
      "id": 2
    },
    {
      "timestamp": 1684513263009,
      "orderId": 1,
      "sizeId": 1,
      "styleId": 1,
      "typeId": 3,
      "id": 3
    },
    {
      "timestamp": 1684513509513,
      "orderId": 2,
      "sizeId": 2,
      "styleId": 2,
      "typeId": 1,
      "id": 4
    },
    {
      "timestamp": 1684513527521,
      "orderId": 3,
      "sizeId": 3,
      "styleId": 3,
      "typeId": 1,
      "id": 5
    },
    {
      "timestamp": 1684513790680,
      "orderId": 5,
      "sizeId": 5,
      "styleId": 3,
      "typeId": 2,
      "id": 6
    },
    {
      "timestamp": 1684513830825,
      "orderId": 1,
      "sizeId": 1,
      "styleId": 2,
      "typeId": 3,
      "id": 7
    }
  ]

def get_all_orders():
    """Return list of all orders"""
    return ORDERS

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
