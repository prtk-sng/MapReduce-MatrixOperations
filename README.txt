Matrix Operation
Prateek Kumar Singh

The folder contains 5 files:

Code Development
mapper.pyreducer.py
run.shPerformance AnalysisReport.pdfalong with README making a total of 5.

Note: The arguments of the mapper in run.sh must be specified based on the 
Orders of the test matrices. The Mapper takes 6 arguments as per rows and 
column numbers of all three matrices. For the matrices M, N, and X, the format 
of the Mapper arguments is "mapper.py M_row M_col N_row N_col X_row X_col"

To run the code, please make sure that the test matrices are in the .txt format
where the 1st column specifies the matrix, 2nd column specifies the row, and then 
the row of the matrix. Please ensure that matrix M is specified by 1, N by 2 and 
X by 3. After this is done, scp all the files for task 1 to jumphost and then hadoop.
Upload the input files to HDFS, change mode for the run.sh using chmod +x run.sh. 
Now execute ./run.sh