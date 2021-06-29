import boto3


s3 = boto3.resource('s3', endpoint_url='',
    aws_access_key_id = '',
    aws_secret_access_key = '')

s3client = boto3.client('s3', endpoint_url='',
    aws_access_key_id = '',
    aws_secret_access_key = '')

for bucket in s3.buckets.all():
    print('List buckets: ')
    print('bucket_name: ', bucket.name)

bucket_name = str(input('Delete bucket: '))

bk = s3.Bucket(bucket_name)
for key in bk.objects.all():
    print('deleting')
    key.delete()
print('delete sucsessfully')

