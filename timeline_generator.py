import pandas as pd
from datetime import datetime, timedelta

def generate_timeline(assessment_results, resource_allocation):
    """
    Generate a detailed timeline for the migration process based on the assessment results and resource allocation.

    :param assessment_results: A dictionary containing assessment results.
    :param resource_allocation: A dictionary containing resource allocation details.
    :return: A DataFrame containing the timeline for each step of the migration process.
    """
    # Define the steps involved in the migration process
    migration_steps = [
        'Initial Assessment',
        'Planning and Design',
        'Data Migration',
        'Application Containerization',
        'Network and Security Configuration',
        'Migration Execution',
        'Validation and Testing',
        'Optimization',
        'Training and Documentation',
        'Go Live'
    ]

    # Create a DataFrame to hold the timeline information
    timeline_df = pd.DataFrame(columns=['Step', 'Start Date', 'End Date', 'Duration', 'Dependencies'])

    # Set a start date for the migration process
    start_date = datetime.now()

    # Example durations for each step (in days)
    step_durations = {
        'Initial Assessment': 5,
        'Planning and Design': 10,
        'Data Migration': 15,
        'Application Containerization': 10,
        'Network and Security Configuration': 5,
        'Migration Execution': 20,
        'Validation and Testing': 10,
        'Optimization': 5,
        'Training and Documentation': 5,
        'Go Live': 1
    }

    # Calculate the timeline for each step
    for step in migration_steps:
        duration = step_durations.get(step, 0)
        end_date = start_date + timedelta(days=duration)

        # Add dependencies based on the step
        dependencies = []
        if step == 'Migration Execution':
            dependencies.append('Planning and Design')
            dependencies.append('Data Migration')
            dependencies.append('Application Containerization')
            dependencies.append('Network and Security Configuration')
        elif step == 'Validation and Testing':
            dependencies.append('Migration Execution')
        elif step == 'Optimization':
            dependencies.append('Validation and Testing')
        elif step == 'Training and Documentation':
            dependencies.append('Optimization')
        elif step == 'Go Live':
            dependencies.append('Training and Documentation')

        # Append the step details to the timeline DataFrame
        timeline_df = timeline_df.append({
            'Step': step,
            'Start Date': start_date.strftime('%Y-%m-%d'),
            'End Date': end_date.strftime('%Y-%m-%d'),
            'Duration': f'{duration} days',
            'Dependencies': ', '.join(dependencies)
        }, ignore_index=True)

        # Update the start date for the next step
        start_date = end_date

    return timeline_df
