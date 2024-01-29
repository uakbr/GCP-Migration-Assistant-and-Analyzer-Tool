import googleapiclient.discovery
from google.oauth2 import service_account

class NetworkConfigurator:
    def __init__(self, project_id, credentials_path):
        self.project_id = project_id
        self.credentials = service_account.Credentials.from_service_account_file(
            credentials_path
        )
        self.compute = googleapiclient.discovery.build('compute', 'v1', credentials=self.credentials)

    def create_vpc_network(self, network_name):
        config = {
            "name": network_name,
            "autoCreateSubnetworks": False,  # Custom subnetworks must be created explicitly
        }
        return self.compute.networks().insert(project=self.project_id, body=config).execute()

    def create_subnetwork(self, network_name, subnetwork_name, region, ip_cidr_range):
        config = {
            "name": subnetwork_name,
            "network": f"global/networks/{network_name}",
            "ipCidrRange": ip_cidr_range,
            "region": region,
        }
        return self.compute.subnetworks().insert(project=self.project_id, region=region, body=config).execute()

    def configure_firewall_rules(self, network_name, rules):
        for rule in rules:
            firewall_config = {
                "name": rule['name'],
                "network": f"global/networks/{network_name}",
                "allowed": rule['allowed'],
                "sourceRanges": rule['source_ranges'],
            }
            self.compute.firewalls().insert(project=self.project_id, body=firewall_config).execute()

    def list_networks(self):
        return self.compute.networks().list(project=self.project_id).execute()

    def list_subnetworks(self, region):
        return self.compute.subnetworks().list(project=self.project_id, region=region).execute()

    def delete_network(self, network_name):
        return self.compute.networks().delete(project=self.project_id, network=network_name).execute()

# Example usage:
# Note: This is just an example and should be replaced with actual implementation logic.
if __name__ == "__main__":
    configurator = NetworkConfigurator('<your-gcp-project-id>', '<path-to-service-account-json>')
    print("Creating VPC network...")
    configurator.create_vpc_network('my-custom-network')
    print("Creating subnetwork...")
    configurator.create_subnetwork('my-custom-network', 'my-custom-subnetwork', 'us-central1', '10.0.0.0/20')
    print("Configuring firewall rules...")
    configurator.configure_firewall_rules('my-custom-network', [
        {
            'name': 'allow-internal',
            'allowed': [{'IPProtocol': 'tcp', 'ports': ['0-65535']}],
            'source_ranges': ['10.0.0.0/8'],
        },
        {
            'name': 'allow-external-http',
            'allowed': [{'IPProtocol': 'tcp', 'ports': ['80']}],
            'source_ranges': ['0.0.0.0/0'],
        }
    ])
    print("Listing networks...")
    print(configurator.list_networks())
    print("Listing subnetworks...")
    print(configurator.list_subnetworks('us-central1'))
    print("Deleting network...")
    configurator.delete_network('my-custom-network')
