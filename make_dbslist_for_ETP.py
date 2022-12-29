# coding: utf-8
import os, sys
sys.path.insert(0, os.path.abspath('../../../software/pysadcp'))

from pysadcp import pysadcp
from pysadcp import process_codas_dbs_L1 as procL1

import numpy as np

sac_ids = np.load("data/sacids_etp.npz")['sacids']

data_basedir = '/work/smullersoares_work/data/adcp/jas_repo_complete/'

dbslist = [data_basedir + sacid + '/' + sacid for sacid in sac_ids]

mv1104_paths = [it.path + '/adcpdb' for it in os.scandir('/work/smullersoares_work/data/adcp/uh_repo/mv1104') if os.path.isdir(it.path) and os.path.split(it.path)[1][0] == 'o']

# dbslist = dbslist.tolist() + mv1104_paths
dbslist = dbslist + mv1104_paths

configs = procL1.RunParams(dbslist, 'data/proc_adcp', out_fname='EastTropPac')



