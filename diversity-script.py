import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Reads the data clinical file into a data frame
clinicalDataFile = 'inputfiles/clinical_data.txt'
df = pd.read_csv(clinicalDataFile, sep='\t')
df['averages'] = ''
df['std'] = ''

#Calculates, and writes respective averages/std to data frame
for index, row in df.iterrows():
    codeName = row['code_name']
    diversityScoreFile = 'inputfiles/diversityScores/'+codeName+'.diversity.txt'
    with open(diversityScoreFile, 'r') as file:
        scores = file.read().splitlines()
        scores = list(map(float, scores))
        df.at[index, 'averages'] = np.mean(scores)
        df.at[index, 'std'] = np.std(scores)

#Writes data frame to clinical_data.stats.txt 
clinicalStatsFile = 'clinical_data.stats.txt'
df.to_csv(clinicalStatsFile, sep='\t')

#Find animals with two largest, and one lowest, diversity scores
df['averages'] = pd.to_numeric(df['averages'], errors='coerce')
largestAnimals = df.nlargest(2, 'averages')['code_name'].tolist()
smallestAnimal = df.nsmallest(1, 'averages')['code_name'].tolist()

#Plot distance matricies for found animals
foundAnimals = largestAnimals+smallestAnimal
for animal in foundAnimals:
    distanceFile = 'inputfiles/distanceFiles/'+animal+'.distance.txt'
    with open(distanceFile, 'r') as file:
        points = file.readlines()
    xValues = []
    yValues = []
    for point in points:
        pair = point.strip().split(',')
        xValues.append(pair[0])
        yValues.append(pair[1])
    
    x = np.array(xValues)
    y = np.array(yValues)
    
    plt.scatter(x,y)
    plt.title(animal+' Distance Plot')
    plt.savefig(animal+'.png')
    plt.close()
