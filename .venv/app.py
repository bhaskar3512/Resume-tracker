from flask import Flask, redirect, request, render_template
import datetime
import sqlite3

app = Flask(__name__)

GITHUB_URL = "https://github.com/bhaskar3512"
LINKEDIN_URL = "https://www.linkedin.com/in/bhaskar-harugade-04-bhaskar/"


# 📊 Database setup
def init_db():
    conn = sqlite3.connect('clicks.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS clicks
                 (platform TEXT, ip TEXT, time TEXT)''')
    conn.commit()
    conn.close()


init_db()


def log_click(platform, ip):
    conn = sqlite3.connect('clicks.db')
    c = conn.cursor()
    c.execute("INSERT INTO clicks VALUES (?, ?, ?)",
              (platform, ip, str(datetime.datetime.now())))
    conn.commit()
    conn.close()


@app.route('/github')
def github():
    log_click("GitHub", request.remote_addr)
    return redirect(GITHUB_URL)


@app.route('/linkedin')
def linkedin():
    log_click("LinkedIn", request.remote_addr)
    return redirect(LINKEDIN_URL)


@app.route('/')
def dashboard():
    conn = sqlite3.connect('clicks.db')
    c = conn.cursor()

    c.execute("SELECT * FROM clicks ORDER BY time DESC")
    data = c.fetchall()

    c.execute("SELECT COUNT(*) FROM clicks WHERE platform='GitHub'")
    github_count = c.fetchone()[0]

    c.execute("SELECT COUNT(*) FROM clicks WHERE platform='LinkedIn'")
    linkedin_count = c.fetchone()[0]

    conn.close()

    return render_template("dashboard.html",
                           data=data,
                           github_count=github_count,
                           linkedin_count=linkedin_count)


if __name__ == '__main__':
    app.run(debug=True)