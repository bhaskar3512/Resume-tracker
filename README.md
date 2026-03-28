# 🚀 Resume Click Tracker

A Flask-based web application that tracks clicks on resume links (GitHub & LinkedIn) and displays them in a live dashboard.

---

## 📌 Features

* 🔗 Track clicks on GitHub and LinkedIn links
* 📊 Dashboard showing total clicks
* 🌐 Stores IP address and timestamp
* 🔄 Auto-delete data older than 24 hours
* ⚡ Lightweight and easy to deploy

---

## 🛠 Tech Stack

* Python
* Flask
* SQLite
* HTML, CSS

---

## 📁 Project Structure

```
resume-click-tracker/
├── app.py
├── requirements.txt
├── Procfile
├── templates/
│   └── dashboard.html
├── .gitignore
```

---

## ⚙️ How It Works

1. User clicks a custom link from your resume
2. Flask server logs the click (IP + time)
3. Data is stored in SQLite database
4. User is redirected to actual profile
5. Dashboard displays analytics

---

## ▶️ Run Locally

```bash
git clone https://github.com/yourusername/resume-click-tracker.git
cd resume-click-tracker
pip install -r requirements.txt
python app.py
```

Open in browser:

```
http://127.0.0.1:5000/
```

---

## 🌐 Deployment (Render)

1. Push project to GitHub
2. Create Web Service on Render
3. Set:

   * Build Command: `pip install -r requirements.txt`
   * Start Command: `gunicorn app:app`
4. Deploy 🚀

---

## 🔗 Usage

Use these links in your resume:

```
https://your-app.onrender.com/github
https://your-app.onrender.com/linkedin
```

---

## ⚠️ Notes

* Localhost links (127.0.0.1) won’t work for others
* Render free tier may sleep after inactivity
* SQLite may reset on free hosting

---

## 🚀 Future Improvements

* 📊 Graph analytics dashboard
* 📍 Location tracking (GeoIP)
* 🔔 Email / Telegram notifications
* 🔐 Authentication for dashboard

---

## 👨‍💻 Author

Bhaskar Harugade

---

## ⭐ If you like this project

Give it a star on GitHub ⭐
