import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

skip = []  # list: import rows that need to skip
x1 = 11
while x1 < 135:
    skip.append(x1)
    skip.append(x1 - 1)
    skip.append(x1 - 2)
    x1 += 11

import_data = pd.read_excel(r"C:\Users\yuanshanmian\Desktop\新建 Microsoft Excel 工作表(已自动还原).xlsx", nrows=140,
                            usecols="N:R", na_values=0, skiprows=lambda x: x in skip, dtype=float)
import_data.fillna(0, inplace=True)  # nan data to 0 to calculate
array_countries_data = [import_data.iloc[i:i + 8, :] for i in
                        range(0, len(import_data), 8)]  # slice origin data to 13x8x5 (13 targets, 8 countries, 5 years)

array_target_weighted = np.zeros((5, 8, 6))  # 5 years, 8 countries, 6 blocks(include targets)

for i in range(5):  # calculate weighted targets
    array_target_weighted[i][:, 0] = np.add(array_countries_data[0].iloc[:, i].values,
                                            array_countries_data[1].iloc[:, i].values) / 2
    array_target_weighted[i][:, 1] = np.add(array_countries_data[2].iloc[:, i].values * 0.4,
                                            array_countries_data[3].iloc[:, i].values * 0.6)
    array_target_weighted[i][:, 2] = np.add(
        np.add(array_countries_data[4].iloc[:, i].values, array_countries_data[5].iloc[:, i].values),
        array_countries_data[6].iloc[:, i].values * 0.5)
    array_target_weighted[i][:, 3] = np.add(array_countries_data[8].iloc[:, i].values * 0.4,
                                            array_countries_data[7].iloc[:, i].values * 0.6)
    array_target_weighted[i][:, 4] = np.add(array_countries_data[9].iloc[:, i].values,
                                            array_countries_data[10].iloc[:, i].values) / 2
    array_target_weighted[i][:, 5] = np.add(array_countries_data[11].iloc[:, i].values * 0.7,
                                            array_countries_data[12].iloc[:, i].values * 0.3)

array_final = np.zeros((8, 5))  # 8 countries, 5 years

for i in range(5):  # sum weighted targets and weighted blocks
    array_final[:, i] = array_target_weighted[i][:, 0] * 0.2 + array_target_weighted[i][:, 1] * 0.15 + \
                        array_target_weighted[i][:, 2] * 0.25 + \
                        array_target_weighted[i][:, 3] * 0.15 + array_target_weighted[i][:, 4] * 0.125 + \
                        array_target_weighted[i][:, 5] * 0.125

# print(array_final)

year = [2016, 2017, 2018, 2019, 2020]
plt.plot(year, array_final[0], label='China')
plt.plot(year, array_final[1], label='German')
plt.plot(year, array_final[2], label='France')
plt.plot(year, array_final[3], label='UK')
plt.plot(year, array_final[4], label='India')
plt.plot(year, array_final[5], label='Japan')
plt.plot(year, array_final[6], label='Russia')
plt.plot(year, array_final[7], label='US')
ax = plt.gca()
ax.get_xaxis().set_major_locator(plt.MaxNLocator(integer=True))
plt.legend()
plt.show()
