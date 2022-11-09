pig -version

Datasets:

111,John,Sales,Austin
222,Alex,Marketing,New York
333,Phiip,Operation,Sacrmento
444,Terry,Sales,New York
555,Jessi,Development,Boston

hadoop dfs -copyFromLocal "F:\Practicals\BigData\Practical Pig\input" hdfs://localhost:9000/
hadoop dfs -chmod -R a+x hdfs://localhost:9000/input/input.txt
hadoop dfs -chmod -R 1777 hdfs://localhost:9000/input/input.txt

hadoop dfs -chmod 755 hdfs://localhost:9000/input/input.txt

sudo chown -R hdfs://localhost:9000/ hdfs://localhost:9000/input/input.txt

pig -x local

employee = LOAD 'hdfs://localhost:9000/input/input.txt' USING PigStorage(',') as (ssn:chararray,name:chararray,department:chararray,city:chararray);

dump employee;

foreach_data = FOREACH employee GENERATE name,department;

dump foreach_data;

emp_filer= filter employee by city == 'Austin';

dump emp_filer;

emp_order = ORDER employee BY ssn desc;

dump emp_order;

STORE emp_filer INTO ' hdfs://localhost:9000/pigresult';

hadoop dfs -copyFromLocal "F:\Practicals\BigData\Practical Pig\log" hdfs://localhost:9000/log

pig -x local hdfs://localhost:9000/log/sampleLog.pig
