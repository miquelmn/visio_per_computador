""" Make an homography between two images.

This script makes the homography between two images. To do so we select manually
the correspondence set of points.

"""
import cv2
from matplotlib import pyplot as plt
import numpy as np

punts = {}


def on_click(name: str, fig, event):
    """ Select a set of points.

    Select a set of points from Matplotlib. The points are saved on a global
    dictionary, whom keys are passed as parameter to this funciton. The fig
    parameter is the figure where to draw the points

    Args:
        name (str): Key of the dictionary, unique
        fig (figure): Matplotlib object, figure obtained from plt.figure
        event : Information frm the event

    Returns:
        None
    """
    if name not in punts:
        punts[name] = []
    punts[name].append([event.xdata, event.ydata])
    plt.scatter(event.xdata, event.ydata)
    fig.canvas.draw()


def run():
    # We read the images
    img1 = cv2.imread("../in/llibre1.jpg")
    img2 = cv2.imread("../in/llibre3.jpg")

    # We show the first image allowing to select the points.
    fig1 = plt.figure()
    fig1.canvas.mpl_connect('button_press_event',
                            lambda x: on_click("img_1", fig1, x))
    plt.imshow(img1)
    plt.show()

    # We show the second image allowing to select the points.
    fig2 = plt.figure()
    fig2.canvas.mpl_connect('button_press_event',
                            lambda x: on_click("img_2", fig2, x))
    plt.imshow(img2)
    plt.show()


run()
