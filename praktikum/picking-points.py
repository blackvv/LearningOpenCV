import cv2 as cv
import argparse
import sys
import os

if __name__ == '__main__':
    img_file = sys.argv[1]

    print(f'Reading image file: {img_file}')
    img = cv.imread(img_file)
    if img.any() == None:
        print(f'Failed reading image file: {img_file}')
        exit(-1)

    while True:
        cv.imshow(f"{os.path.basename(img_file)}", img)
        key = cv.waitKey(1)
        if key == ord("c"):
            break

    cv.destroyAllWindows()
