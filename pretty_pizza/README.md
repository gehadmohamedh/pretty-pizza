# 🍕 Pretty Pizza Game

A super simple and funny Django game built to demonstrate how web apps can be containerized using Docker.

## 🎮 About the Game

Click the **"Make Pizza 🍕"** button and get a random result:

* 🍕 Perfect Pizza (+1)
* 🔥 Burnt Pizza (-1)
* 🐶 Dog stole it (0)
* 😂 Chef ate it (0)

Your score increases as you play!


## 🚀 How to Run

### 1️⃣ Create Virtual Environment

```bash
python -m venv venv
```

### 2️⃣ Activate Virtual Environment

**Mac/Linux**

```bash
source venv/bin/activate
```

**Windows**

```bash
venv\Scripts\activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Run Migrations

```bash
python manage.py migrate
```

---

### 5️⃣ Run Server

```bash
python manage.py runserver
```

Open your browser:

```
http://127.0.0.1:8000/
```
