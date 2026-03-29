# 🍕 Pretty Pizza Game

A super simple and funny Django game built to demonstrate how web apps can be containerized using Docker.

## 🎮 About the Game

Click the **"Make Pizza 🍕"** button and get a random result:

* 🍕 Awesome Pizza 😋😍🍕 (+2)
* 🍕 Perfect Pizza (+1)
* 🔥 Burnt Pizza (-1)
* 🐶 Dog stole it (0)
* 😂 Chef ate it (0)

Your score increases as you play!
Your score inittally = 0 and saved in "~/tmp/data_score"



## 🚀 How to Run


### 1️⃣ change Directory to be inside the app folder 

```bash
cd  pretty-pizza/
```
### 2️⃣ upgrade pip 

```bash
pip install --upgrade pip
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run Migrations

```bash
python manage.py migrate
```

### 5️⃣ Run Server

```bash
python manage.py runserver 0.0.0.0:8000
```

Open your browser:

```
http://127.0.0.1:8000/
```
## Enviroment Variables 
```
BACKGROUND_COLOR --> default "#A98B76"
```

## Data Directory 
```
~/tmp/data_score
```
