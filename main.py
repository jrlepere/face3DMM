import numpy as np
from sop import sop

if __name__ == '__main__':
    v = np.array([1,1,0]).T
    x = sop(v,2,3,4)
    print(x)



# https://github.com/unibas-gravis/scalismo/blob/master/src/main/scala/scalismo/mesh/TriangleMesh.scala
# https://github.com/unibas-gravis/scalismo-faces/blob/d6aa8e59718d5c7d8a6b709eaefd7b039709c2f0/src/main/scala/scalismo/faces/io/MoMoIO.scala
# http://gravis.dmi.unibas.ch/PMM/
# https://github.com/statismo/statismo
# https://github.com/unibas-gravis/basel-face-model-viewer/blob/master/src/main/scala/faces/apps/ModelViewer.scala
