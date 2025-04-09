import json
from ..constants import MAX_ENTRIES,LEADERBOARD_PATH

def load_leaderboard():
    try:
        with open(LEADERBOARD_PATH, 'r') as leaderboard_file:
            leaderboard_contents = leaderboard_file.read() # read the leaderboard

        parsed_leaderboard = json.loads(leaderboard_contents) # parse the leaderbaord into a dict

        if not isinstance(parsed_leaderboard, dict): # ensures the the dict is a dict
            raise ValueError("Leaderboard file does not contain a valid dictionary.")

        return parsed_leaderboard
    
    except FileNotFoundError:
        # if the file doesnt't exist.
        print(f"Leaderboard file not found at {LEADERBOARD_PATH}. Creating a new one.")
        return {}

    except json.JSONDecodeError:
        print(f"Leaderboard file at {LEADERBOARD_PATH} is malformed.")
        return{}

    except ValueError as e:
        print(f"Error loading the leaderboard: {e}")
        return {}

def save_leaderboard(leaderboard):
    
    with open(LEADERBOARD_PATH, 'w') as leaderboard_file:
        json.dump(leaderboard, leaderboard_file)   

def add_score(name, score, leaderboard, max_entries = MAX_ENTRIES):
    
    leaderboard[name] = score
    
    sorted_leaderboard = sorted(leaderboard.items(),key = lambda item: item[1], reverse = True)

    trimmed_leaderboard = dict(sorted_leaderboard[:max_entries])

    return trimmed_leaderboard