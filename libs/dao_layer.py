import pandas

def get_drugs():
    return pandas.read_csv("../resources/drugs.csv")

def get_pubmeds():
    return pandas.read_csv("../resources/pubmed.csv")

def get_clinical_trials():
    return pandas.read_csv("../resources/clinical_trials.csv")