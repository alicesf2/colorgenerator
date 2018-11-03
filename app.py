from flask import Flask
from colour import Color
import utils

app = Flask(__name__)

@app.route("/")
def main():
    #each scheme has 3 colors
    red = utils.red()
    colors = utils.achromatic(red)

    return "%s, %s, %s" % (colors[0], colors[1], colors[2])
