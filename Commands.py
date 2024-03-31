"""

## Way to login into the Clusters master Node
ssh -i [key-pair] hadoop@[emr-master-public-dns-address]

##Creating the file in Master Node
nano spark-etl.py

##Running the spark job via the Master Node
spark-submit spark-etl.py s3://<YOUR-BUCKET>/input/ s3://<YOUR-BUCKET>/output/

##Command to be given while adding a step in EMR with the jar to be used as command-runner.jar
spark-submit s3://<bucketname>/files/spark-etl.py s3://<bucketname>/input s3://<bucketname>/output


"""