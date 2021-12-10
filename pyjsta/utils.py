import numpy as np


def rrep(x, times=1, each=1, length_out=None):
    """[summary]

    Args:
        x ([type]): [description]
        times (int, optional): [description]. Defaults to 1.
        each (int, optional): [description]. Defaults to 1.
        length_out ([type], optional): [description]. Defaults to None.

    Returns:
        [type]: [description]

    Examples:
    ```python
     utils.rrep([1,2,3], 2, 1)
    ```       
    """
    
    if not isinstance(times, list):
        times = [times]

    res = "".join([str(i) * each for i in x])

    if len(times) > 1:
        res = "".join(str(i) * m for i, m in zip(x, times))
    else:
        res = "".join(res * times[0])

    if length_out is None:
        return res
    else:
        return res[0:length_out]


def rtable(a):
    """A clone of rstats table
    https://stackoverflow.com/a/43096495/3362993

    Parameters
    ----------
    a : a list (or list-like object)

    Examples
    --------
    pyjsta.rtable([1,2,3])
    """
    unique, counts = np.unique(a, return_counts=True)
    return np.asarray((unique, counts)).T
