import pandas as pd
import numpy as np

"""

For the sake of simplicity, this script specifically takes the anectodes.csv file and extracts the information from there. It is not intended to work with any .csv file.

"""

class Anekdoot:

    def __init__(self, file_path):
        self.file_path = file_path

    def read_dataframe(self):
        # Skip row 0 (generic Column1, Column2...), use row 1 as header
        return pd.read_csv(self.file_path, sep=';', encoding='latin-1', skiprows=1)

    def extract_main_col(self, dataframe, col_name):
        return dataframe[col_name]

    def dataframe_size(self, dataframe):
        return dataframe.size

    def dataframe_shape(self, dataframe):
        return dataframe.shape