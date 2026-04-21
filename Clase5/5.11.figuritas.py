import random
import numpy as np

def crear_album(figus_total):
    A = np.zeros(figus_total, dtype = np.int64)
    return A


def album_incompleto(A):
    return sum(A) == 0
