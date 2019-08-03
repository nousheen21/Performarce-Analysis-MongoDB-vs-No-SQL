import pandas as pd
from sklearn.utils import shuffle

class Data_Loader():

    """
    Loads csv file into a Pandas DataFrame by shuffling all rows.
    Fragments names by poistioning, religion and gender.
    """

    def __init__(self, Data=None):
        self.dataframe = Data
        
        self.names = {
            "firstname" : 1,
            "middlename" : 2,
            "lastname" : 3,
        }
        
        self.gender = {
            "male" : 1,
            "female" : 2,
            "unisex" : 3,
        }
         
        self.religion = {
            "muslim" : 1,
            "hindu" : 2,
            "christian" : 3,
            "budhist" : 4,
        } 

    def read_csvfile(self, filename):
        self.dataframe = pd.read_csv(filename)
        self.dataframe = shuffle(self.dataframe)
        return self.dataframe

    def save_csvfile(self, filename, Data, Columns):
        self.dataframe = pd.DataFrame(Data, columns = Columns)

        self.dataframe = shuffle(self.dataframe)
        self.dataframe.to_csv(filename, index=False)
        return self.dataframe.count

    def get_all_names_by_religion(self, religion):
        results = self.dataframe.groupby('religion')['Name'].apply(list)
        all_names = results[self.religion[religion]]
        return all_names

    def get_all_names_by_gender(self, gender):
        results = self.dataframe.groupby('sex')['Name'].apply(list)
        all_names = results[self.gender[gender]]
        return all_names

    def get_all_first_middle_last_names(self):
        results = self.dataframe.groupby('Pos')['Name'].apply(list)
        return results

    def get_names_by_religion_gender(self, religion, gender):
        all_names = self.get_all_first_middle_last_names()
        
        first_names = all_names[1]
        middle_names = all_names[2]
        last_names = all_names[3]
        
        names_by_religion = self.get_all_names_by_religion(religion)
        names_by_gender = self.get_all_names_by_gender(gender)
        
        first_names_by_religion = list(set(first_names).intersection(names_by_religion))
        first_names_by_gender = list(set(first_names).intersection(names_by_gender))
        middle_names_by_religion = list(set(middle_names).intersection(names_by_religion))
        middle_names_by_gender = list(set(middle_names).intersection(names_by_gender))
        last_names_by_religion = list(set(last_names).intersection(names_by_religion))
        last_names_by_gender = list(set(last_names).intersection(names_by_gender))
        
        first_names_by_religion_gender = list(set(first_names_by_religion).intersection(first_names_by_gender))
        middle_names_by_religion_gender = list(set(middle_names_by_religion).intersection(middle_names_by_gender))
        last_names_by_religion_gender = list(set(last_names_by_religion).intersection(last_names_by_gender))
        
        return first_names_by_religion_gender, middle_names_by_religion_gender, last_names_by_religion_gender
