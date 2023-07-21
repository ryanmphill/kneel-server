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
    """Get a single order from database"""
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        single_order_response = None

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            o.id,
            o.timestamp,
            o.metal_id,
            o.size_id,
            o.style_id,
            o.type_id
        FROM Orders o
        WHERE o.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        if data is not None:
            # Create an order instance from the current row
            order = Orders(data['id'], data['timestamp'], data['metal_id'],
                                data['size_id'], data['style_id'],
                                data['type_id'])
            single_order_response = order.__dict__

        return single_order_response

def create_order(new_order):
    """Insert new order into database Table"""
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Orders
            ( timestamp, metal_id, size_id, style_id, type_id )
        VALUES
            ( ?, ?, ?, ?, ?);
        """, (new_order['timestamp'], new_order['metal_id'],
              new_order['size_id'], new_order['style_id'],
              new_order['type_id'], ))

        # The `lastrowid` property on the cursor will return
        # the primary key of the last thing that got added to
        # the database.
        id = db_cursor.lastrowid

        # Add the `id` property to the order dictionary that
        # was sent by the client so that the client sees the
        # primary key in the response.
        new_order['id'] = id


    return new_order

def delete_order(id):
    """Delete order from database"""
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM Orders
        WHERE id = ?
        """, (id, ))
        # Were any rows affected?
        # Did the client send an `id` that exists?
        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        # Forces 404 response by main module
        result = False
    else:
        # Forces 204 response by main module
        result = True

    return result

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
