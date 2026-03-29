import os 

BASE_DIR = os.path.expanduser("/tmp")

def save_score(score):
    os.makedirs(BASE_DIR, exist_ok=True)
    with open(os.path.join(BASE_DIR, "score.txt"), "w") as f:
        f.write(str(score))

def get_score():
    try:
        with open(os.path.join(BASE_DIR, "score.txt"), "r") as f:
            score = int(f.read())
    except (FileNotFoundError, ValueError):
        score = 0 
        
    return score