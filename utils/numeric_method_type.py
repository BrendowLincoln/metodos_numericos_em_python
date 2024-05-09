from enum import Enum


class NumericMethodType(Enum):
    BISSECTION_METHOD = 0
    SECANT_METHOD = 1
    NEWTON_METHOD = 3
    GAUSS_JACOBI_ALGEBRIC = 4
    GAUSS_JACOBI_MATRIX = 5