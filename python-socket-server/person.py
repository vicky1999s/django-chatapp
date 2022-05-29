class Person:
    def __init__(self, addr, client) -> None:
        self.name = None
        self.addr = addr
        self.client = client

    def set_name(self, name):
        self.name = name
    
    def __repr__(self) -> str:
        return f"person({self.addr} {self.name})"