
import boto3


# sqs = boto3.resource('sqs')
#
# queue = sqs.create_queue(QueueName='alex-test2', Attributes={'DelaySeconds': '5'})
#
# print queue.url
# print (queue.attributes.get('DelaySeconds'))
#
# result = queue.delete(QueueUrl=queue.url)
#
# print result

s3 = boto3.client('s3')

bucket = s3.create_bucket('alex.balakersky.test2')

s3.list_buckets()

