# Given the Percentile of the score and the size of the band, assign score in each band
import numpy as np
import pandas as pd

def percentile_band(percentile, band_size = 10):
    percentile = np.array(percentile)
    band = np.ceil(percentile / (100 / band_size))
    band = np.where(band == 0, 1, band)
    return band
    
df = pd.DataFrame({'Percentile':[i for i in range(101)]})
df['Decile'] = percentile_band(df['Percentile'], band_size = 10)
df['Twentile'] = percentile_band(df['Percentile'], band_size = 20)
print(df[['Percentile', 'Decile', 'Twentile']])
