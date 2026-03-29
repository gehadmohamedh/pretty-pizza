from django.shortcuts import render

# Create your views here.
import random
from django.shortcuts import render

def pizza_game(request):
    messages = [
        ("Perfect Pizza 🍕", 1),
        ("Burnt Pizza 🔥", -1),
        ("Dog stole it 🐶", 0),
        ("Chef ate it 😂", 0),
    ]

    result = None
    score = request.session.get('score', 0)

    if request.method == "POST":
        message, points = random.choice(messages)
        score += points
        request.session['score'] = score

        result = message
    back_ground_color = "yello"

    return render(request, "pizza_game/pizza.html", {
        "result": result,
        "score": score,
        "background_color": back_ground_color
    })