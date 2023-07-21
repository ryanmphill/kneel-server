import sqlite3
from models import Orders, Metals, Sizes, Styles, Types

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
            o.type_id,
            m.metal,
            m.price metal_price,
            sz.carets,
            sz.price size_price,
            st.style,
            st.price style_price,
            t.name type_name,
            t.price_multiplier
        FROM Orders o
        JOIN Metals m ON m.id = o.metal_id
        JOIN Sizes sz ON sz.id = o.size_id
        JOIN Styles st ON st.id = o.style_id
        JOIN Types t ON t.id = o.type_id
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

            # Create a Metal instance from the current row
            metal = Metals(row['metal_id'], row['metal'], row['metal_price'])

            # Create a Size instance from the current row
            size = Sizes(row['size_id'], row['carets'], row['size_price'])

            # Create a Style instance from the current row
            style = Styles(row['style_id'], row['style'], row['style_price'])

             # Create a Type instance from the current row
            type = Types(row['type_id'], row['type_name'], row['price_multiplier'])

            # Add the dictionary representation of the foreign dictionaries to the order
            order.metal = metal.__dict__
            order.size = size.__dict__
            order.style = style.__dict__
            order.type = type.__dict__

            # Add the dictionary representation to the orders list
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
            o.type_id,
            m.metal,
            m.price metal_price,
            sz.carets,
            sz.price size_price,
            st.style,
            st.price style_price,
            t.name type_name,
            t.price_multiplier
        FROM Orders o
        JOIN Metals m ON m.id = o.metal_id
        JOIN Sizes sz ON sz.id = o.size_id
        JOIN Styles st ON st.id = o.style_id
        JOIN Types t ON t.id = o.type_id
        WHERE o.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        if data is not None:
            # Create an order instance from the current row
            order = Orders(data['id'], data['timestamp'], data['metal_id'],
                                data['size_id'], data['style_id'],
                                data['type_id'])

            # Create a Metal instance from the current row
            metal = Metals(data['metal_id'], data['metal'], data['metal_price'])

            # Create a Size instance from the current row
            size = Sizes(data['size_id'], data['carets'], data['size_price'])

            # Create a Style instance from the current row
            style = Styles(data['style_id'], data['style'], data['style_price'])

            # Create a Type instance from the current row
            type = Types(data['type_id'], data['type_name'], data['price_multiplier'])

            # Add the dictionary representation of the foreign dictionaries to the order
            order.metal = metal.__dict__
            order.size = size.__dict__
            order.style = style.__dict__
            order.type = type.__dict__

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
    """Make an update to the order row"""
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Orders
            SET
                timestamp = ?,
                metal_id = ?,
                size_id = ?,
                style_id = ?,
                type_id = ?
        WHERE id = ?
        """, (new_order['timestamp'], new_order['metal_id'],
              new_order['size_id'], new_order['style_id'],
              new_order['type_id'], id, ))

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
