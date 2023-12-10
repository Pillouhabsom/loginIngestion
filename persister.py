import os

from messageValidator import check_message_validity, get_output_message
from google.cloud import bigquery

bq_client = bigquery.Client()


output_bq_tables = {
    "valid_output_table_name": os.getenv("valid_output_table_name"),
    "invalid_output_table_name": os.getenv("invalid_output_table_name")
}


def get_output_table_id(is_valid_message):
    output_project_name = os.getenv("output_project_name")
    output_dataset_name = os.getenv("output_dataset_name")
    output_table_name = output_bq_tables["valid_output_table_name"] if is_valid_message else output_bq_tables["invalid_output_table_name"]
    output_table_id = ".".join([output_project_name, output_dataset_name, output_table_name])
    return output_table_id


def persistMessage(message: str):
    is_valid_message, reason = check_message_validity(message)

    output_table_id = get_output_table_id(is_valid_message)

    output_message = [get_output_message(message, reason)]

    errors = bq_client.insert_rows_json(table=output_table_id, json_rows=output_message)
    if not errors:
        print(f"row have been added to table: {output_table_id}")
    else:
        print(f"Encountered errors while inserting row: {errors}")
    return None
