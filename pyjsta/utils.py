import os
import itertools
import numpy as np
import pandas as pd  # for to_csv


def rrep(x, times=1, each=1, length_out=None):
    """> A clone of rstats rep

    Args:
        x ([type]): [description]
        times (int, optional): [description]. Defaults to 1.
        each (int, optional): [description]. Defaults to 1.
        length_out ([type], optional): [description]. Defaults to None.

    Returns:
        [type]: [description]

    Examples:
    ```python
     pyjsta.rrep([1,2,3], 2, 1)
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
    """> A clone of rstats table

    See [https://stackoverflow.com/a/43096495/3362993](https://stackoverflow.com/a/43096495/3362993)

    Args:
        a (list): or list-like object.

    Examples:
    ```python
    pyjsta.rtable([1,2,3])
    ```
    """
    unique, counts = np.unique(a, return_counts=True)
    return np.asarray((unique, counts)).T


def pdappend(x, fpath):
    """Append to csv if file does not exist

    Args:
        x (DataFrame): _description_
        fpath (_type_): _description_

    Examples:
    ```python
    from pyjsta import utils
    x = pd.DataFrame({"x":1}, index=[0])
    fpath = "test.csv"
    utils.pdappend(x, fpath)
    utils.pdappend(x, fpath)
    ```
    """
    if not os.path.exists(fpath):
        x.to_csv(fpath, index=False)
        return None

    x.to_csv(fpath, mode="a", header=False, index=False)


def r_expand_grid(col_names, list_of_lists):
    """A clone of R's expand.grid function

    Args:
        col_names (_type_): _description_
        list_of_lists (_type_): _description_

    Returns:
        _type_: _description_

    Examples:
    ```python
    col_names = ["one", "two"]
    list_of_lists = [["a", "b"], ["C", "D", "E"]]
    r_expand_grid(col_names, list_of_lists)
    ```
    """
    res = pd.DataFrame(list(itertools.product(*list_of_lists)))
    res.columns = col_names
    return res
