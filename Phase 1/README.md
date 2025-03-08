## Project Phase 1

## Gavin Boley & Ellie Nash

For phase 1 of the project, we extracted all hashtags and URLs from a database of tweets. We used the results as input for wordcount first in default Apache Hadoop, then in the Spark shell.

Gavin wrote the Python code to extract the hashtags/URL (excluding some minor tweaks made to better format the output for the Hadoop operations).

Ellie performed the wordcount operations in Hadoop and Spark. 

The json Tweet inputs are in /Tweets/. The Python code is located in /Code/. 
/Output/ holds the results of each of the steps. /Output/Tweets/ has the results of Gavin's extraction, either delimited by newlines or spaces depending on the needs of the wordcount operations. /Output/Hadoop/ and /Output/Spark/ have the wordcount results for each program, respectively. 
/Logs/ holds the Hadoop logs from the data/name containers that wordcount was executed on.