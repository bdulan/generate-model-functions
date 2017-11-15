# ---------------------------------------------------------------------------------
#                            Main Python file
# Desc: Run the models
from modules import outcome as outcome, survival as survival
import pandas


def generate_model_function():

    # get dataframes and store them into pkl files
    o_df = outcome.run()
    o_df.to_pickle('test_outcome.pkl')
    
    s_df = survival.run()
    o_df.to_pickle('test_survival.pkl')

generate_model_function()