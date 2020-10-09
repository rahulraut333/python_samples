"""
module to create spark dataframe and perform various operations on it.
"""
import pyspark

def create_spark_context():
    """
    Creates spark context.
    """
    sc = spark.sparkContext(server, port , cores, memory)
    return sc

def json_df(sc, path):
    """
    Creates spark dataframe by reading json files from a path
    Also performs some basic operation on DF.
    """
    emp_df = spark.read.json(path)
    emp_df.printSchema()
    #create temp table.
    emp_df.createOrReplaceTempView("employee")

    #create dataframe using some data of table
    new_df = spark.sql("SELECT * FROM employee where employee_salary > 10000")
    new_df.show()
    #new_df.show(5)    

json_df(r"F:\rahul\demo\json_store")
