#!/usr/bin/python
# -*- coding: utf-8 -*-
 
import bibtexparser
from pylatexenc.latex2text import LatexNodes2Text

def printPaper(entry):
    author = LatexNodes2Text().latex_to_text(entry['author'].replace('\n', ' '))
    title = LatexNodes2Text().latex_to_text(entry['title'].replace('\n', ' ')) 
    year = entry['year']
    if(entry['ENTRYTYPE'] == 'article'):
        venue = entry['journal'].replace('\n', ' ')
    else:
        venue = entry['booktitle'].replace('\n', ' ') 
    venue = LatexNodes2Text().latex_to_text(venue)
    return u'   * {}. _{}_. {}. {}'.format(author, title, venue, year).encode('UTF-8')

with open('bibliography.bib') as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file)

papersByYear = {}     

for e in bib_database.entries:
    year = e['year'] 
    if year in papersByYear:
        papersByYear[year].append(e) 
    else:
        papersByYear[year] = [e]

for year in sorted(papersByYear.keys(), reverse=True):
    print('## {}'.format(year))
    for p in papersByYear[year]:
        print(printPaper(p))
        print('\n') 


