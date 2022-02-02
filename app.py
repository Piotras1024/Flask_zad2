from flask import Flask, request, redirect, render_template

app = Flask(__name__)

@app.route("/")
def main_endpoint():
    return redirect("/mypage/me")

@app.route("/mypage/me")
def mypage_me():
    return render_template("me.html")

@app.route("/mypage/contact", methods=['GET', 'POST'])
def mypage_contact():
    if request.method == 'GET':
        return render_template("contact.html")
    elif request.method == 'POST':
        wiadomosc = request.form['element']
        print(f"OTRZYMALEM POST. WIADOMOSC {wiadomosc}")
        return redirect("/mypage/contact")
