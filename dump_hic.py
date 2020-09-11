#!/home/yli11/.conda/envs/py2/bin/python
from joblib import Parallel, delayed

import sys
import os
import glob


hic_file_list = glob.glob("*.hic")
chrom_size = sys.argv[1]
chr_list = []
with open(chrom_size) as f:
    for line in f:
        line = line.strip().split()
        chr_list.append(line[0].replace("chr","").upper())
print (chr_list)

def dump(hic,chr):
    command = f"module load juicer_tools;java -jar /home/yli11/HemTools/share/script/jar/juicer_tools_1.21.01.jar dump oe NONE {hic} {chr} {chr} BP 250000 {hic.replace('.hic','')}_{chr}_oe.mat -d"
    print (command)
    os.system(command)
input_list=[]
for h in hic_file_list:
    for c in chr_list:
        input_list.append([h,c])
Parallel(n_jobs=10,verbose=10)(delayed(dump)(x[0],x[1]) for x in input_list)
