import sys
sys.path.append('../pfeature2')
from pfeature2.aac_wp import *
from pfeature2.dpc_wp import *
from pfeature2.bin_aa_nt import *
from pfeature2.bin_aa_ct import *

dataset_dir = '../dataset/'
features_dir = '../features/'

def generate_aac_features():

    aac_wp(dataset_dir + 'pos_train', features_dir + 'aac/pos_train')
    aac_wp(dataset_dir + 'neg_train', features_dir + 'aac/neg_train')
    aac_wp(dataset_dir + 'pos_valid', features_dir + 'aac/pos_valid')
    aac_wp(dataset_dir + 'neg_valid', features_dir + 'aac/neg_valid')
    aac_wp(dataset_dir + 'neg_train_rand', features_dir + 'aac/neg_train_rand')
    aac_wp(dataset_dir + 'neg_valid_rand', features_dir + 'aac/neg_valid_rand')

def generate_dpc_features():
    dpc_wp(dataset_dir + 'pos_train', features_dir + 'dpc/pos_train', 0)
    dpc_wp(dataset_dir + 'neg_train', features_dir + 'dpc/neg_train', 0)
    dpc_wp(dataset_dir + 'pos_valid', features_dir + 'dpc/pos_valid', 0)
    dpc_wp(dataset_dir + 'neg_valid', features_dir + 'dpc/neg_valid', 0)
    dpc_wp(dataset_dir + 'neg_train_rand', features_dir + 'dpc/neg_train_rand', 0)
    dpc_wp(dataset_dir + 'neg_valid_rand', features_dir + 'dpc/neg_valid_rand', 0)

def generate_nt_features():
    bin_aa_nt(dataset_dir + 'pos_train', features_dir + 'bp/nt/pos_train_n5', 5)
    bin_aa_nt(dataset_dir + 'pos_train', features_dir + 'bp/nt/pos_train_n10', 10)
    bin_aa_nt(dataset_dir + 'pos_train', features_dir + 'bp/nt/pos_train_n15', 15)

    bin_aa_nt(dataset_dir + 'neg_train', features_dir + 'bp/nt/neg_train_n5', 5)
    bin_aa_nt(dataset_dir + 'neg_train', features_dir + 'bp/nt/neg_train_n10', 10)
    bin_aa_nt(dataset_dir + 'neg_train', features_dir + 'bp/nt/neg_train_n15', 15)

    bin_aa_nt(dataset_dir + 'pos_valid', features_dir + 'bp/nt/pos_valid_n5', 5)
    bin_aa_nt(dataset_dir + 'pos_valid', features_dir + 'bp/nt/pos_valid_n10', 10)
    bin_aa_nt(dataset_dir + 'pos_valid', features_dir + 'bp/nt/pos_valid_n15', 15)

    bin_aa_nt(dataset_dir + 'neg_valid', features_dir + 'bp/nt/neg_valid_n5', 5)
    bin_aa_nt(dataset_dir + 'neg_valid', features_dir + 'bp/nt/neg_valid_n10', 10)
    bin_aa_nt(dataset_dir + 'neg_valid', features_dir + 'bp/nt/neg_valid_n15', 15)

    bin_aa_nt(dataset_dir + 'neg_train_rand', features_dir + 'bp/nt/neg_train_rand_n5', 5)
    bin_aa_nt(dataset_dir + 'neg_train_rand', features_dir + 'bp/nt/neg_train_rand_n10', 10)
    bin_aa_nt(dataset_dir + 'neg_train_rand', features_dir + 'bp/nt/neg_train_rand_n15', 15)

    bin_aa_nt(dataset_dir + 'neg_valid_rand', features_dir + 'bp/nt/neg_valid_rand_n5', 5)
    bin_aa_nt(dataset_dir + 'neg_valid_rand', features_dir + 'bp/nt/neg_valid_rand_n10', 10)
    bin_aa_nt(dataset_dir + 'neg_valid_rand', features_dir + 'bp/nt/neg_valid_rand_n15', 15)

def generate_ct_features():
    bin_aa_ct(dataset_dir + 'pos_train', features_dir + 'bp/ct/pos_train_c5', 5)
    bin_aa_ct(dataset_dir + 'pos_train', features_dir + 'bp/ct/pos_train_c10', 10)
    bin_aa_ct(dataset_dir + 'pos_train', features_dir + 'bp/ct/pos_train_c15', 15)

    bin_aa_ct(dataset_dir + 'neg_train', features_dir + 'bp/ct/neg_train_c5', 5)
    bin_aa_ct(dataset_dir + 'neg_train', features_dir + 'bp/ct/neg_train_c10', 10)
    bin_aa_ct(dataset_dir + 'neg_train', features_dir + 'bp/ct/neg_train_c15', 15)

    bin_aa_ct(dataset_dir + 'pos_valid', features_dir + 'bp/ct/pos_valid_c5', 5)
    bin_aa_ct(dataset_dir + 'pos_valid', features_dir + 'bp/ct/pos_valid_c10', 10)
    bin_aa_ct(dataset_dir + 'pos_valid', features_dir + 'bp/ct/pos_valid_c15', 15)

    bin_aa_ct(dataset_dir + 'neg_valid', features_dir + 'bp/ct/neg_valid_c5', 5)
    bin_aa_ct(dataset_dir + 'neg_valid', features_dir + 'bp/ct/neg_valid_c10', 10)
    bin_aa_ct(dataset_dir + 'neg_valid', features_dir + 'bp/ct/neg_valid_c15', 15)

    bin_aa_ct(dataset_dir + 'neg_train_rand', features_dir + 'bp/ct/neg_train_rand_c5', 5)
    bin_aa_ct(dataset_dir + 'neg_train_rand', features_dir + 'bp/ct/neg_train_rand_c10', 10)
    bin_aa_ct(dataset_dir + 'neg_train_rand', features_dir + 'bp/ct/neg_train_rand_c15', 15)

    bin_aa_ct(dataset_dir + 'neg_valid_rand', features_dir + 'bp/ct/neg_valid_rand_c5', 5)
    bin_aa_ct(dataset_dir + 'neg_valid_rand', features_dir + 'bp/ct/neg_valid_rand_c10', 10)
    bin_aa_ct(dataset_dir + 'neg_valid_rand', features_dir + 'bp/ct/neg_valid_rand_c15', 15)

generate_aac_features()
generate_dpc_features()
generate_nt_features()
generate_ct_features()
