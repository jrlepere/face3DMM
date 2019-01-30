import abc


class ImageGenerator(abc.ABC):

    @abc.abstractmethod
    def getImage(self):
        pass

    @abc.abstractmethod
    def open(self):
        pass

    @abc.abstractmethod
    def close(self):
        pass
