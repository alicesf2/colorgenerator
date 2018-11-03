from flask import Flask
from colour import Color

import utils

app = Flask(__name__)

@app.route("/")
def main():
    #each scheme has 3 colors
    color = utils.green()
    colors = utils.complementary(color.hue)

    return "%s, %s, %s, %s, %s" % (colors[0], colors[1], colors[2], colors[3], colors[4])
