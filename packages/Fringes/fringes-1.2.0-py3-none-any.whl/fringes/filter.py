import logging
import time

import cv2
import numpy as np

from fringes.util import vshape

logger = logging.getLogger(__name__)


def direct(b: np.ndarray) -> np.ndarray:
    """Direct illumination component.

    Parameters
    ----------
    b : np.ndarray
        Modulation

    Returns
    -------
    d : np.ndarray
        Direct illumination component.

    References
    ----------
    .. [#] `Nayar et al.,
           “Fast separation of direct and global components of a scene using high frequency illumination”,
           SIGGRAPH,
           2006.
           <https://dl.acm.org/doi/abs/10.1145/1179352.1141977>`_
    """
    return 2 * b


def indirect(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """Indirect (global) illumination component.

    Parameters
    ----------
    a : np.ndarray
        Brightness.
    b : np.ndarray
        Modulation

    Returns
    -------
    g : np.ndarray
        Indirect (global) illumination component.

    References
    ----------
    .. [#] `Nayar et al.,
           “Fast separation of direct and global components of a scene using high frequency illumination”,
           SIGGRAPH,
           2006.
           <https://dl.acm.org/doi/abs/10.1145/1179352.1141977>`_
    """
    # todo: assert videoshape of a and b

    D = a.shape[0]
    K = int(b.shape[0] / D)

    g = 2 * (a.reshape(D, 1, -1) - b.reshape(D, K, -1)).reshape(b.shape).clip(0, None)

    return g


def visibility(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """Visibility.

    Parameters
    ----------
    a : np.ndarray
        Brightness.
    b : np.ndarray
        Modulation

    Returns
    -------
    V : np.ndarray
        Visibility.
    """
    # todo: assert videoshape of a and b

    D, Y, X, C = a.shape
    K = int(b.shape[0] / D)

    V = np.minimum(
        1, b.reshape(D, K, Y, X, C) / np.maximum(a[:, None, :, :, :], np.finfo(np.float64).eps)
    )  # avoid division by zero

    return V.astype(np.float32, copy=False).reshape(D * K, Y, X, C)


def exposure(a: np.ndarray, Irec: np.ndarray, lessbits: bool = True) -> np.ndarray:
    """Exposure.

    Parameters
    ----------
    a : np.ndarray
        Brightness.
    Irec : np.ndarray
        Fringe pattern sequence.
    lessbits: bool, optional
        The camera recorded `Irec` may contain fewer bits of information than its data type can hold,
        e.g. 12 bits for dtype `uint16`.
        If this flag is activated, it looks for the maximal value in `I`
        and sets `Imax` to the same or next power of two which is divisible by two.
        Example: If `I.max()` is 3500, `Imax` is set to 4095 (the maximal value a 12bit camera can deliver).

    Returns
    -------
    E : np.ndarray
        Exposure.
    """

    if Irec.dtype.kind in "ui":
        if np.iinfo(Irec.dtype).bits > 8 and lessbits:  # data may contain fewer bits of information
            bits = int(np.ceil(np.log2(Irec.max() + 1)))  # same or next power of two
            bits += -bits % 2  # same or next power of two which is divisible by two
            Imax = 2**bits - 1
        else:
            Imax = np.iinfo(Irec.dtype).max
    else:  # float
        Imax = 1  # assume

    E = a / Imax

    return E.astype(np.float32, copy=False)


def curvature(s: np.ndarray, center: bool = False, normalize: bool = False) -> np.ndarray:  # todo: test
    """Mean curvature map.

    Computed by differentiating a slope map.

    Parameters
    ----------
    s : np.ndarray
        Slope map.
        It is reshaped to video-shape (frames `T`, height `Y`, width `X`, color channels `C`) before processing.
    center : bool, optional
        If this flag is set to True, the curvature values get centered around zero using the median.
        Default is False.
    normalize : bool
        Flag indicating whether to use the acr-tangent function
        to non-linearly map the codomain from [-inf, inf] to [-1, 1].
        Default is False.

    Returns
    -------
    c : np.ndarray
        Curvature map.
    """
    t0 = time.perf_counter()

    T, Y, X, C = vshape(s).shape
    s = s.reshape(T, Y, X, C)  # returns a view

    assert T == 2, "Number of direction doesn't equal 2."
    assert X >= 2 and Y >= 2, "Shape too small to calculate numerical gradient."

    # Gy = np.gradient(s[0], axis=0) + np.gradient(s[1], axis=0)
    # Gx = np.gradient(s[0], axis=1) + np.gradient(s[1], axis=1)
    # c = np.sqrt(Gx**2 + Gy**2)  # here only positive values!

    xdx = np.gradient(s[0], axis=0)  # 0
    xdy = np.gradient(s[0], axis=1)  # 1
    ydx = np.gradient(s[1], axis=0)  # 1
    ydy = np.gradient(s[1], axis=1)  # 0
    c = xdx + xdy + ydx + ydy

    # xdx2 = np.gradient(s[0], axis=0, edge_order=2)  # 0
    # xdy2 = np.gradient(s[0], axis=1, edge_order=2)  # 1
    # ydx2 = np.gradient(s[1], axis=0, edge_order=2)  # 1
    # ydy2 = np.gradient(s[1], axis=1, edge_order=2)  # 0
    # c2 = xdx2 + xdy2 + ydx2 + ydy2

    # todo: derivative of gaussian, LoG

    if center:
        # c -= np.mean(c, axis=(0, 1))
        c -= np.median(c, axis=(0, 1))  # Median is a robust estimator of the mean.

    if normalize:
        c = np.arctan(c) * 2 / np.pi  # scale [-inf, inf] to [-1, 1]

    logger.debug(f"{(time.perf_counter() - t0) * 1000:.0f}ms")

    return c  # .reshape(-1, Y, X, C)


# def height(curv: np.ndarray, iterations: int = 3) -> np.ndarray:  # todo: test
#     """Local height map.
#
#     It is computed by iterative local integration via an inverse laplace filter.
#     Think of it as a relief, where height is only relative to the local neighborhood.
#
#     Parameters
#     ----------
#     curv : np.ndarray
#         Curvature map.
#         It is reshaped to video-shape (frames `T`, height `Y`, width `X`, color channels `C`) before processing.
#     iterations : int, optional
#         Number of iterations of the inverse Laplace filter kernel.
#         Default is 3.
#
#     Returns
#     -------
#     h : np.ndarray
#         Local height map.
#     """
#     t0 = time.perf_counter()
#
#     kernel = np.array([[0,  1, 0], [ 1, 0,  1], [0,  1, 0]], np.float32)
#     # kernel *= iterations  # todo
#
#     curv = vshape(curv)
#     T, Y, X, C = curv.shape  # returns a view
#
#     if T == 1:
#         curv = np.squeeze(curv, axis=0)  # returns a view
#
#     if curv.min() == curv.max():
#         return np.zeros_like(curv)
#
#     h = np.zeros_like(curv)
#     for c in range(C):
#         for i in range(iterations):
#             h[..., c] = (cv2.filter2D(h[..., c], -1, kernel) - curv[..., c]) / 4
#
#     # todo: residuals
#     # filter2(kernel_laplace, h) - curvature;
#
#     logger.debug(f"{(time.perf_counter() - t0) * 1000:.0f}ms")
#
#     return h.reshape(-1, Y, X, C)
