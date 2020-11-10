""" Make an homography between two images.

Make an homography between two images. In this script we use automatic methods
to select and identify keypoints. The available method so far is ORB.

"""
import cv2
from matplotlib import pyplot as plt
import numpy as np

from visio_per_computador.common import descriptors


def run():
    """ Read two images of a document and tries to warpped them.
    """

    # We read the images
    deformed_img = cv2.imread("../in/descriptors/photo_doc.jpg", 0)
    scanned_img = cv2.imread("../in//descriptors/scanned.jpg", 0)

    kp1, desc1 = descriptors.get_kp_desc(method="sift", img=deformed_img)
    kp2, desc2 = descriptors.get_kp_desc(method="sift", img=scanned_img)

    matches = descriptors.match_descriptors(method="F", desc1=desc1,
                                            desc2=desc2, k=2)

    matches = descriptors.filter_matches(method="KNN", matches=matches,
                                         proportion=0.7)

    points1 = np.zeros((len(matches), 2), dtype=np.float32)
    points2 = np.zeros((len(matches), 2), dtype=np.float32)

    for i, match in enumerate(matches):
        points1[i, :] = kp1[match.queryIdx].pt
        points2[i, :] = kp2[match.trainIdx].pt

    # Find homography
    h, mask = cv2.findHomography(points1, points2, cv2.RANSAC)

    # Use homography
    height, width = scanned_img.shape
    im1Reg = cv2.warpPerspective(deformed_img, h, (width, height))

    plt.subplot(1, 3, 1)
    plt.title("Warped")
    plt.imshow(im1Reg, cmap="gray")

    plt.subplot(1, 3, 2)
    plt.imshow(deformed_img, cmap="gray")

    plt.subplot(1, 3, 3)
    plt.imshow(scanned_img, cmap="gray")

    plt.show()

    cv2.imwrite("../out/document_fixed.png", deformed_img)


run()
