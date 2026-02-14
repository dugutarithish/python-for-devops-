import boto3

ec2 = boto3.client("ec2", region_name="ap-south-1")

instance_id = "i-04712386e245732a6"

ec2.start_instances(InstanceIds=[instance_id])

print("Started:", instance_id)
