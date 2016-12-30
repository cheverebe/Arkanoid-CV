import cv2
import numpy as np


class ImageUtils(object):

    @staticmethod
    def insert_sprite(sprite_img, position, background_img):
        dimensions = sprite_img.shape[:2]
        bg_dimensions = background_img.shape[:2]
        x_0 = int(position[0] - float(dimensions[0]) / 2)
        y_0 = int(position[1] - float(dimensions[1]) / 2)
        x_1 = x_0 + dimensions[0]
        y_1 = y_0 + dimensions[1]
        if x_1 <= 0 or x_0 >= bg_dimensions[0] or y_1 <= 0 or y_0 >= bg_dimensions[1]:
            return background_img
        if x_0 < 0:
            sprite_img = sprite_img[-x_0:, :]
            x_0 = 0
        if y_0 < 0:
            sprite_img = sprite_img[:, -y_0:]
            y_0 = 0
        if x_1 > bg_dimensions[0]:
            diff_x = x_1 - bg_dimensions[0]
            sprite_img = sprite_img[:-diff_x, :]
            x_1 = bg_dimensions[0]
        if y_1 > bg_dimensions[1]:
            diff_y = y_1 - bg_dimensions[1]
            sprite_img = sprite_img[:, :-diff_y]
            y_1 = bg_dimensions[1]
        # background_img[x_0:x_1, y_0:y_1] = sprite_img

        for c in range(0, 3):
            background_img[x_0:x_1, y_0:y_1, c] = \
                sprite_img[:, :, c] * (sprite_img[:, :, 3] / 255.0) + \
                background_img[x_0:x_1, y_0:y_1, c] * (1.0 - sprite_img[:, :, 3] / 255.0)

    @staticmethod
    def resize_image(image, factor):
        return cv2.resize(image, None, fx=factor, fy=factor, interpolation=cv2.INTER_CUBIC)

    @staticmethod
    def load_img_with_alpha(img_src):
        img = cv2.imread(img_src, -1)
        if img.shape[2] == 3:
            b, g, r = cv2.split(img)
            alpha = b/b * 100
            return cv2.merge([b, g, r, alpha])
        elif img.shape[2] == 4:
            return img
        else:
            raise ValueError
