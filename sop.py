"""
Scaled Orthogonal Projection implementation for projecting 3D points to 2D positions.

Author: Jake Lepere
Date: 09/01/2018
"""

import numpy as np

def sop(v, R, t, s):
    """
    Scaled Orthogonal Projection.
    SOP[v,R,t,s] = scRv+st

    Args:
      v: 3D point
      R: rotation matrix
      t: 2D translation
      s: scale
    """

    c = np.array([
                [1,0,0],
                [0,1,0]])

    return np.matmul(c,v)
