# This program checks if there are 739 districts
from collections import Counter
import json
import pandas as pd

# Task: Capture the boundaries of 739 districts. Verify that there are 739 districts (or what is the number?)
# reads data 
with open('India.json') as f:
  data = json.load(f)

# reads data and skips first row, last couple rows
couple_rows = [0, 1, 2] 
excel = pd.ExcelFile('territories.xlsx')
sheet2 = pd.read_excel(excel, 'districts')
old_districts = pd.read_csv('reduced.csv') # get 2011 data

geometries = []
counter = 0
list1 = []
print("These districts (in JSON file) are not in the excel workbook:")
for i in range(len(data['objects']['India']['geometries'])):
  val1 = data['objects']['India']['geometries'][i]['properties']['dtname']
  val2 = data['objects']['India']['geometries'][i]['properties']['stname']
  geometries.append(val1)

  if val1 not in list(sheet2['District'].values):
    print(val1)
  elif val1 in list(sheet2['District'].values):
    list1.append(val1)
    counter += 1

print("Number of districts in JSON that are in excel workbook: " + str(len(list1)))


d =  Counter(list1)  
res = [k for k, v in d.items() if v > 1]
print("\nDuplicates in JSON file:")
print(res)


anothercounter = 0
list2 = []
print("\nThese values (in excel sheet) are not in the json file:")
for i in list(sheet2['District'].values):
  if i not in geometries:
    print(i)
  elif i in geometries:
    #print(i)
    anothercounter += 1
    list2.append(i)

print("Number of districts in excel workbook that are in JSON: " + str(len(list2)))

d =  Counter(list2)  
res = [k for k, v in d.items() if v > 1]
print("\nDuplicates in Excel Workbook:")
print(res)



print("\nTotal number of districts in JSON: " + str(len(data['objects']['India']['geometries'])))


# adds the 2011 data to the excel sheet
'''
for rows in sheet2.itertuples():
  for r in old_districts.itertuples():
    if (r._5.lower()==rows.District.lower()):
      #sheet2.loc[(sheet2['District'].lower() == old_districts['5'].lower()), 'Population(2011)'] = old_districts["11"]
      #rows.Population(2011) = r._11 
      sheet2.at[rows.Index, 'Population(2011)'] = r._11
#print(sheet2)
'''
for rows in sheet2.itertuples():
  for r in old_districts.itertuples():
    #print(r)
    if (r._5 == rows.District):
      #sheet2.loc[(sheet2['District'].lower() == old_districts['5'].lower()), 'Population(2011)'] = old_districts["11"]
      #rows.Population(2011) = r._11 
      sheet2.at[rows.Index, 'Area(2011)'] = r.area
#print(sheet2)
sheet2.to_csv('territories.csv', index=False, encoding='utf-8') 

# find out if each districts population sums up to be the states population