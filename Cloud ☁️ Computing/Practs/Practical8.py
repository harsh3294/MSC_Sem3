#pip install pyspark

from pyspark.sql import SparkSession
from pyspark.sql.functions import col


# FIND THE S3 URI IN THE S3 BUCKET
# PATH  S3_URI/FILENAME
S3_DATA_SOURCE_PATH="s3://harshc3294awsbucket/data-source/survey_results_public.csv" 
S3_DATA_OUTPUT_PATH="s3://harshc3294awsbucket/data-output"

def main ():
    spark= SparkSession.builder.appName("HarshDemoApp").getOrCreate()
    all_data=spark.read.csv(S3_DATA_SOURCE_PATH,header=True)
    print("The total number of records int the source data : %s" % all_data.count())
    selected_data = all_data.where((col("Country")=="United States") & (col("WorkWeekHrs")>45))
    print("The number of engineers who worked more than 45 hours a week in the US are: %s" % selected_data.count())
    selected_data.write.mode("overwrite").parquet(S3_DATA_OUTPUT_PATH)
    print("Selected data was successfully saved to S3 %s"% S3_DATA_OUTPUT_PATH)

if __name__==   "__main__":
     main()