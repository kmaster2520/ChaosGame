from PIL import Image
from math import sin, cos, pi
from random import randint, choice
import sys

'''
Code written by Sathvik Kadaveru
3/19/2023
'''

IMAGE_W = 800
IMAGE_H = IMAGE_W

BG_COLOR = (0, 0, 0)
POINT_COLOR = (0, 255, 0)


def midpoint(a, b, d=0.5):
    mx = int(d * a[0] + (1 - d) * b[0])
    my = int(d * a[1] + (1 - d) * b[1])
    return mx, my


def chaos_game(image, *, num_points=3, d=0.5, num_iter=50000, include_center=False):

    center_p = (IMAGE_W // 2, IMAGE_H // 2)
    radius = int(min(center_p) * 0.8)
    d_theta = 2 * pi / num_points
    points = []
    for i in range(num_points):
        theta = d_theta * i
        px = center_p[0] + int(radius * sin(theta))
        py = center_p[1] - int(radius * cos(theta))
        points.append((px, py))
    if include_center:
        points.append(center_p)

    for point in points:
        image.putpixel(point, POINT_COLOR)

    p = (randint(0, IMAGE_W), randint(0, IMAGE_H))
    for i in range(num_iter):
        goal_p = choice(points)
        mid_p = midpoint(p, goal_p, d)
        image.putpixel(mid_p, POINT_COLOR)
        p = mid_p



def main():
    print('begin main')
    # to run this:
    # python main.py [n]

    if len(sys.argv) <= 1:
        n = 3
    else:
        n = int(sys.argv[1])

    '''
    d (from 0 to 1) is the jump from the current point to a chosen point.
    if d is 1/2, then the next point is 1/2 from the current point to the chosen point
    if n is the number of vertices of the fractal, then d should be 3 / (n + 3)
    '''
    d = 3 / (n + 3)
    num_iter = 50000

    img = Image.new(mode="RGB", size=(IMAGE_W, IMAGE_H), color=BG_COLOR)
    chaos_game(img, num_points=n, d=d, num_iter=num_iter)
    #img.show()
    img.save(f"generated/chaos_{n}p_{num_iter}iter.png")


if __name__ == '__main__':
    main()

