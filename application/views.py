from flask import Blueprint, render_template, url_for, request, g, redirect, session, jsonify
import urllib.request, random
import config as conf
from .gamesession import Gamesession
from . import trendapi

views = Blueprint("views", __name__, url_prefix="/")

def getGameSession():
    return session.get("gamesession")

@views.route("/")
def index():
    return render_template("index.html")

@views.route("/gameView")
def gameView():
    return render_template("gameView.html", gameData=getGameSession().getGameData())

@views.route("/startGame", methods=["POST"])
def startGame():
    playerOneName = request.form["nameOne"]
    playerTwoName = request.form["nameTwo"]

    session["gamesession"] = Gamesession()

    getGameSession().startGame(playerOneName, playerTwoName)

    return redirect(url_for('views.gameView'))

@views.route("/generateWord")
def generateWord():
    getGameSession().generateWord()
    return getGameSession().getWord()

@views.route("/submitTerms", methods=["POST"])
def submitTerms():
   
    termOne = request.form["termOne"]
    termTwo = request.form["termTwo"]
    
    getGameSession().playRound(termOne, termTwo)

    return jsonify(getGameSession().getGameData())