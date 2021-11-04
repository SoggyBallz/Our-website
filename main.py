from flask import Flask, render_template
app = Flask('app')


@app.route('/')
def index():
  return render_template("index.html")

@app.route('/checkout')
def checkout():
  return render_template("checkout.html")

@app.route('/client-main')
def client():
  return render_template("client-main.html")

@app.route('/search')
def search():
  return render_template("search.html")

@app.route('/admin-main')
def admin_main():
  return render_template("admin-main.html")

@app.route('/admin-changes')
def admin_changes():
  return render_template("admin-changes.html")

@app.route('/about')
def about():
  return render_template("about.html")

@app.route('/reserve')
def reserve():
  return render_template("reserve.html")

app.run(host='0.0.0.0', port=8080)