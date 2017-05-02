#!/usr/bin/python
# -*- coding: utf8 -*-

import os
import numpy as np
import pandas as pd
import matplotlib as plt
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import pandas as pd
from pyFTS.partitioners import Grid
from pyFTS.common import FLR,FuzzySet,Membership,Transformations
from pyFTS import fts,hofts,ifts,pwfts,tree, chen
from pyFTS.benchmarks import benchmarks as bchmk
from pyFTS.benchmarks import Measures
from numpy import random

#gauss_treino = random.normal(0,1.0,1600)
#gauss_teste = random.normal(0,1.0,400)


os.chdir("/home/petronio/dados/Dropbox/Doutorado/Codigos/")

enrollments = pd.read_csv("DataSets/Enrollments.csv", sep=";")
enrollments = np.array(enrollments["Enrollments"])

import importlib
import pandas as pd
from pyFTS.partitioners import Grid
from pyFTS.common import FLR, FuzzySet, Membership, SortedCollection
from pyFTS import fts
from pyFTS import hofts
from pyFTS import pwfts
from pyFTS import tree
from pyFTS.benchmarks import benchmarks as bchmk

enrollments_fs1 = Grid.GridPartitioner(enrollments, 6).sets
for s in enrollments_fs1:
    print(s)

pfts1_enrollments = pwfts.ProbabilisticWeightedFTS("1")
pfts1_enrollments.train(enrollments, enrollments_fs1, 1)
pfts1_enrollments.shortname = "1st Order"
pfts2_enrollments = pwfts.ProbabilisticWeightedFTS("2")
pfts2_enrollments.dump = False
pfts2_enrollments.shortname = "2nd Order"
pfts2_enrollments.train(enrollments, enrollments_fs1, 2)
pfts3_enrollments = pwfts.ProbabilisticWeightedFTS("3")
pfts3_enrollments.dump = False
pfts3_enrollments.shortname = "3rd Order"
pfts3_enrollments.train(enrollments, enrollments_fs1, 3)

bchmk.plot_compared_series(enrollments,[pfts1_enrollments,pfts2_enrollments, pfts3_enrollments],
                           ["red","blue","green"], linewidth=2,
                         typeonlegend=True,save=False,file="pictures/pwfts_enrollments_interval.png",
                           tam=[20,7],points=False, intervals=True)






