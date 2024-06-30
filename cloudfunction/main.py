# Project PLUTO Starter Code
# Assumes a dataset called activities exists
# Assumes a table call resources
# resources schema - single column:  message:string
import base64
import json
from google.cloud import bigquery
from google.cloud import compute_v1

table_id = "activities.resources"


def pubsub_to_bigquery(event, context):
    pubsub_message = base64.b64decode(event['data']).decode('utf-8')
    print("Row To Insert: " + pubsub_message)
    client = bigquery.Client()
    table = client.get_table(table_id)
    row_to_insert = [(pubsub_message,)]  # NOTE - the trailing comma is required for this case - it expects a tuple
    errors = client.insert_rows(table, row_to_insert)
    if errors == []:
        print("Row Inserted: " + pubsub_message)


def stop_vm(event, context):
    pubsub_message = base64.b64decode(event['data']).decode('utf-8')
    message_data = json.loads(pubsub_message)
    instance_client = compute_v1.InstancesClient()
    instance_name = message_data['incident']['metric']['labels']['instance_name']
    project_id = message_data['incident']['resource']['labels']['project_id']
    zone = find_instance_zone(project_id=project_id, instance_name=instance_name, client=instance_client)

    ops = instance_client.stop(project=project_id, zone=zone, instance=instance_name)
    ops_result = ops.result()


def find_instance_zone(project_id: str, instance_name: str, client) -> str:
    request = compute_v1.AggregatedListInstancesRequest(project=project_id)
    all_instances = client.aggregated_list(request)

    for zone, response in all_instances:
        for vm in response.instances:
            if vm == instance_name:
                return zone
