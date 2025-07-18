import random

# Village settings
VILLAGE_WIDTH = 31
VILLAGE_HEIGHT = 21
PATH = "🟫"
EMPTY = "⬜"

# Building emojis
BUILDINGS = {
    "house": "🏠",
    "farm": "🌾",
    "blacksmith": "⚒️ ",
    "market": "🛒",
    "inn": "🏨",
    "church": "⛪",
    "barn": "🐄",
    "guardpost": "🛡️ ",
}

BUILDING_LIST = list(BUILDINGS.values())

# Directions (no diagonals)
DIRECTIONS = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # N, E, S, W

# Initialize village grid
def create_empty_village():
    return [[EMPTY for _ in range(VILLAGE_WIDTH)] for _ in range(VILLAGE_HEIGHT)]

# Check if coordinates are within bounds
def in_bounds(x, y):
    return 0 <= x < VILLAGE_WIDTH and 0 <= y < VILLAGE_HEIGHT

# Check if there's already a parallel path next to this one
def has_parallel_path(village, x, y, dx, dy):
    # For vertical paths, check east and west
    if dx == 0:
        for offset in [-1, 1]:
            if in_bounds(x + offset, y) and village[y][x + offset] == PATH:
                return True
    # For horizontal paths, check north and south
    if dy == 0:
        for offset in [-1, 1]:
            if in_bounds(x, y + offset) and village[y + offset][x] == PATH:
                return True
    return False

# Generate the village
def generate_village():
    village = create_empty_village()
    center_x, center_y = VILLAGE_WIDTH // 2, VILLAGE_HEIGHT // 2
    village[center_y][center_x] = "⛲"  # central fountain

    paths = [(center_x, center_y, dx, dy, 7) for dx, dy in DIRECTIONS]
    visited = set()

    while paths:
        x, y, dx, dy, base_length = paths.pop()
        length = max(3, base_length + random.randint(-1, 1))  # add a bit of variety
        for _ in range(length):
            x += dx
            y += dy
            if not in_bounds(x, y):
                break
            if (x, y) in visited:
                continue
            if has_parallel_path(village, x, y, dx, dy):
                break  # cancel this path segment to avoid 2-wide paths
            village[y][x] = PATH
            visited.add((x, y))

            # Chance to add an offshoot in the perpendicular direction, with reduced length
            if random.random() < 0.10:
                perp_dx, perp_dy = -dy, dx  # rotate 90 degrees
                paths.append((x, y, perp_dx, perp_dy, max(3, base_length - 2)))
            if random.random() < 0.10:
                perp_dx, perp_dy = dy, -dx  # rotate other 90
                paths.append((x, y, perp_dx, perp_dy, max(3, base_length - 2)))

            # Chance to place a building next to path
            for adj_dx, adj_dy in DIRECTIONS:
                adj_x, adj_y = x + adj_dx, y + adj_dy
                if in_bounds(adj_x, adj_y) and village[adj_y][adj_x] == EMPTY:
                    if random.random() < 0.25:
                        village[adj_y][adj_x] = random.choice(BUILDING_LIST)

    return village

# Render the village
def draw_village(village):
    return "\n".join("".join(row) for row in village)

# Generate and display the village
village = generate_village()
village_map = draw_village(village)
print(village_map)
