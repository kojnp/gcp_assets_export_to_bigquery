#Export to BigQuery

step 1 create pubsub topic
```
gcloud pubsub topics create assets-export-topic
```

step 2
create cloud scheduler with trigger pubsub topic
```
gcloud scheduler jobs create pubsub my-job --schedule="0 */3 * * *"
    --topic=assets-export-topic --message-body="Hello"
```

step 2
create BQ dataset
```
bq --location=US mk -d \
--description "Assets Export dataset." \
assets
```

step 3
create service account with required permissions: Cloud Asset Admin at org level if exporting org assets + local GCF execution rights (primitive Editor for a quick fix - but tighten it for production security))

step 4
create google cloud function with pubsub trigger using the code in this repo

step 5 
trigger manual execution to test all ok
or
to test locally
make sure this is added end of file
```
if __name__ == "__main__":
    export_assets(0,0)
```
then
```
gcloud iam service-accounts keys create --iam-account my-iam-account@somedomain.com key.json
export GOOGLE_APPLICATION_CREDENTIALS=./key.json
pip3 install --upgrade google-cloud-asset
python3 test.py
```
