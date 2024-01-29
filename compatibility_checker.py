import pandas as pd

def check_compatibility(infrastructure_info):
    """
    Check the compatibility of the current IT infrastructure with GCP.

    :param infrastructure_info: A DataFrame containing details about the current infrastructure.
    :return: A dictionary containing compatibility results for each instance.
    """
    compatibility_results = {}

    # Define a list of GCP compatible machine types
    gcp_compatible_machine_types = [
        'n1-standard', 'n1-highmem', 'n1-highcpu',
        'n2-standard', 'n2-highmem', 'n2-highcpu',
        'e2-standard', 'e2-micro', 'e2-small', 'e2-medium',
        # Add more machine types as needed
    ]

    # Check each instance for compatibility
    for index, instance in infrastructure_info.iterrows():
        machine_type = instance['machine_type'].split('/')[-1]  # Extract machine type from full path
        is_compatible = machine_type in gcp_compatible_machine_types
        compatibility_results[instance['id']] = {
            'name': instance['name'],
            'compatible': is_compatible,
            'machine_type': machine_type,
            'status': instance['status'],
            'zone': instance['zone'],
            'recommendation': None if is_compatible else 'Consider changing machine type to a GCP compatible one.'
        }

    return compatibility_results
