## Diversity Script
#### Calculates diversity scores, and visualizes respective distance matricies of the data.
#### Vivek M. - 12/17/2024
### Description
A single Python script named diversity-script.py that generates an updated clinical data file with
average diversity scores, and standard deviation. Also generates scatter plots of animals with the largest
average diversity score (2), and smallest diversity score.

Input:

clinical_data.txt   Tabulated TXT file containing information regarding animals from dataset
diversityScores     Directory containing TXT files for diversity scores of every animal found in clinical_data.txt
distanceFiles       Directory containing TXT files for distance matricies of every animal found in clinical_data.txt


Output:

PNG files (3) for scatterplot of distance matricies of the animals with two largest diversity score, and the one with the smallest diversity score.
TXT file containing clinical data of animals with additional average diversity score, and standard deviation column.

How to Run:

To execute the script, navigate to the directory containing the script file (ensuring the inputfiles folder is in the same directory) and run:

pip install pandas
pip install numpy
pip install matplotlib
chmod +X diversity-script.py
python3 diversity-script.py
