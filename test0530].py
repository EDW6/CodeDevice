import os
from Statistics.plotforpaper import plot_venn5, norm_tabel
labels = {'00001':1, '00010':2, '00011':3, '00100':4, '00101':5, '00110':6, '00111':7, '01000':8, '01001':9,
          '01010':10, '01011':11, '01100':12, '01101':13, '01110':14, '01111':15, '10000':16, '10001':17, '10010':18,
          '10011':19, '10100':20,  '10101':21, '10110':22, '10111':23, '11000':24, '11001':25,
          '11010':26, '11011':27, '11100':28, '11101':29 , '11110':30,'11111':31 }

os.chdir('/home/whj/output')
plot_venn5(labels)