"""
Module containing all the generic initialization functions
"""

import numpy as np
from ._init_cy import *


def init_single_unconstrained(colstart, coords, run, effect_types):
    """
    Initializes a run at random. There are three possibilities:
    'continuous' which is random between (-1, 1), categorical which is
    a random level, or from coords which selects a random coordinate from
    `coords`.

    Parameters
    ----------
    colstart : np.array(1d)
        The starting column of each factor.
    coords : list(np.array(2d) or None)
        The coordinates to sample from.
    run : np.array(2d)
        Output buffer of the function. Also returned at the end.
    effect_types : np.array(1d)
        The type of each effect in case no coordinates are specified.
    
    Returns
    -------
    run : np.array(2d)
        The randomly sampled run.
    """
    return init_single_unconstrained_cython_impl(colstart, coords, np.ascontiguousarray(run), effect_types)

def full_factorial(colstart, coords, Y=None):
    """
    Generates a full factorial design.

    Parameters
    ----------
    colstart : np.array(1d)
        The starting columns of each factor
    coords : list(np.array(2d))
        The list of possible coordinates for each factor.
    Y : np.array(2d) or None
        The output array for the full factorial design.

    Returns
    -------
    Y : np.array(2d)
        The full factorial design.
    """
    # Initialize Y
    if Y is None:
        n = np.prod([coords[i].shape[0] for i in range(len(coords))])
        Y = np.zeros((n, colstart[-1]), dtype=np.float64)

    # Create the full factorial matrix
    tile = 1
    rep = len(Y)
    for i in range(colstart.size - 1):
        rep = int(rep / coords[i].shape[0])
        Y[:, colstart[i]:colstart[i+1]] = np.tile(np.repeat(coords[i], rep, axis=0), (tile, 1))
        tile *= coords[i].shape[0]

    return Y
