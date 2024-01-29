import logging
from planning_service import PlanningService
from data_migration_service import DataMigrationService
from containerization_service import ContainerizationService
from kubernetes_integration import KubernetesIntegration
from cloud_run_integration import CloudRunIntegration
from google.cloud import compute_v1

class GCPMigrationIntegration:
    def __init__(self, project_id, zone):
        self.project_id = project_id
        self.zone = zone
        self.planning_service = PlanningService()
        self.data_migration_service = DataMigrationService()
        self.compute_client = compute_v1.InstancesClient()

    def execute_migration_plan(self):
        """
        Executes the migration plan using the services provided.
        """
        try:
            # Create a migration plan
            migration_plan = self.planning_service.create_migration_plan(self.project_id, self.zone)

            # Execute each step in the migration plan
            for step in migration_plan['steps']:
                self._execute_step(step)

            logging.info("Migration plan executed successfully.")
        except Exception as e:
            logging.error(f"Failed to execute migration plan: {e}")
            raise

    def _execute_step(self, step):
        """
        Executes a single step in the migration plan.

        :param step: A dictionary containing details about the step to execute.
        """
        try:
            step_type = step.get('type')
            if step_type == 'data_transfer':
                self._transfer_data(step)
            elif step_type == 'containerization':
                self._containerize_application(step)
            elif step_type == 'kubernetes_deployment':
                self._deploy_to_kubernetes(step)
            elif step_type == 'cloud_run_deployment':
                self._deploy_to_cloud_run(step)
            else:
                logging.warning(f"Unknown step type: {step_type}")

        except Exception as e:
            logging.error(f"Failed to execute step {step.get('name')}: {e}")
            raise

    def _transfer_data(self, step):
        """
        Transfers data as part of the migration step.

        :param step: A dictionary containing details about the data transfer step.
        """
        source_file_path = step.get('source_file_path')
        bucket_name = step.get('bucket_name')
        destination_blob_name = step.get('destination_blob_name')

        self.data_migration_service.transfer_data_to_gcs(source_file_path, bucket_name, destination_blob_name)

    def _containerize_application(self, step):
        """
        Containerizes an application as part of the migration step.

        :param step: A dictionary containing details about the containerization step.
        """
        app_directory = step.get('app_directory')
        target_image_name = step.get('target_image_name')

        containerization_service = ContainerizationService(app_directory, target_image_name)
        containerization_service.containerize_application()

    def _deploy_to_kubernetes(self, step):
        """
        Deploys an application to Kubernetes as part of the migration step.

        :param step: A dictionary containing details about the Kubernetes deployment step.
        """
        cluster_name = step.get('cluster_name')
        deployment_yaml = step.get('deployment_yaml')

        kubernetes_integration = KubernetesIntegration(self.project_id, self.zone)
        kubernetes_integration.deploy_to_cluster(cluster_name, deployment_yaml)

    def _deploy_to_cloud_run(self, step):
        """
        Deploys an application to Cloud Run as part of the migration step.

        :param step: A dictionary containing details about the Cloud Run deployment step.
        """
        service_name = step.get('service_name')
        image_name = step.get('image_name')

        cloud_run_integration = CloudRunIntegration()
        cloud_run_integration.deploy_to_cloud_run(service_name, image_name)

# Example usage:
# migration_integration = GCPMigrationIntegration('your-gcp-project-id', 'your-gcp-zone')
# migration_integration.execute_migration_plan()
