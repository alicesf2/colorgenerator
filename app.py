from flask import Flask
from colour import Color
import utils

app = Flask(__name__)

@app.route("/")
def main():
    red = utils.red()
    orange = utils.orange()
    yellow = utils.yellow()
    green = utils.green()
    blue = utils.blue()
    violet = utils.violet()
    return "%s, %s, %s, %s, %s, %s," % (red.hue, orange.hue, yellow.hue, green.hue, blue.hue, violet.hue)
