class Orders():
    """Class to create an animal"""
    # Class initializer
    def __init__(self, id, timestamp, metal_id, size_id, style_id, type_id = 0):
        self.id = id
        self.timestamp = timestamp
        self.metal_id = metal_id
        self.size_id = size_id
        self.style_id = style_id
        self.type_id = type_id
        self.metal = None
        self.size = None
        self.style = None
        self.type = None
