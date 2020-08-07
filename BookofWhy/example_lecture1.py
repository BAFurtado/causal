""" Example Lecture 1 """

import numpy as np
import pandas as pd
import statsmodels.formula.api as smf

n = 500000
C = np.random.normal(size=n)
A = .8 * np.random.normal(size=n)
K = A + .1 * np.random.normal(size=n)
X = C - 2 * A + .2 * np.random.normal(size=n)
F = 3 * X + .8 * np.random.normal(size=n)
D = -2 * X + .5 * np.random.normal(size=n)
G = D + .5 * np.random.normal(size=n)
Y = 2 * K - D + .2 * np.random.normal(size=n)
H = .5 * Y + .1 * np.random.normal(size=n)

data = pd.DataFrame({'C': C, 'A': A, 'K': K, 'X': X, 'F': F, 'D': D, 'G': G, 'Y': Y, 'H': H})

print(smf.ols('Y ~ X', data=data).fit().params, '\n biased')
print(smf.ols('Y ~ X + K', data=data).fit().params, '\n not-biased')
print(smf.ols('Y ~ X + A', data=data).fit().params, '\n not-biased')
print(smf.ols('Y ~ X + C + K', data=data).fit().params, '\n not-biased')
print(smf.ols('Y ~ X + C + F + K', data=data).fit().params, '\n not-biased')
print(smf.ols('Y ~ X + F + C + K + H', data=data).fit().params, '\n biased')
