import boto3
import subprocess
from datetime import datetime, timezone

def utc_to_local(utc_dt):
    return utc_dt.replace(tzinfo=timezone.utc).astimezone(tz=None)

def diff_dates(date1, date2):
    return abs(date2 - date1).days

resource = boto3.resource('iam')
client = boto3.client("iam")

noMail=["rtytgat", "rikregular"]

KEY = 'LastUsedDate'
needsUpdate = ""
for user in resource.users.all():
    if "sa-" in user.user_name or "ca-" in user.user_name or "ecr-" in user.user_name:
        pass
    else:
        Metadata = client.list_access_keys(UserName=user.user_name)
        if Metadata['AccessKeyMetadata']:
            for key in user.access_keys.all():
                
                AccessId = key.access_key_id
                Status = key.status
                CreatedDate = key.create_date

                numOfDays = diff_dates(utc_to_local(datetime.utcnow()), utc_to_local(CreatedDate))
                LastUsed = client.get_access_key_last_used(AccessKeyId=AccessId)

                if (Status == "Active"):
                    if KEY in LastUsed['AccessKeyLastUsed']:
                        if numOfDays > 80 and user.user_name not in needsUpdate:
                            if user.user_name in noMail:
                                print(f"{user.user_name}'s key(s) needs to be updated")
                            else:
                                needsUpdate = needsUpdate + user.user_name  + ","
subprocess.run("pbcopy", universal_newlines=True, input=needsUpdate)