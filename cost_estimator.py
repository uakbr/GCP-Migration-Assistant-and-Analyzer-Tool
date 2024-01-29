import pandas as pd
from google.cloud import compute_v1
from google.cloud import billing

class CostEstimator:
    def __init__(self):
        self.compute_client = compute_v1.InstancesClient()
        self.billing_client = billing.CloudBillingClient()

    def estimate_cost(self, infrastructure_info):
        """
        Estimate the cost of migrating the current IT infrastructure to GCP.

        :param infrastructure_info: A DataFrame containing details about the current infrastructure.
        :return: A dictionary containing estimated monthly costs for each instance.
        """
        estimated_costs = {}

        # Define average costs per machine type in GCP (USD per month)
        # These are example values and should be updated with current GCP pricing
        gcp_machine_type_costs = {
            'n1-standard': 70,
            'n1-highmem': 100,
            'n1-highcpu': 80,
            'n2-standard': 90,
            'n2-highmem': 120,
            'n2-highcpu': 110,
            'e2-standard': 50,
            'e2-micro': 10,
            'e2-small': 20,
            'e2-medium': 30,
            # Add more machine types and costs as needed
        }

        # Calculate estimated costs for each instance
        for index, instance in infrastructure_info.iterrows():
            machine_type = instance['machine_type'].split('/')[-1]  # Extract machine type from full path
            estimated_cost = gcp_machine_type_costs.get(machine_type, 0) * instance['num_instances']
            estimated_costs[instance['id']] = {
                'name': instance['name'],
                'estimated_monthly_cost': estimated_cost
            }

        return estimated_costs

# Example usage:
# estimator = CostEstimator()
# infrastructure_info = pd.DataFrame({
#     'id': ['instance-1', 'instance-2'],
#     'name': ['MyInstance1', 'MyInstance2'],
#     'machine_type': ['zones/us-central1-a/machineTypes/n1-standard', 'zones/us-central1-a/machineTypes/e2-micro'],
#     'num_instances': [2, 3]
# })
# print(estimator.estimate_cost(infrastructure_info))
