import os
import subprocess
import yaml
from google.cloud import container_v1

class KubernetesIntegration:
    def __init__(self, project_id, zone):
        self.project_id = project_id
        self.zone = zone
        self.client = container_v1.ClusterManagerClient()

    def get_cluster_info(self, cluster_name):
        """Retrieve information about the specified GKE cluster."""
        try:
            response = self.client.get_cluster(
                name=f'projects/{self.project_id}/locations/{self.zone}/clusters/{cluster_name}'
            )
            return response
        except Exception as e:
            print(f"Error retrieving cluster information: {e}")
            return None

    def create_kubernetes_deployment(self, deployment_name, image_name, replicas=1):
        """Create a Kubernetes deployment on GKE."""
        deployment = {
            "apiVersion": "apps/v1",
            "kind": "Deployment",
            "metadata": {
                "name": deployment_name
            },
            "spec": {
                "replicas": replicas,
                "selector": {
                    "matchLabels": {
                        "app": deployment_name
                    }
                },
                "template": {
                    "metadata": {
                        "labels": {
                            "app": deployment_name
                        }
                    },
                    "spec": {
                        "containers": [{
                            "name": deployment_name,
                            "image": image_name
                        }]
                    }
                }
            }
        }

        # Write the deployment spec to a YAML file
        with open(f"{deployment_name}_deployment.yaml", 'w') as file:
            yaml.dump(deployment, file)

        # Use kubectl to create the deployment
        try:
            subprocess.run(["kubectl", "apply", "-f", f"{deployment_name}_deployment.yaml"], check=True)
            print(f"Deployment {deployment_name} created successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Failed to create deployment: {e}")

    def delete_kubernetes_deployment(self, deployment_name):
        """Delete a Kubernetes deployment on GKE."""
        try:
            subprocess.run(["kubectl", "delete", "deployment", deployment_name], check=True)
            print(f"Deployment {deployment_name} deleted successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Failed to delete deployment: {e}")

# Example usage:
# k8s_integration = KubernetesIntegration('your-gcp-project-id', 'your-gcp-zone')
# cluster_info = k8s_integration.get_cluster_info('your-cluster-name')
# k8s_integration.create_kubernetes_deployment('my-app', 'gcr.io/my-project/my-app-image')
# k8s_integration.delete_kubernetes_deployment('my-app')

