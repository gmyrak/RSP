"""Try to predict next element of sequence"""

import random


class Session:
    sequence = []
    items = set()

    def put(self, item):
        """Add new item"""
        self.sequence.append(item)
        self.items.add(item)

    def len(self):
        """Get length of sequence"""
        return len(self.sequence)

    def prediction(self):
        return 1




