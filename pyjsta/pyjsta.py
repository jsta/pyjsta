import numpy as np

def rep(x, times = 1, each = 1, length_out = None):
    """A clone of rstats rep

    Parameters
    ----------
    x : list

    Examples
    --------
    pyjsta.rep([1,2,3], 2, 1)
    """
    if not isinstance(times, list):
        times = [times]

    res = ''.join([str(i) * each for i in x])

    if len(times) > 1:
        res = ''.join(str(i) * m for i, m in zip(x, times))
    else:
        res = ''.join(res * times[0])

    if length_out is None:
        return res
    else:
        return res[0:length_out]

# a clone of Rstats table
# https://stackoverflow.com/a/43096495/3362993
def table(a):
    unique, counts = np.unique(a, return_counts=True)
    return np.asarray((unique, counts)).T

