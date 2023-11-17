import numpy as np
import pandas as pd

pulsar_stars = pd.read_csv('https://courses.openedu.ru/asset-v1:ITMOUniversity+DATANFST2035+cifru_2035+type@asset+block@pulsar_stars_new.csv',
                          delimiter=',',
                          decimal='.')

#Задание 1
#Получите выборку из набора данных pulsar_stars на основании критериев
data_filter = pulsar_stars[((pulsar_stars.TG == 0) & ((pulsar_stars.MIP >= 85.5234375) & (pulsar_stars.MIP <= 86.6171875))) | 
                            ((pulsar_stars.TG == 1) & ((pulsar_stars.MIP >= 65.078125) & (pulsar_stars.MIP <= 70.7421875)))]

print(data_filter) #row = 202

#Определите выборочное среднее для столбца MIP: 
mean_MIP = data_filter['MIP'].mean()
print(round(mean_MIP, 3))   #mean = 76.901           
