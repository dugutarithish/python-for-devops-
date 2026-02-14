import boto3

ec2 = boto3.client("ec2", region_name="ap-south-1")

response = ec2.run_instances(
    ImageId="ami-019715e0d74f695be",
    InstanceType="t2.micro",
    MinCount=1,
    MaxCount=1,
    KeyName="new",
    TagSpecifications=[
        {
            "ResourceType": "instance",
            "Tags": [
                {"Key": "Name", "Value": "boto3-instance"}
            ]
        }
    ]
)

instance_id = response["Instances"][0]["InstanceId"]
print("Created:", instance_id)
