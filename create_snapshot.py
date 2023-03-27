import boto3
import sys


# Define the volume ID and snapshot description
volume_id = sys.argv[1] #arguement 1 is volume id 
snapshot_description = sys.argv[2] #Arguemtn 2 is 'YOUR_SNAPSHOT_DESCRIPTION'
rentention_period = sys.argv[3]

region = sys.argv[4]
access_key = sys.argv[5]
secret_key = sys.argv[6]

# Set up the EC2 client
ec2 = boto3.client('ec2' ,region_name=region ,aws_access_key_id=access_key,
    aws_secret_access_key=secret_key)



# Define the tags in a dictionary
tags = {
    'Retention Period': rentention_period
}

# Create the snapshot
response = ec2.create_snapshot(
    VolumeId=volume_id,
    Description=snapshot_description
)

# Get the snapshot ID
snapshot_id = response['SnapshotId']
print(f"Snapshot {snapshot_id} created.")

# Wait for the snapshot to complete
#waiter = ec2.get_waiter('snapshot_completed')
#waiter.wait(SnapshotIds=[snapshot_id])

# Tag the snapshot
ec2.create_tags(
    Resources=[snapshot_id],
    Tags=[{'Key': key, 'Value': value} for key, value in tags.items()]
)
#print(f"Snapshot {snapshot_id} tagged with {tags}.")
