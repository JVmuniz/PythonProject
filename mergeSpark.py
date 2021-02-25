from pyspark.sql import SparkSession as sc

spark = sc.builder \
    .master("local") \
    .appName("Word Count") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

def swap(backtest)

df = spark.read.csv()