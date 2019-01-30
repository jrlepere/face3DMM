from face3DMM.image_generators.ImageGenerator import ImageGenerator


class SingleFileImageGenerator(ImageGenerator):

    def __init__(self, imageFilepath):
        self.image = cv2.imread(imageFilepath)

    def getImage(self):
        return self.image

    def open(self):
        return True

    def close(self):
        return True
