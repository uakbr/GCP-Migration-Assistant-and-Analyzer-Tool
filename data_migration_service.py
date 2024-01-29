import os
import logging
from google.cloud import storage
from google.cloud import bigquery
from google.resumable_media import common

class DataMigrationService:
    def __init__(self):
        self.storage_client = storage.Client()
        self.bigquery_client = bigquery.Client()

    def transfer_data_to_gcs(self, source_file_path, bucket_name, destination_blob_name):
        """
        Transfer data from a local file to a GCS bucket.

        :param source_file_path: Path to the source file.
        :param bucket_name: Name of the GCS bucket.
        :param destination_blob_name: Name of the destination blob.
        :return: None
        """
        try:
            bucket = self.storage_client.get_bucket(bucket_name)
            blob = bucket.blob(destination_blob_name)

            blob.upload_from_filename(source_file_path)

            logging.info(f"File {source_file_path} uploaded to {destination_blob_name}.")
        except Exception as e:
            logging.error(f"Failed to upload file to GCS: {e}")
            raise

    def sync_data_to_bigquery(self, bucket_name, blob_name, dataset_id, table_id):
        """
        Synchronize data from a GCS bucket to a BigQuery table.

        :param bucket_name: Name of the GCS bucket.
        :param blob_name: Name of the blob in the GCS bucket.
        :param dataset_id: BigQuery dataset ID.
        :param table_id: BigQuery table ID.
        :return: None
        """
        try:
            dataset_ref = self.bigquery_client.dataset(dataset_id)
            table_ref = dataset_ref.table(table_id)

            job_config = bigquery.LoadJobConfig()
            job_config.source_format = bigquery.SourceFormat.CSV
            job_config.autodetect = True

            uri = f"gs://{bucket_name}/{blob_name}"

            load_job = self.bigquery_client.load_table_from_uri(
                uri, table_ref, job_config=job_config
            )

            load_job.result()  # Waits for the job to complete.

            logging.info(f"Data from {uri} synced to BigQuery table {table_id}.")
        except Exception as e:
            logging.error(f"Failed to sync data to BigQuery: {e}")
            raise

# Example usage:
# dms = DataMigrationService()
# dms.transfer_data_to_gcs('path/to/local/file.csv', 'my-gcs-bucket', 'destination_blob_name.csv')
# dms.sync_data_to_bigquery('my-gcs-bucket', 'destination_blob_name.csv', 'my_bigquery_dataset', 'my_bigquery_table')
