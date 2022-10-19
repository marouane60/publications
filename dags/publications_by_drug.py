import pandas
from libs import dao_layer

def add_pubmeds_for_drugs(drugsDF: pandas.DataFrame):
    pubmeds = dao_layer.get_pubmeds()

    for index, drug in drugsDF.iterrows():
        drug_pubmeds = pubmeds[pubmeds['title'].str.contains(drug['atccode'])]
        drugsDF.at[index,'pubmeds'] = drug_pubmeds.to_json()

    return drugsDF

def add_clinical_trials_for_drugs(drugsDF: pandas.DataFrame):
    clinical_trials = dao_layer.get_clinical_trials()

    for index, drug in drugsDF.iterrows():
        drug_clinical_trials = clinical_trials[clinical_trials['title'].str.contains(drug['atccode'])]
        drugsDF.at[index, 'clinical_trials'] = drug_clinical_trials.to_json()

    return drugsDF

def main_task():
    drugs = dao_layer.get_drugs()
    drugs_pubmeds = add_pubmeds_for_drugs(drugs)
    drugs_publications = add_clinical_trials_for_drugs(drugs_pubmeds)

    return drugs_publications.to_json()

if __name__ == '__main__':
    print(main_task())