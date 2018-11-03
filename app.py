from flask import Flask
from colour import Color
import utils

app = Flask(__name__)

@app.route("/")
def main():
    #each scheme has 3 colors
    red = utils.red()
    colors = utils.analogous(red)

    return "%s, %s, %s" % (colors[0].hue, colors[1].hue, colors[2].hue)
