"""Try to predict next element of sequence"""

import random


class Session:
    sequence = []

    def put(self, item):
        """Add new item"""
        self.sequence.append(item)

    def len(self):
        """Get length of sequence"""
        return len(self.sequence)






