import boto3


s3 = boto3.resource('s3', endpoint_url='http://10.5.90.184',
    aws_access_key_id = 'VZZVY7DF8M3M8542823W',
    aws_secret_access_key = 'UckdxApU9bAe1kecGkUTiwBoykgQy8QH0WaLIvLL')

s3client = boto3.client('s3', endpoint_url='http://10.5.90.184',
    aws_access_key_id = 'VZZVY7DF8M3M8542823W',
    aws_secret_access_key = 'UckdxApU9bAe1kecGkUTiwBoykgQy8QH0WaLIvLL')

for bucket in s3.buckets.all():
    print('List buckets: ')
    print('bucket_name: ', bucket.name)

bucket_name = str(input('Delete bucket: '))

bk = s3.Bucket(bucket_name)
for key in bk.objects.all():
    print('deleting')
    key.delete()
print('delete sucsessfully')

