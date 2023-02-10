# -*- coding=utf8 -*-

import pandas as pd
from Preprocessing.text_cleaning_functions import text_cleaning


"""
Author:     JGY
Creation:   1?/02
By gathering all the text from the datasets and creating the Bag of Words (BoW) space.
We create a correspondence between each sentence of the datasets and an element of the BoW space
"""

#
path_data = "./Tables/Data/"

# Import the datasets
train = pd.read_csv(path_data+"train.csv")
test = pd.read_csv(path_data+"test.csv")

