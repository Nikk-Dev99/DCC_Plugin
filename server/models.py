class Item:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def to_dict(self):
        return {"name": self.name, "quantity": self.quantity}
