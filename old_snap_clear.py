import boto3
import datetime
from datetime import datetime,timedelta
import pytz
utc=pytz.UTC
expiry=datetime.now()-timedelta(32)
t11=expiry.replace(tzinfo=utc)
AK='put access key here'
SK='put secret key here'
def checkAKSK(AK,SK):
        try:
                client = boto3.client('ec2',aws_access_key_id=AK,aws_secret_access_key=SK,region_name='us-east-1')
                Region = [region['RegionName'] for region in client.describe_regions()['Regions']]
                return 1
        except Exception as e:
                return 0


if(checkAKSK(AK,SK)):
    client = boto3.client('ec2',aws_access_key_id=AK,aws_secret_access_key=SK,region_name='us-east-1')
    Region = [region['RegionName'] for region in client.describe_regions()['Regions']]
    for a in Region:

        client = boto3.client('ec2',aws_access_key_id=AK,aws_secret_access_key=SK,region_name=a)
        response= client.describe_snapshots()
        for d in response['Snapshots']:
            t22=d['StartTime'].replace(tzinfo=utc)
            if t11 > t22 :
                client.delete_snapshot(SnapshotId=d["SnapshotId"])

else:
    print 'invalid AK/SK '
