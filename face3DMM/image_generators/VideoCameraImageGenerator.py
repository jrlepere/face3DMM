from face3DMM.image_generators.ImageGenerator import ImageGenerator


class VideoCameraInput(ImageGenerator):

    def getImage(self):
        ret, frame = self.cap.read()
        return frame

    def open(self):
        self.cap = cv2.VideoCapture(0)
        return True

    def close(self):
        self.cap.release()
        cv2.destroyAllWindows()
        return True
