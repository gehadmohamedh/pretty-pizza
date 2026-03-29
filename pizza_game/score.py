import os 
def save_score(score):

    with open("./data/score.txt", "w") as f:
        f.write(str(score))

def get_score(request):
    try:
        with open("./data/score.txt", "r") as f:
            score = int(f.read())
    except (FileNotFoundError, ValueError):
        score = 0 
        
    return score