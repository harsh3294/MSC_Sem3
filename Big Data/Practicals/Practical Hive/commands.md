## Commands to executing the hive

[Click here to check the standard setup](https://medium.com/analytics-vidhya/hive-how-to-install-in-5-steps-in-windows-10-cf56579bfb69)

=====================================================================================================

**_NOTE:_** Start all the hadoop services.

=====================================================================================================

## Starting hive meta store server

hive --service metastore

=====================================================================================================

## hive server 2

hive --service hiveserver2 --hiveconf hive.server2.thrift.port=10001 --hiveconf hive.root.logger=INFO,console

https://stackoverflow.com/questions/46030458/how-to-fix-missing-version-in-readmessagebegin-old-client-when-connecting-to

=====================================================================================================

## xml formatter

[XML Formatter](https://www.freeformatter.com/xml-formatter.html#before-output)

[Medium Link for installation](https://medium.com/analytics-vidhya/hive-how-to-install-in-5-steps-in-windows-10-cf56579bfb69)

[Kontext link for installation](https://kontext.tech/article/291/apache-hive-300-installation-on-windows-10-step-by-step-guide)

[Towards data science link for installation](https://towardsdatascience.com/installing-apache-hive-3-1-2-on-windows-10-70669ce79c79)

=====================================================================================================

## Create a database:

create database demo;

## To Check the database:

Show Databases;

## Create a managed table in demo database:

create table employee(ID int ,Name string,Salary float, Age int) row format delimited fields terminated by ',' ;

## Describe Table:

describe employee;

## To Check whether the table created is managed table or external table:

describe formatted employee;

## Create an external table in demo database:

create external table employee2(ID int ,Name string,Salary float, Age int) row format delimited fields terminated by ',' stored as textfile ;

## Describe Managed Table:

describe employee2;

## To Check whether the table created is managed table or external table:

describe formatted employee2;

## Creating the external table at the specified location

create external table employee3(ID int ,Name string,Salary float, Age int) row format delimited fields terminated by ',' location 'hdfs://localhost:9000/hivedb/demoemp3';

## Renaming the table

Alter table employee3 RENAME to emptable;

## Describe Renamed Table:

describe emptable;

## Altering / Adding columns in the table

Alter table emptable add columns (Surname string);

## Describing table after adding columns

describe emptable;

## ALtering / Renaming existing columns in the table

Alter table emptable change name first_name string;

## Describing table after renaming the column

describe emptable;

# Partitioning

## Creating a new Database with the name Student

create database student;

## Setting the default database

use student;

## Creating a table using partition with the name Student:

create table Student(ID int ,Name string, Age int) partitioned by (Course string) row format delimited fields terminated by ',' ;

## Describe Student Table:

describe Student;

## Loading the Student.csv file to the hdfs:

hadoop dfs -copyFromLocal "F:\Practicals\BigData\Practical Hive\Student.csv" hdfs://localhost:9000/Harsh/Student

## Loading the data into the partition

#### Course = Hadoop

load data inpath "hdfs://localhost:9000/Harsh/Student" into table Student partition (course= "Hadoop");

#### Course = Java

load data inpath "hdfs://localhost:9000/Harsh/Student" into table Student partition (Course="Java");

#### Course = Python

load data inpath "hdfs://localhost:9000/Harsh/Student" into table Student partition (Course="Python");

## Retriving the data from the Student where Course is Java:

<p> select * from Student where Course="Java"; </p>

# Dynamic Partitioning

## Creating a new Database with the name Student2

create database student2;

## Setting the default database

use student2;

## Setting the dynamic partition execution

set hive.exec.dynamic.partition = true;

## Setting the dynamic partition execution mode

set hive.exec.dynamic.partition.mode = nonstrict;

## Creating a table with the name Student2:

create table Student2(ID int ,Name string,Course string, Age int) row format delimited fields terminated by ',' ;

## Loading the Student.csv file to the hdfs:

hadoop dfs -copyFromLocal "F:\Practicals\BigData\Practical Hive\Student.csv" hdfs://localhost:9000/Harsh/Student;

## Loading the data into the partition

load data inpath "hdfs://localhost:9000/Harsh/Student" into table Student2;

## Create the student_part table for the dynamic partition

create table Student_Part(ID int ,Name string, Age int) partitioned by (Course string) row format delimited fields terminated by ',' ;

## Insert into the student_part table

insert into Student_Part partition(Course) Select ID,Name,Course,Age from Student2;

## Reading the data from the student_part table:

<p>Select * from Student_Part; </p>

# Bucketing

## Craete a database with the name tempbucket

create database tempbucket;

## Setting the default database

use tempbucket;

## Creating a table with the name empbucket:

create table empbucket(ID int ,Name string,Salary float, Age int) row format delimited fields terminated by ',' ;

## Loading the Employee.csv file to the hdfs:

hadoop dfs -copyFromLocal "F:\Practicals\BigData\Practical Hive\Employee.csv" hdfs://localhost:9000/Harsh/Employee;

## Setting the bucket

set hive.enforce.bucketing=true;

## Create a table with the name empbucket2 with 3 Buckets:

create table empbucket2 (ID int,Name string,Salary float,Age int) clustered by (ID) into 3 buckets row format delimited fields terminated by ',';

## inserting the records from empbucket to empbucket2

<p>

insert overwrite table empbucket2 select \* from empbucket;

</p>

# Performing the HQL query

## Craete a database with the name hiveql

create database hiveql;

## Setting the default database

use hiveql;

## Creating a table with the name emloyee:

create table employee(ID int ,Name string,Salary float, Age int) row format delimited fields terminated by ',' ;

## Loading the Employee.csv file to the hdfs:

hadoop dfs -copyFromLocal "F:\Practicals\BigData\Practical Hive\Employee.csv" hdfs://localhost:9000/Harsh/Employee;

## Loading the data into the employee

load data inpath "hdfs://localhost:9000/Harsh/Employee" into table employee;

## Get all the records from the employee table:

<p>select * from employee;</p>

## Display all the records and add 5000rs in salary for all the employee:

select ID,Name,Salary + 5000 from employee;

## Display all the records and remove 1000rs from salary for all the employee:

select ID,Name,Salary - 1000 from employee;

## Display all the records from employee whose salary is 15000 and greater:

select ID,Name,Salary,Age from employee where salary >= 15000;

## Display all the records from employee whose salary is less than 15000:

select ID,Name,Salary,Age from employee where salary < 15000;

# Hive Functions

## Square root

Select ID,Name,sqrt(Salary),Age from employee;

## Max Function :

Select max(Salary) from employee;

## Min Function :

Select min(Salary) from employee;

## Upper case function:

select ID, upper(Name) from employee;

## Lowae case function:

select ID, lower(Name) from employee;

# Group By

## Craete a database with the name empgroup

create database empgroup;

## Setting the default database

use empgroup;

## Creating a table with the name emloyee:

create table employee(ID int ,Name string,Salary float, Age int,Country string) row format delimited fields terminated by ',' ;

## Loading the Employee2.csv file to the hdfs:

hadoop dfs -copyFromLocal "F:\Practicals\BigData\Practical Hive\Employee2.csv" hdfs://localhost:9000/Harsh/Employee2;

## Loading the data into the employee

load data inpath "hdfs://localhost:9000/Harsh/Employee2" into table employee;

## Get the Total Salary by the country wise

Select Country,Sum(Salary) from employee group by Country;

## Get the Total Salary by the country wise having the sum greater than or equal to 25000

Select Country,Sum(Salary) from employee group by Country having sum(Salary)>=25000;
