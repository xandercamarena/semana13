# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1TTQXYMP4yo4PHt3EBCSwrwWRwz6JD9DR
"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, expr, mean, corr

spark = SparkSession.builder.appName("Estadistica").getOrCreate()

spark.stop()

spark

data = [("Elvis", 32),("Juan", 24),("Ronaldo", 30),("Pablo", 28),("Alexis", 20),("Cris", 27),("Ana", 30),("Carlos", 21),("Carlos", 19)]
columns = ["Nombre", "Edad"]
variable = spark.createDataFrame(data,columns)

variable.select(mean(col("Edad")).alias("Media")).collect()[0]["Media"]

variable.select(mean(col("Edad")).alias("Media")).show()

var_mediana = variable.approxQuantile("Edad",[0.5],0.0)

print("La mediana es:", var_mediana)

var_moda = variable.groupBy("Edad").count().orderBy(col("count").desc()).first()

print("La moda es:",var_moda["Edad"])

data_var = [(9,9),(4,3),(5,2),(4,1),(9,2),(2,3),(1,4),(5,9),(4,1),(3,1),(2,7),(7,3),(2,4),(6,4)]
columns_var = ["var1","var2"]
variable_corr = spark.createDataFrame(data_var, columns_var)

correlacion = variable_corr.select(corr(col("var1"),col("var2")).alias("correlacion")).collect()[0]["correlacion"]

print("La correlacion es:", correlacion)

csv=spark.read.csv("/content/Xander.csv",header=True, inferSchema=True)
columns = ["Alumnos", "Notas"]
variable = spark.createDataFrame(data,columns)

csv.show()

variable.select(mean(col("Notas")).alias("Media")).collect()[0]["Media"]

spark.read.csv= csv.groupBy("Notas").count().orderBy(col("count").desc()).first()