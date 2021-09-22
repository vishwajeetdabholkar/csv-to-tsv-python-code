import csv

def csv_to_tsv(inFile, outFile):    
    # code to convert txt file to tsv file
    with open('file 02.txt','r') as csvin, open('output02.txt', 'w', newline='') as tsvout:
        csvin = csv.reader(csvin, skipinitialspace=True)
        tsvout = csv.writer(tsvout, delimiter='\t',quotechar='"')

        for row in csvin:
            tsvout.writerow(row)
        
inFile = 'file 02.txt'
outFile = 'output02.txt'
csv_to_tsv(inFile, outFile)
