import matplotlib as mpl; mpl.use('TkAgg')
import matplotlib.pyplot as plt
import pandas as pd

from easyml.factory import easy_glmnet


# Set matplotlib settings
plt.style.use('ggplot')

import os
os.chdir('./Python/examples/prostate')


if __name__ == "__main__":
    # Load data
    prostate = pd.read_table('./prostate.txt')

    # Analyze data
    easy_glmnet(prostate, 'lpsa',
                random_state=1, progress_bar=True, parallel=True,
                n_samples=10, n_divisions=10, n_iterations=5,
                alpha=1, n_lambda=200, standardize=False, cut_point=0, max_iter=1e6)
