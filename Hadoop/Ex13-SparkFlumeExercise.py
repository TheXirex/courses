import re

from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.flume import FlumeUtils

parts = [
    r'(?P<host>\S+)',
    r'\S+',
    r'(?P<user>\S+)',
    r'\[(?P<time>.+)\]',
    r'"(?P<request>.+)"',
    r'(?P<status>[0-9]+)',
    r'(?P<size>\S+)',
    r'"(?P<referer>.*)"',
    r'"(?P<agent>.*)"',
]
pattern = re.compile(r'\s+'.join(parts)+r'\s*\Z')

def extractStatus(line):
    exp = pattern.match(line)
    if exp:
        status = exp.groupdict()["status"]
        if status:
            return status


if __name__ == "__main__":

    sc = SparkContext(appName="StreamingFlumeLogAggregator")
    sc.setLogLevel("ERROR")
    ssc = StreamingContext(sc, 1)

    flumeStream = FlumeUtils.createStream(ssc, "localhost", 9092)

    lines = flumeStream.map(lambda x: x[1])
    statusCodes = lines.map(extractStatus)


    statusCounts = statusCodes.map(lambda x: (x, 1)).reduceByKeyAndWindow(lambda x, y: x + y, lambda x, y : x - y, 300, 5)


    sortedResults = statusCounts.transform(lambda rdd: rdd.sortBy(lambda x: x[1], False))
    sortedResults.pprint()

    ssc.checkpoint("data/checkpoint")
    ssc.start()
    ssc.awaitTermination()
