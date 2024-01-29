import os
import logging
from google.cloud import storage
from google.cloud.exceptions import NotFound

class DataTransferTool:
    def __init__(self):
        self.storage_client = storage.Client()

    def upload_file_to_gcs(self, source_file_path, bucket_name, destination_blob_name):
        """
        Uploads a file to a Google Cloud Storage bucket.

        :param source_file_path: Path to the source file.
        :param bucket_name: Name of the GCS bucket.
        :param destination_blob_name: Name of the destination blob.
        :return: None
        """
        try:
            bucket = self.storage_client.get_bucket(bucket_name)
            blob = bucket.blob(destination_blob_name)

            blob.upload_from_filename(source_file_path)

            logging.info(f"File {source_file_path} uploaded to {destination_blob_name} in bucket {bucket_name}.")
        except NotFound:
            logging.error(f"The bucket {bucket_name} does not exist.")
            raise
        except Exception as e:
            logging.error(f"Failed to upload file to GCS: {e}")
            raise

    def download_file_from_gcs(self, bucket_name, source_blob_name, destination_file_path):
        """
        Downloads a file from a Google Cloud Storage bucket.

        :param bucket_name: Name of the GCS bucket.
        :param source_blob_name: Name of the source blob.
        :param destination_file_path: Path to the destination file.
        :return: None
        """
        try:
            bucket = self.storage_client.get_bucket(bucket_name)
            blob = bucket.blob(source_blob_name)

            blob.download_to_filename(destination_file_path)

            logging.info(f"File {source_blob_name} downloaded to {destination_file_path}.")
        except NotFound:
            logging.error(f"The bucket {bucket_name} or blob {source_blob_name} does not exist.")
            raise
        except Exception as e:
            logging.error(f"Failed to download file from GCS: {e}")
            raise

# Example usage:
# dtt = DataTransferTool()
# dtt.upload_file_to_gcs('path/to/local/file.csv', 'my-gcs-bucket', 'destination_blob_name.csv')
# dtt.download_file_from_gcs('my-gcs-bucket', 'source_blob_name.csv', 'path/to/local/file.csv')
