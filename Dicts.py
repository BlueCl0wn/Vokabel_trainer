class dicts():
    def __init__(self, id, name, URI, sprache1, sprache2):
        self.id = id
        self.name = name
        self.URI = URI
        self.sprache1 = sprache1
        self.sprache2 = sprache2
    def toDicts(self):
        return str(self.id) + " | " + self.name
