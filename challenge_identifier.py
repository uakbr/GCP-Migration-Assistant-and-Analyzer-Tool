import pandas as pd

def identify_challenges(infrastructure_info):
    """
    Identify potential migration challenges based on the current IT infrastructure.

    :param infrastructure_info: A DataFrame containing details about the current infrastructure.
    :return: A dictionary containing potential challenges for each instance.
    """
    potential_challenges = {}

    # Define a list of common migration challenges
    common_challenges = [
        'OS compatibility',
        'Network bandwidth limitations',
        'Data sovereignty and compliance requirements',
        'Legacy system dependencies',
        'Custom configurations and integrations',
        # Add more common challenges as needed
    ]

    # Example criteria to identify challenges (to be expanded based on real checks)
    for index, instance in infrastructure_info.iterrows():
        instance_challenges = []

        # Check for OS compatibility issues
        if instance['os_type'] not in ['linux', 'windows']:
            instance_challenges.append('OS compatibility')

        # Check for network bandwidth limitations
        if instance['network_speed'] < 100:  # Assuming 100 Mbps as a threshold
            instance_challenges.append('Network bandwidth limitations')

        # Check for data sovereignty and compliance requirements
        if instance['data_location'] not in ['US', 'EU']:
            instance_challenges.append('Data sovereignty and compliance requirements')

        # Check for legacy system dependencies
        if instance['is_legacy']:
            instance_challenges.append('Legacy system dependencies')

        # Check for custom configurations and integrations
        if instance['has_custom_configs']:
            instance_challenges.append('Custom configurations and integrations')

        # Add the instance's challenges to the dictionary
        potential_challenges[instance['id']] = {
            'name': instance['name'],
            'challenges': instance_challenges if instance_challenges else ['No significant challenges identified']
        }

    return potential_challenges

# Example usage:
# infrastructure_info = pd.DataFrame({
#     'id': ['instance-1', 'instance-2'],
#     'name': ['MyInstance1', 'MyInstance2'],
#     'os_type': ['linux', 'solaris'],
#     'network_speed': [150, 80],
#     'data_location': ['US', 'IN'],
#     'is_legacy': [False, True],
#     'has_custom_configs': [False, True]
# })
# print(identify_challenges(infrastructure_info))
