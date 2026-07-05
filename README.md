# 🍽️ Spice Garden — AI Food Ordering Chatbot

<div align="center">

**An intelligent, production-ready AI chatbot for food ordering**
Built with FastAPI · SQLite · Groq LLaMA · Tailwind CSS

[![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.111-009688?style=flat-square&logo=fastapi)](https://fastapi.tiangolo.com)
[![Groq](https://img.shields.io/badge/AI-Groq%20LLaMA-orange?style=flat-square)](https://groq.com)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)

</div>

---

## 📸 Screenshots

<div align="center">

### 💬 Chat Interface
![Chat Interface](screenshots/chat.png)

### 🏠 Welcome Screen
![Welcome Screen](screenshots/welcome.png)

</div>

---

## ✨ Features

- 🤖 **AI-Powered Conversations** — Zara, your intelligent food assistant powered by Groq LLaMA (free & fast)
- 🍕 **Menu-Aware Responses** — Knows the full menu, pricing, combos, and deals
- 💬 **Persistent Chat History** — All conversations stored in SQLite (no database setup needed)
- 🎨 **Modern Dark UI** — ChatGPT-inspired interface with Tailwind CSS
- 📱 **Fully Responsive** — Works on desktop, tablet, and mobile
- 🔄 **Session Management** — Multiple conversations with sidebar navigation
- ⌨️ **Typing Animation** — Visual loading indicator while AI responds
- 🚀 **FastAPI Backend** — Async Python API with automatic OpenAPI docs
- 🔒 **Environment Variables** — Secure credential management via `.env`
- 🗄️ **Zero Database Setup** — SQLite creates itself automatically on first run

---

## 🛠️ Tech Stack

| Layer       | Technology                        |
|-------------|-----------------------------------|
| Frontend    | HTML, Tailwind CSS, Vanilla JS    |
| Backend     | FastAPI (Python 3.10+)            |
| Database    | SQLite (auto-created)             |
| ORM         | SQLAlchemy 2.0                    |
| AI Model    | Groq LLaMA 3.3 70B (Free)        |
| Server      | Uvicorn (ASGI)                    |

---

## 📁 Project Structure

```
food-ordering-chatbot/
├── backend/
│   ├── app/
│   │   ├── database/connection.py       # SQLite connection
│   │   ├── models/chat.py               # ORM model
│   │   ├── schemas/chat.py              # Pydantic schemas
│   │   ├── routes/chat.py               # API endpoints
│   │   ├── services/openai_service.py   # Groq AI integration
│   │   └── utils/crud.py               # Database operations
│   ├── main.py                          # FastAPI entry point
│   ├── requirements.txt
│   ├── .env.example
│   └── chatbot.db                       # Auto-created SQLite DB
│
├── frontend/
│   └── index.html                       # Complete chatbot UI
│
└── README.md
```

---

## ⚡ Quick Start

### Prerequisites
- Python 3.10 or higher
- A free [Groq API key](https://console.groq.com) (no credit card needed)

### 1. Clone the repository

```bash
git clone https://github.com/your-username/food-ordering-chatbot.git
cd food-ordering-chatbot
```

### 2. Set up the backend

```bash
cd backend
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate

pip install -r requirements.txt
```

### 3. Configure environment variables

```bash
# Windows
copy .env.example .env
notepad .env
```

Add your Groq API key:
```env
GROQ_API_KEY=gsk_your_groq_api_key_here
```

> Get your free Groq API key at: https://console.groq.com

### 4. Run the backend

```bash
uvicorn main:app --reload
```

You should see:
```
🚀 Starting Food Ordering Chatbot API...
✅ Database and tables ready.
INFO:     Uvicorn running on http://127.0.0.1:8000
```

### 5. Open the frontend

Open `frontend/index.html` directly in your browser. No extra setup needed!

---

## 🔌 API Endpoints

| Method   | Endpoint             | Description                        |
|----------|----------------------|------------------------------------|
| `POST`   | `/api/chat`          | Send a message, receive AI reply   |
| `GET`    | `/api/history`       | Get chat history for a session     |
| `DELETE` | `/api/clear`         | Delete all messages for a session  |
| `GET`    | `/health`            | Health check                       |
| `GET`    | `/docs`              | Interactive Swagger API docs       |

### Example Request

```bash
curl -X POST http://127.0.0.1:8000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Suggest a spicy pizza under Rs.300", "session_id": "test123"}'
```

### Example Response

```json
{
  "reply": "Great choice! For spicy options under Rs.300, I recommend our Spicy Paneer Pizza at Rs.249...",
  "session_id": "test123",
  "timestamp": "2024-01-15T10:30:00"
}
```

---

## 🍽️ Menu Highlights

| Category    | Items                                                          |
|-------------|----------------------------------------------------------------|
| 🍕 Pizzas   | Margherita Rs.199, Spicy Paneer Rs.249, Chicken BBQ Rs.299    |
| 🍔 Burgers  | Veg Burger Rs.149, Chicken Zinger Rs.199, Double Patty Rs.249 |
| 🍜 Pasta    | Arrabbiata Rs.189, Creamy Mushroom Rs.219                     |
| 🥗 Healthy  | Quinoa Bowl Rs.239, Grilled Chicken Salad Rs.219              |
| 🍰 Desserts | Chocolate Lava Cake Rs.149, Tiramisu Rs.169                   |
| 🥤 Drinks   | Mango Lassi Rs.99, Cold Coffee Rs.119                         |

**Combo Deals:**
- 🎯 Burger + Fries + Drink = Rs.299 *(Save Rs.80)*
- 👨‍👩‍👧‍👦 Family Meal (2 Pizzas + 4 Drinks) = Rs.799
- 🍕 Pizza + Drink = 15% off

---

## 💬 Example Conversations

| You say | Zara responds |
|---------|---------------|
| "Suggest a spicy veg pizza under Rs.300" | Recommends Spicy Paneer Pizza at Rs.249 |
| "I want a burger combo deal" | Suggests Burger + Fries + Drink at Rs.299 |
| "What are healthy options?" | Lists Quinoa Bowl, Grilled Chicken Salad |
| "Place an order for 2 Margheritas" | Confirms with order number #ORD12345 |
| "Track my order" | Simulates tracking with estimated delivery |

---

## 🗄️ Database Schema

```sql
CREATE TABLE chat_messages (
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id VARCHAR(100) NOT NULL,
    role       VARCHAR(20) NOT NULL,
    content    TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

The `chatbot.db` SQLite file is **automatically created** on first run!

---

## 🔮 Future Improvements

- [ ] User authentication with JWT tokens
- [ ] Real payment gateway integration (Razorpay)
- [ ] Live order tracking with WebSockets
- [ ] Multi-language support (Hindi, Telugu, Tamil)
- [ ] Voice input and output support
- [ ] Admin dashboard for menu management
- [ ] Docker containerization
- [ ] Deploy to cloud (Render, Railway)
- [ ] Image gallery for menu items
- [ ] Loyalty points and rewards system

---

## 🚀 Deployment

### Backend → Render (Free)

1. Push repo to GitHub
2. Go to [render.com](https://render.com) → New Web Service
3. Connect your GitHub repo, set root to `backend/`
4. Build command: `pip install -r requirements.txt`
5. Start command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
6. Add env variable: `GROQ_API_KEY=your_key`

### Frontend → Netlify (Free)

1. Go to [netlify.com](https://netlify.com)
2. Drag and drop the `frontend/` folder
3. Update `API_BASE` in `index.html` to your Render backend URL

---

## 📄 License

MIT License — free to use, modify, and distribute.

---

## 🙏 Acknowledgements

- [Groq](https://groq.com) — Free, blazing-fast LLaMA inference
- [FastAPI](https://fastapi.tiangolo.com) — Modern Python web framework
- [Tailwind CSS](https://tailwindcss.com) — Utility-first CSS framework
- [SQLAlchemy](https://sqlalchemy.org) — Python SQL toolkit and ORM

---

<div align="center">

**Made with ❤️ by Divya Laxmi**

⭐ Star this repo if you found it helpful!

</div>
