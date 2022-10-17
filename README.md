# PLUTO Demonstration Code
Project Logistics, UTilization and Operations (PLUTO)
 
## Clone in the Repo
Open Cloud Shell\
Clone in the `https://github.com/ROIGCP/PLUTO` repo\
    Command: `git clone https://github.com/ROIGCP/PLUTO`\
    Command: `cd PLUTO`

## GETTING PLUTO WORKING
Make sure you have a project set\
    Command: `gcloud config set project YOURPROJECTNAME`

Bucket named projectid-bucket\
    Command: `gsutil mb gs://$GOOGLE_CLOUD_PROJECT"-bucket"`
    
BigQuery Dataset called "activities"\
    Command: `bq mk activities`

BigQuery Table called "resources" - starting schema\
    Command: `bq mk --schema messages:STRING -t activities.resources`
    
Create a Cloud Function
    Python 3.9
    Trigger by Pub/Sub Message
    Use the sample in CloudFunction folder
