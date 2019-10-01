#!/usr/bin/python

# make a dot file for an undirected graph of mainpernors

# open mainpernors csv, remove first line

import csv
import re

f=open("mainpernor-dotfile.dot","w+")
f.write("digraph D {\n");
with open('mainpernors-notitles.csv','rb') as csvfile:
    # the first line is the dude who was the criminal. The others are mainpernors.
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        print(row)
	row[0]=row[0].decode("utf-8-sig")
        #print(row[0])
	re.sub('[^A-Za-z0-9\-]+', '',row[0])
        nonzeroitemsinrow=[];
        for i in row[1:]:
	    f.write(i.lstrip('entity-')+"[color=\"green\" shape=\"circle\"]\n")
            if i!="":
                nonzeroitemsinrow.append(i.lstrip('entity-'));
	f.write(row[0].lstrip('entity-')+"[color=\"red\" shape=\"polygon\"]\n");
        f.write(row[0].lstrip('entity-')+"-> {"+",".join(nonzeroitemsinrow)+"}\n");

f.write("}\n")
