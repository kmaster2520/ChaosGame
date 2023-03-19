from PIL import Image
from math import sin, cos, pi
from random import randint, choice
import sys
import argparse

"""
Code written by Sathvik Kadaveru
3/19/2023
"""

IMAGE_W = 800
IMAGE_H = IMAGE_W

BG_COLOR = (0, 0, 0)
POINT_COLOR = (0, 255, 0)


def midpoint(a, b, d=0.5):
    """
    :param a: The current point
    :param b: The target point
    :param d: The proportion to travel from point a to b
    :return: The next point
    """
    mx = int(d * a[0] + (1 - d) * b[0])
    my = int(d * a[1] + (1 - d) * b[1])
    return mx, my


def chaos_game(image, *, num_points=3, d=0.5, num_iter=50000, include_center=False):
    """

    :param image: The new PIL image to modify
    :param num_points: The number of vertices
    :param d: The proportion to travel to the target point
    :param num_iter: The number of iterations
    :param include_center: Whether to include the center as a valid point to travel to (not fully supported)
    :return:
    """
    center_p = (IMAGE_W // 2, IMAGE_H // 2)
    radius = int(min(center_p) * 0.8)

    # generate vertices
    d_theta = 2 * pi / num_points
    points = []
    for i in range(num_points):
        theta = d_theta * i
        px = center_p[0] + int(radius * sin(theta))
        py = center_p[1] - int(radius * cos(theta))
        points.append((px, py))
    for point in points:
        image.putpixel(point, POINT_COLOR)

    if include_center:
        points.append(center_p)

    # run the chaos game
    p = (randint(0, IMAGE_W), randint(0, IMAGE_H))
    for i in range(num_iter):
        goal_p = choice(points)
        mid_p = midpoint(p, goal_p, d)
        image.putpixel(mid_p, POINT_COLOR)
        p = mid_p


def main():
    print("begin main")
    # to run this:
    # python main.py [n]

    parser = argparse.ArgumentParser(description='Run a Chaos Game')
    parser.add_argument('-n', type=int, help="Number of vertices", default=3)
    parser.add_argument('-i', type=int, help="Number of iterations", default=50000)
    parser.add_argument('-s', help="Should save image to file?", action="store_true")
    args = parser.parse_args()

    """
    d (from 0 to 1) is the jump from the current point to a chosen point.
    if d is 1/2, then the next point is 1/2 from the current point to the chosen point
    if n is the number of vertices of the fractal, then d should be 3 / (n + 3)
    """
    n = args.n
    d = 3 / (n + 3)
    should_save_image = args.s
    num_iter = args.i

    img = Image.new(mode="RGB", size=(IMAGE_W, IMAGE_H), color=BG_COLOR)
    chaos_game(img, num_points=n, d=d, num_iter=num_iter)
    img.show()
    if should_save_image:
        img.save(f"generated/chaos_{n}p_{num_iter}iter.png")


if __name__ == "__main__":
    main()
