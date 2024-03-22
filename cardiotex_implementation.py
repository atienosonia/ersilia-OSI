import cardiotox

import pandas as pd
from sklearn.metrics import roc_auc_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import balanced_accuracy_score
from sklearn.metrics import matthews_corrcoef

import numpy as np

model = cardiotox.load_ensemble()

test_set_pos = pd.read_csv("data/external_test_set_pos.csv")
test_set_neg = pd.read_csv("data/external_test_set_neg.csv")
test_set_new = pd.read_csv("data/external_test_set_new.csv")

pos_smiles = list(test_set_pos["smiles"])
y_test_ex_fp_pos = test_set_pos["ACTIVITY"]

neg_smiles = list(test_set_neg["smiles"])
y_test_ex_fp_neg = test_set_neg["ACTIVITY"]

new_smiles = list(test_set_new["smiles"])
y_test_ex_fp_new = test_set_new["ACTIVITY"]

###################### Stack ensemble for POSITIVELY BIASED TEST DATA ########################################

pred_test_external_stack_pos = model.predict(pos_smiles)

# store predictions in a dataframe
# store dataframe predictions in a csv file
pd.DataFrame(pred_test_external_stack_pos).to_csv("data/pred_external_test_set_pos.csv", header=['predictions'], index = False) 

###################### Stack ensemble for NEGATIVELY BIASED TEST DATA ########################################

pred_test_external_stack_neg = model.predict(neg_smiles)

# store predictions in a dataframe
# store dataframe predictions in a csv file
pd.DataFrame(pred_test_external_stack_neg).to_csv("data/pred_external_test_set_neg.csv", header=['predictions'], index = False)


###################### Stack ensemble for NEW BIASED TEST DATA ########################################

pred_test_external_stack_new = model.predict(new_smiles)

# have predictions in a pandas dataframe
# store the predictions in a csv file
pd.DataFrame(pred_test_external_stack_new).to_csv("data/pred_external_test_set_new.csv", header=['predictions'], index = False)