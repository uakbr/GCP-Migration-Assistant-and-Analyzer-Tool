import subprocess
import logging
from google.cloud import run_v1

class CloudRunIntegration:
    def __init__(self, project_id, region):
        self.project_id = project_id
        self.region = region
        self.client = run_v1.ServicesClient()

    def deploy_to_cloud_run(self, service_name, image_name, allow_unauthenticated=False):
        """
        Deploys a container to Google Cloud Run.
        """
        service = {
            "api_version": "serving.knative.dev/v1",
            "kind": "Service",
            "metadata": {
                "name": service_name,
                "namespace": self.project_id
            },
            "spec": {
                "template": {
                    "spec": {
                        "containers": [
                            {
                                "image": image_name
                            }
                        ]
                    }
                }
            }
        }

        if allow_unauthenticated:
            service["metadata"]["annotations"] = {
                "run.googleapis.com/launch-stage": "BETA",
                "run.googleapis.com/ingress": "all",
                "run.googleapis.com/allow-unauthenticated": "true"
            }

        parent = f"namespaces/{self.project_id}/locations/{self.region}"
        try:
            response = self.client.create_service(parent=parent, service=service)
            service_url = response.status.url
            logging.info(f"Successfully deployed to Cloud Run. The service URL is {service_url}")
            return service_url
        except Exception as e:
            logging.error(f"Failed to deploy to Cloud Run: {e}")
            return None

    def remove_from_cloud_run(self, service_name):
        """
        Removes a service from Google Cloud Run.
        """
        service_path = f"namespaces/{self.project_id}/services/{service_name}"
        try:
            self.client.delete_service(name=service_path)
            logging.info(f"Successfully removed service {service_name} from Cloud Run.")
        except Exception as e:
            logging.error(f"Failed to remove service {service_name} from Cloud Run: {e}")

# Example usage:
# cloud_run_integration = CloudRunIntegration('your-gcp-project-id', 'your-gcp-region')
# service_url = cloud_run_integration.deploy_to_cloud_run('your-service-name', 'gcr.io/your-project-id/your-image-name', allow_unauthenticated=True)
# if service_url:
#     print(f"Service deployed at {service_url}")
# else:
#     print("Failed to deploy service. Check logs for details.")
