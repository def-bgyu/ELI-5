# 🧠 ELI5 Bot – Explain Like I'm 5

A fun and educational Generative AI chatbot that explains complex topics at three levels of understanding: Beginner, Intermediate, and Advanced. Built using Together.ai’s Mistral-7B model and Streamlit, this app is perfect for students, learners, and curious minds!

![Screenshot](./src/begin.jpg)
![Screenshot](./src/inter.jpg)

---

## ✨ Features

- 🎓 Choose explanation complexity: Beginner 🍼, Intermediate 📗, Advanced 🎓
- 🧵 Prompt-engineered LLM responses using Together.ai
- 📦 Deployment on Streamlit Cloud
- 🔒 Secure API key management 

---

## 🛠️ Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/your-username/eli5-bot.git
cd eli5-bot
```

### 2. Create and activate a virtual environment (optional)

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your Together.ai API key

Create a file at `.streamlit/secrets.toml` with the following:

```toml
TOGETHER_API_KEY = "your-together-api-key-here"
```

### 5. Run the app locally

```bash
streamlit run app.py
```

---

## 🌐 Deployment (Streamlit Cloud)

1. Push the project to GitHub
2. Go to [streamlit.io/cloud](https://streamlit.io/cloud) and sign in
3. Click **"New app"** → select your GitHub repo
4. Set the file path to `app.py`
5. In **Advanced Settings**, add your secret key:
   - `TOGETHER_API_KEY`: (paste your actual Together.ai key)

---

## 📁 Project Structure

```
eli5-bot/
├── app.py
├── prompts.py
├── background.jpg
├── requirements.txt
├── .gitignore
└── .streamlit/
    └── secrets.toml  
```

---

## 🎯 Future Improvements

- 🎨 **Improved UI & UX**
  - Custom fonts (e.g., Poppins or Montserrat)
  - Animated transitions or chat-style response bubbles
  - Dark mode toggle

- 🧠 **Advanced Features**
  - Compare explanations across all levels
  - PDF download of responses
  - "Learn More" follow-up suggestions using session memory

- ☁️ **Multi-deployment support**
  - Hugging Face Spaces / Vercel / Render integrations
  - Optional mobile-friendly layout

---

## 📚 License

MIT License. Feel free to fork, remix, and learn!

---

## 🤝 Contributing

Pull requests welcome! For major changes, please open an issue first.

---

## 👩‍💻 Built By

Nidhi Sankhe – [linkedin.com/in/nidhisankhe](https://linkedin.com/in/nidhisankhe)
