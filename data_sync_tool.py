import logging
from google.cloud import storage
from google.cloud.exceptions import NotFound
from google.cloud import bigquery

class DataSyncTool:
    def __init__(self):
        self.storage_client = storage.Client()
        self.bigquery_client = bigquery.Client()

    def sync_files_between_buckets(self, source_bucket_name, source_blob_name, destination_bucket_name, destination_blob_name):
        """
        Synchronize files between two GCS buckets.

        :param source_bucket_name: Name of the source GCS bucket.
        :param source_blob_name: Name of the source blob.
        :param destination_bucket_name: Name of the destination GCS bucket.
        :param destination_blob_name: Name of the destination blob.
        :return: None
        """
        try:
            source_bucket = self.storage_client.get_bucket(source_bucket_name)
            source_blob = source_bucket.blob(source_blob_name)
            destination_bucket = self.storage_client.get_bucket(destination_bucket_name)
            
            # Create a new blob in the destination bucket and copy content from the source blob
            destination_blob = destination_bucket.blob(destination_blob_name)
            source_bucket.copy_blob(source_blob, destination_bucket, destination_blob_name)

            logging.info(f"File {source_blob_name} from bucket {source_bucket_name} synchronized to {destination_blob_name} in bucket {destination_bucket_name}.")
        except NotFound:
            logging.error(f"One of the buckets {source_bucket_name} or {destination_bucket_name} does not exist.")
            raise
        except Exception as e:
            logging.error(f"Failed to synchronize files between buckets: {e}")
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
            job_config.write_disposition = bigquery.WriteDisposition.WRITE_TRUNCATE
            job_config.source_format = bigquery.SourceFormat.CSV
            job_config.autodetect = True

            uri = f"gs://{bucket_name}/{blob_name}"

            load_job = self.bigquery_client.load_table_from_uri(
                uri, table_ref, job_config=job_config
            )

            load_job.result()  # Waits for the job to complete.

            logging.info(f"Data from {uri} synchronized to BigQuery table {table_id}.")
        except Exception as e:
            logging.error(f"Failed to synchronize data to BigQuery: {e}")
            raise

# Example usage:
# dst = DataSyncTool()
# dst.sync_files_between_buckets('source-gcs-bucket', 'source_blob_name.csv', 'destination-gcs-bucket', 'destination_blob_name.csv')
# dst.sync_data_to_bigquery('my-gcs-bucket', 'destination_blob_name.csv', 'my_bigquery_dataset', 'my_bigquery_table')
