from pyspark import SparkContext
sc = SparkContext(appName = "test")

hello = sc.textFile("/tmp/data/hello.txt")

print("HELLO:", hello.first())

hello.saveAsTextFile("/tmp/data/out")
