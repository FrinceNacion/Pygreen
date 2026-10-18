import json
from pathlib import Path
from entities.Enemy import Enemy
from entities.Tower import Tower

STAGE_DIR = Path(__file__).resolve().parent
PATH_POINTS_FILE = STAGE_DIR / "path_points.json"
STAGE_DATA_FILE = STAGE_DIR / "stage_data.json"

DEFAULT_PATH_POINTS = [
    [11, 169],
    [274, 183],
    [648, 148],
    [897, 177],
    [946, 260],
    [862, 357],
    [710, 405],
    [518, 381],
    [482, 446],
    [513, 705]
]


def load_path_points():
    """Load path points from path_points.json."""
    if PATH_POINTS_FILE.exists():
        try:
            with open(PATH_POINTS_FILE, "r") as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading {PATH_POINTS_FILE}: {e}")
    return [list(pt) for pt in DEFAULT_PATH_POINTS]


def save_path_points(points):
    """Save path points to path_points.json."""
    with open(PATH_POINTS_FILE, "w") as f:
        json.dump(points, f, indent=4)


def load_stage_data():
    """Load stage configuration data from stage_data.json."""
    if STAGE_DATA_FILE.exists():
        try:
            with open(STAGE_DATA_FILE, "r") as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading {STAGE_DATA_FILE}: {e}")
    return {"enemies": [], "towers": []}


def save_stage_data(data):
    """Save stage configuration data to stage_data.json."""
    with open(STAGE_DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)


def get_enemies(path=None):
    """Instantiate and return Enemy objects configured for this stage."""
    if path is None:
        path = load_path_points()
    if not path:
        return []
    data = load_stage_data()
    enemies = []
    for item in data.get("enemies", []):
        enemies.append(Enemy(
            name=item["name"],
            health=item["health"],
            speed=item["speed"],
            path=path
        ))
    return enemies

def get_tower_slots():
    """Return tower slot positions configured for this stage."""
    data = load_stage_data()
    tower_slots = []
    for slot in data.get("tower_slots", []):
        tower_slots.append(Tower(slot["id"], slot["position"]))
    return tower_slots


"""def get_towers():
    data = load_stage_data()
    towers = []
    for item in data.get("towers", []):
        towers.append(Tower(
            name=item["name"],
            damage=item["damage"],
            range=item["range"],
            cooldown=item["cooldown"],
            position=tuple(item["position"])
        ))
    return towers"""


def get_stage_data():
    """Returns all stage data including path points, enemy configs, tower configs, and instances."""
    points = load_path_points()
    data = load_stage_data()
    return {
        "path_points": points,
        "enemies_data": data.get("enemies", []),
        "towers_data": data.get("towers", []),
        "enemies": get_enemies(points),
        "tower_slots": data.get("tower_slots", []),
        #"towers": get_towers(),
    }
