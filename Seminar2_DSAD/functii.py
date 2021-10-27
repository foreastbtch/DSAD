import numpy as np


def nan_replace(x):
    is_nan = np.isnan(x)
    # print(is_nan)
    k = np.where(is_nan)
    # print(k)
    x[k] = np.nanmean(x[:, k[1]], axis=0)
    # axis = 0 calculul se face pe coloane
