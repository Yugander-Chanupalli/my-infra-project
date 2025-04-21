import pulumi
from pulumi_aws import s3

bucket = s3.BucketV2('my-bucket')

s3.BucketAclV2("my-bucket-acl",
    bucket=bucket.id,
    acl="private" 
)

pulumi.export('bucket_name', bucket.id)