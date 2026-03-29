from django.shortcuts import render
from django.conf import settings
# Create your views here.
import random
from django.shortcuts import render
from .score import save_score, get_score

def pizza_game(request):
    messages = [
        ("Perfect Pizza 🍕", 1),
        ("Awesome Pizza 😋😍🍕", 2),
        ("Burnt Pizza 🔥", -1),
        ("Dog stole it 🐶", -2),
        ("Chef ate it 😂", 0)
    ]

    result = None
    score = get_score()

    if request.method == "POST":
        message, points = random.choice(messages)
        score += points
        save_score(score)
        result = message

    return render(request, "pizza_game/pizza.html", {
        "result": result,
        "score": score,
        "background_color": settings.BACKGROUND_COLOR
    })