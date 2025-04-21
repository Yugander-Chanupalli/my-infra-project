import pulumi
from pulumi_aws import s3

bucket = s3.BucketV2('my-bucket')

s3.BucketAclV2("my-bucket-acl",
    bucket=bucket.id,
    acl="private",
    opts=pulumi.ResourceOptions(depends_on=[bucket])  # <- Explicit dependency 
)

pulumi.export('bucket_name', bucket.id)