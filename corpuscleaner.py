### prior to script:
# This file is the last step in a download-to-corpus pipeline
# source: https://kairozu.github.io/updates/japanese-wiki-corpus
# First complete the download and WikiExtractor steps:

## japanese wikimedia dump (tested 02-03-2023)
## https://dumps.wikimedia.org/jawiki/20221120/jawiki-20221120-pages-articles-multistream.xml.bz2
#### attn: 3.6Gb download

## Extraction:
# !attn: requires python2, WikiExtractor.py. Took ~ 45 minutes on my machine
## $ bzcat jawiki-20221120-pages-articles-multistream.xml.bz2 | python2 WikiExtractor.py -o texts -