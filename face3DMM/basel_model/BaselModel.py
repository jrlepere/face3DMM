from trimesh.base import Trimesh


class BaselModel:

    def __init__(self, filepath):
        # load the basel model
        self.model = h5py.File(filepath, 'r')

        # load all of the shape and expression data
        self.shapeMean = np.array(self.model['shape']['model']['mean']) + np.array(
            self.model['expression']['model']['mean'])
        self.shapePCABasis = np.concatenate(
            [np.array(self.model['shape']['model']['pcaBasis']),
             np.array(self.model['expression']['model']['pcaBasis'])],
            axis=-1
        )
        self.shapePCAVariance = np.concatenate(
            [np.array(self.model['shape']['model']['pcaVariance']),
             np.array(self.model['expression']['model']['pcaVariance'])],
            axis=-1
        )

        '''important for matrix operations to reshape vectors to [Nx1] matrices'''
        self.shapeMean = self.shapeMean.reshape(self.shapeMean.shape + (1,))
        self.shapePCAVariance = self.shapePCAVariance.reshape(self.shapePCAVariance.shape + (1,))

        # model mesh triangles
        self.triangles = np.array(self.model['shape']['representer']['cells']).T

        self.numPoints = len(self.shapeMean) // 3
        self.numComponents = len(self.shapePCAVariance)

    def getShapeMean(self, pointIndexes=None):
        return self.shapeMean if pointIndexes is None else self.shapeMean[pointIndexes]

    def getShapePCABasis(self, pointIndexes=None):
        return self.shapePCABasis if pointIndexes is None else self.shapePCABasis[pointIndexes]

    def getShapePCAVariance(self, pointIndexes=None):
        return self.shapePCAVariance if pointIndexes is None else self.shapePCAVariance[pointIndexes]

    def getModelMeshTriangles(self):
        return self.triangles

    def getMeshScene(self, a, r, t, s):
        return self.getMesh(a, r, t, s).scene()

    def getDefaultMeshScene(self):
        a, r, t, s = Optimizer.getDefaults(self.numComponents)
        return self.getMeshScene(a, r, t, s)

    def getMesh(self, a, r, t, s):
        points = self._modelPointCombination(a)
        return self._getModelMesh(points)

    def _modelPointCombination(self, a):
        # calculate [u1, v2, w3, ..., un, vn, wn]
        points = self.shapeMean + np.matmul(self.shapePCABasis, a)
        # format the points into (3, n)
        return np.reshape(points, (3, self.numPoints), order='F')

    def _getModelMesh(self, points):
        return Trimesh(vertices=points.T, faces=self.triangles)