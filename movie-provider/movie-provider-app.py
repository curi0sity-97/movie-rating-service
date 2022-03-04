from flask import Flask,request,render_template,redirect
from argparse import ArgumentParser
import sys

app = Flask(__name__)

@app.route("/movies")
def list_movies():
    movies = ["Avengers: End Game", "Scarface", "Fight Club"]
    return {"success":True,"list": movies}


if __name__ == "__main__":
    ip, port = sys.argv[1], sys.argv[2]
    app.run(host=ip,port=port)

