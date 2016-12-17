import cv2


class ImageUtils(object):

    @staticmethod
    def insert_sprite(sprite_img, position, background_img):
        dimensions = sprite_img.shape[:2]
        bg_dimensions = background_img.shape[:2]
        x_0 = min(max(int(position[0] - float(dimensions[0]) / 2), 0), bg_dimensions[0]-dimensions[0])
        y_0 = min(max(int(position[1] - float(dimensions[1]) / 2), 0), bg_dimensions[1]-dimensions[1])
        x_1 = min(x_0 + dimensions[0], bg_dimensions[0])
        y_1 = min(y_0 + dimensions[1], bg_dimensions[1])
        background_img[x_0:x_1, y_0:y_1] = sprite_img

    @staticmethod
    def resize_image(image, factor):
        return cv2.resize(image, None, fx=factor, fy=factor, interpolation=cv2.INTER_CUBIC)
