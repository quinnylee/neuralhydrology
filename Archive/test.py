import pandas as pd


df = pd.read_parquet('/media/volume/NeuralHydrology/Test_Quinn_Data/forty_year_test_data/attributes/nwm_analysis_AL_atts.parquet')
print(len(df))