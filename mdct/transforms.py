""" Module for calculating DCT type 4 using FFT and pre/post-twiddling

"""

from __future__ import division
import numpy
import scipy

__all__ = [
    'mdct', 'imdct',
    'mdst', 'imdst',
    'cmdct', 'icmdct',
]


def mdct(x):
    """ Calculate modified discrete cosine transform of input signal

    Parameters
    ----------
    X : array_like
        The input signal

    Returns
    -------
    out : array_like
        The output signal

    """
    return numpy.real(cmdct(x))


def imdct(X):
    """ Calculate inverse modified discrete cosine transform of input signal

    Parameters
    ----------
    X : array_like
        The input signal

    Returns
    -------
    out : array_like
        The output signal

    """
    return numpy.real(icmdct(X))


def mdst(x):
    """ Calculate modified discrete sine transform of input signal

    Parameters
    ----------
    X : array_like
        The input signal

    Returns
    -------
    out : array_like
        The output signal

    """
    return numpy.imag(cmdct(x))


def imdst(X):
    """ Calculate inverse modified discrete sine transform of input signal

    Parameters
    ----------
    X : array_like
        The input signal

    Returns
    -------
    out : array_like
        The output signal

    """
    return numpy.imag(icmdct(X))


def cmdct(x):
    """ Calculate complex MDCT of input signal

    Parameters
    ----------
    x : array_like
        The input signal

    Returns
    -------
    out : array_like
        The output signal

    """
    N = len(x)
    n0 = (N / 2 + 1) / 2

    X = scipy.fftpack.fft(
        x * numpy.exp(-1j * 2 * numpy.pi * numpy.arange(N) / 2 / N)
    )

    return X[:N/2] * numpy.exp(
        -1j * 2 * numpy.pi * n0 * (numpy.arange(N / 2) + 0.5) / N
    )


def icmdct(X):
    """ Calculate inverse complex MDCT of input signal

    Parameters
    ----------
    X : array_like
        The input signal

    Returns
    -------
    out : array_like
        The output signal

    """
    N = 2 * len(X)
    n0 = (N / 2 + 1) / 2

    Y = numpy.zeros(N, dtype=X.dtype)

    Y[:N/2] = X
    Y[N/2:] = -1 * X[::-1]

    y = scipy.fftpack.ifft(
        Y * numpy.exp(1j * 2 * numpy.pi * numpy.arange(N) * n0 / N)
    )

    return 2 * y * numpy.exp(
        1j * 2 * numpy.pi * (numpy.arange(N) + n0) / 2 / N
    )
