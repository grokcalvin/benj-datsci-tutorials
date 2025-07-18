from noise import pnoise2

# Map dimensions (viewport)
VIEW_WIDTH = 31
VIEW_HEIGHT = 31

# Tiles
TILE_GRASS = "🌿"
TILE_WATER = "💧"
TILE_SAND = "🟨"
TILE_FOREST = "🌲"
TILE_SMILE = "😄"

# Biome thresholds
TILE_THRESHOLDS = [
    (0.3, TILE_WATER),
    (0.45, TILE_SAND),
    (0.65, TILE_GRASS),
    (1.0, TILE_FOREST),
]

# Adjusted real Perlin noise tile function
def real_noise_tile(x, y, scale=0.1, octaves=1, persistence=0.5, lacunarity=2.0):
    value = pnoise2(x * scale, y * scale, octaves=octaves, persistence=persistence, lacunarity=lacunarity)
    # Normalize value from [-1, 1] to [0, 1]
    normalized = (value + 1) / 2
    return normalized

# Function to get tile based on Perlin noise
def get_tile_real_noise(x, y):
    value = real_noise_tile(x, y, scale=0.08)
    for threshold, tile in TILE_THRESHOLDS:
        if value <= threshold:
            return tile
    return TILE_GRASS

# Viewport center offset (player fixed in center)
offset_x = 0
offset_y = 0

# Re-render map with real noise
def draw_viewport_real(center_x, center_y):
    output = []
    for j in range(center_y - VIEW_HEIGHT // 2, center_y + VIEW_HEIGHT // 2):
        row = ""
        for i in range(center_x - VIEW_WIDTH // 2, center_x + VIEW_WIDTH // 2):
            if i == center_x and j == center_y:
                row += TILE_SMILE
            else:
                row += get_tile_real_noise(i, j)
        output.append(row)
    return "\n".join(output)

# Render the map using real Perlin noise
offset_x = 0
offset_y = 20
real_noise_map = draw_viewport_real(offset_x, offset_y)
print(real_noise_map)


