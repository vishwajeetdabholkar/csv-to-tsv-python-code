import csv

def csv_to_tsv(inFile, outFile):
    with open(inFile,'r') as csvin, open(outFile, 'w', newline='') as tsvout:
    csvin = csv.reader(csvin, skipinitialspace=True)
    tsvout = csv.writer(tsvout, delimiter='\t',quotechar='"')

    for row in csvin:
        tsvout.writerow(row)
        
inFile = 'file 02.txt'
outFile = 'output02.txt'
csv_to_tsv(inFile, outFile)
