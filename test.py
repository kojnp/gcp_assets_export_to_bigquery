import base64
import time
from google.cloud import asset_v1
from google.cloud.asset_v1.proto import asset_service_pb2

def export_assets(event, context):
    """Triggered from a message on a Cloud Pub/Sub topic.
    Args:
        event (dict): Event payload.
        context (google.cloud.functions.Context): Metadata for the event.
    """


    #pubsub_message = base64.b64decode(event['data']).decode('utf-8')
    #print(pubsub_message)

    ts = time.time()
    print(ts)

    # TODO project_id = 'Your Google Cloud Project ID'
    # TODO dump_file_path = 'Your asset dump file path'
    
    client = asset_v1.AssetServiceClient()
    parent = 'organizations/940264541059'
    output_config = asset_service_pb2.OutputConfig()
    #projects/projectId/datasets/datasetId
    output_config.bigquery_destination.dataset = 'projects/ml-sme-223918/datasets/assets'
    table_name = "gcf_assets_exp_" + str(ts)
    #gcf_assets_exp_1593129481.6903338 -> "." not allowed in a BQ table name
    table_name2 = table_name.replace(".","_")
    print(table_name2)
    
    output_config.bigquery_destination.table = table_name2
    print(output_config.bigquery_destination.table)
    asset_types = ["compute.googleapis.com/SslCertificate"]
    response = client.export_assets(parent, output_config, asset_types=asset_types, content_type="RESOURCE")
    print(response.result())
    

if __name__ == "__main__":
    export_assets(0,0)