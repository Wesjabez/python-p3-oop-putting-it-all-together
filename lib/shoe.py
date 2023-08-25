#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size
        self.condition = "New"  # Initialize condition attribute

    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")

if __name__ == "__main__":
    pass
