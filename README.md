# Indexing-and-scoring

Boolean Query and Inverted Index

The project deals with calculating a TF-IDF score to rank and sort the query results.

<b> Given : </b>

A sample input text file consisting of Doc IDs and sentences. 

<b> Task : </b>

Build an inverted index using the information extracted from the given data. 
Storing the index and implementing a Document-at-a-time (DAAT) strategy to return Boolean query results. 
Calculating a TF_IDF score to rank and sort the query results.

<b> Input Dataset : </b>

input_corpus.txt is a tab-delimited file where each line is a document; the first field is the document ID, and the second is a sentence. The two fields are separated by a tab.

Example: 

1839  Feeling inspired? Make a meal for your family or roommates

1875  Make an effort to get to know someone you don’t usually talk to.

<b> Output : </b>

GetPostings 

term0 term1

DaatAnd term0 term1

TF-IDF term0 term1

DaatOr term0 term1

TF-IDF term0 term1

GetPostings 

term2 term3 term4 term5 term6 term7DaatAnd term2 term3 term4 term5 term6 term7

TF-IDF term2 term3 term4 term5 term6 term7

DaatOr term2 term3 term4 term5 term6 term7

TF-IDF term2 term3 term4 term5 term6 term7

GetPostings term8 term9 term10

DaatAnd term8 term9 term10

TF-IDF term8 term9 term10

DaatOr term8 term9 term10

TF-IDF term8 term9 term10
