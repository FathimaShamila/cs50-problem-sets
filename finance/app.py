import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    user_id = session.get("user_id")
    portfolio = db.execute("SELECT symbol,shares,price FROM portfolio WHERE user_id = ?",user_id)
    cash = db.execute("SELECT cash FROM users WHERE id = ?",user_id)[0]["cash"]
    portfolio_total = 0
    for stock in portfolio:
        stock["value"] = stock["shares"] * stock["price"]
        portfolio_total += stock["value"]
    grand_total = portfolio_total + cash

    return render_template("index.html",portfolio = portfolio,cash = cash,grand_total = grand_total)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "GET":
        return render_template("buy.html")
    if request.method == "POST":
        symbol = request.form.get("symbol")
        number = request.form.get("number")

        # Convert shares to int
        try:
            number = int(number)
        except ValueError:
            return apology("Enter a valid number of shares.",403)
        if number <= 0:
            return apology("Enter a positive number of shares.",403)

        # Lookup Stock
        result = lookup(symbol)
        if result is None:
            return apology("Invalid Symbol",403)

        user_id = session.get("user_id")
        cash = db.execute("SELECT cash FROM users WHERE id = ?",user_id)[0]["cash"]
        total_cost =  number * result["price"]
        if cash < total_cost:
            return apology("Insufficient Funds!",403)
        balance = cash - total_cost
        db.execute("UPDATE users SET cash = ? WHERE id = ? ",balance,user_id)
        rows = db.execute("SELECT shares FROM portfolio WHERE user_id = ? AND symbol = ?",user_id,result["symbol"])
        if len(rows) > 0:
            current_shares = rows[0]["shares"]
            new_shares = current_shares + number
            db.execute("UPDATE portfolio SET shares = ?,price = ? WHERE user_id = ? AND symbol = ?",new_shares,result["price"],user_id,result["symbol"])
        else:
            db.execute("INSERT INTO portfolio (symbol,shares,price,user_id) VALUES (?,?,?,?)",result["symbol"],number,result["price"],user_id)
        return render_template("bought.html",symbol = result["symbol"],name = result["name"],price = result["price"])


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    user_id = session.get("user_id")
    rows = db.execute
    return apology("TODO")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "GET":
        return render_template("quote.html")
    if request.method == "POST":
        symbol = request.form.get("symbol")
        result = lookup(symbol)
        if result != None:
            return render_template("quoted.html",symbol = result["symbol"],name = result["name"],price = result["price"])
        else:
            return apology("Invalid Symbol",403)


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    # Display registration form
    if request.method == "GET":
        return render_template("registration.html")
    if request.method == "POST":
        username = request.form.get("user_name")
        password = request.form.get("pass_word")
        confirm_password = request.form.get("confirm_password")
        if not username:
            return apology("Enter Username",403)
        if not password:
            return apology("Enter password",403)
        if password != confirm_password:
            return apology("passwords must match",403)
        rows = db.execute(
        "SELECT * FROM users WHERE username = ?", username)
        if len(rows) > 0 :
            return apology("Username already exists.Choose a different username",403)
        else:
            hash = generate_password_hash(password)
            db.execute("INSERT INTO users (username,hash) VALUES (?,?)",username,hash)
            return redirect("/")



@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    user_id = session.get("user_id")
    stocks = db.execute("SELECT symbol,shares FROM portfolio WHERE user_id = ? ",user_id)
    if request.method == "GET":
        return render_template("sell.html",stocks = stocks)
    if request.method == "POST":
        symbol = request.form.get("symbol")
        number = request.form.get("number")
        if not symbol or not number:
            return apology("Must Provide stock and number of shares")
        try:
            number = int(number)
        except ValueError:
            return apology("Invalid number of shares")
        stock = next((s for s in stocks if s["symbol"] == symbol),None)
        if not stock:
            return apology("Stock not found",403)
        if number > stock["shares"]:
            return apology("Insufficient shares to sell")
        result = lookup(symbol)
        price = result["price"]
        cost = price * number
        if number == stock["shares"]:
            db.execute("DELETE FROM portfolio WHERE user_id = ? AND symbol = ?",user_id,symbol)
        else:
            db.execute("UPDATE portfolio SET shares = shares - ?  WHERE user_id = ? AND symbol = ?",number,user_id,symbol)
        db.execute("UPDATE users SET cash = cash + ? WHERE id = ?",cost ,user_id)
        flash(f"Sold {number} shares of {symbol}")
        return redirect("/")



