class Band:
    """Class Band, a band with multiple musicians"""

    def __init__(self,name):
        """Initialize a Band class"""
        self.name = name
        self.musicians = []

    def add(self, musician):
        """Add a musician to a band """
        self.musicians.append(musician)

    def __str__(self):
        """String representation for band class"""
        musician_str = ",".join(str(m) for m in self.musicians)
        return f"{self.name} ({musician_str})"

    def play(self):
        """play all musicians and return result"""
        return "\n".join(musician.play() for musician in self.musicians)
