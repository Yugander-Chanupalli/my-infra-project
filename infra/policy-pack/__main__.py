from pulumi_policy import PolicyPack, ResourceValidationPolicy, ReportViolation, EnforcementLevel

def s3_bucket_policy_validator(args, report_violation: ReportViolation):
    acl = None
    if args.resource_type == "aws:s3/bucketV2:BucketV2":
        acl = args.props.get("acl")
    elif args.resource_type == "aws:s3/bucketAclV2:BucketAclV2":
        acl = args.props.get("acl")
    else:
        return

    if acl in ["public-read", "public-read-write"]:
        report_violation(
            f"S3 bucket '{args.name}' must not be public (acl={acl})."
        )

PolicyPack(
    name="secure-aws-policies",
    policies=[
        ResourceValidationPolicy(
            name="no-public-s3-buckets",
            description="Prohibits public S3 buckets by ACL settings.",
            validate=s3_bucket_policy_validator,
            enforcement_level=EnforcementLevel.MANDATORY,  # ✅ Blocks deployment
        ),
    ],
)
