TYPES = [
    {
      "id": 1,
      "name": "Ring",
      "priceMultiplier": 1
    },
    {
      "id": 2,
      "name": "Earrring",
      "priceMultiplier": 2
    },
    {
      "id": 3,
      "name": "Necklace",
      "priceMultiplier": 4
    }
]

def get_all_types():
    """Return list of all types"""
    return TYPES

# Function with a single parameter
def get_single_type(id):
    """Get a single dictionary from the list"""
    # Variable to hold the found type, if it exists
    requested_type = None

    # Iterate the TYPES list above. Very similar to the
    # for..of loops you used in JavaScript.
    for type in TYPES:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if type["id"] == id:
            requested_type = type

    return requested_type
