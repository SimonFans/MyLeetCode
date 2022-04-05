# convert 11012021 to 2021-01-11
# series -> datetime -> current format -> desired format
pd.to_datetime(pd.Series('11012021'), format='%d%m%Y').dt.strftime('%Y-%m-%d')
