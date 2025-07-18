# Tile class
class Tile:
    def __init__(self, tile_type, emoji):
        self.tile_type = tile_type
        self.emoji = emoji
        self.tile_block = {}
    def __eq__(self, other):
        return isinstance(other, Tile) and self.emoji == other.emoji and self.tile_type == other.tile_type

    def __hash__(self):
        return hash((self.emoji, self.tile_type))

    def __repr__(self):
        return f"Tile({self.tile_type!r}, {self.emoji!r})"