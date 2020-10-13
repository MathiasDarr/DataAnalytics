### Dakobed Kinesis Streams 


In this directory I experiment with Kinesis streams. 

aws kinesis describe-stream --stream-name test-kinesis-stream

aws kinesis get-shard-iterator --shard-id shardId-000000000000 --shard-iterator-type TRIM_HORIZON --stream-name test-kinesis-stream


SHARD_ITERATOR=$(aws kinesis get-shard-iterator --shard-id shardId-000000000000 --shard-iterator-type TRIM_HORIZON --stream-name test-kinesis-stream --query 'ShardIterator')
aws kinesis get-records --shard-iterator $SHARD_ITERATOR