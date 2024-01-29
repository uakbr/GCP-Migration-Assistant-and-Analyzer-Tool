import json
import datetime

class ReportingTool:
    def __init__(self):
        self.reports = []

    def generate_report(self, assessment_results, migration_plan, post_migration_analysis):
        """
        Generate a comprehensive report that includes the assessment results,
        migration plan, and post-migration analysis.
        """
        report = {
            'timestamp': datetime.datetime.now().isoformat(),
            'assessment_results': assessment_results,
            'migration_plan': migration_plan,
            'post_migration_analysis': post_migration_analysis
        }
        self.reports.append(report)
        return report

    def save_report_to_file(self, report, filename):
        """
        Save the generated report to a file in JSON format.
        """
        with open(filename, 'w') as file:
            json.dump(report, file, indent=4)

    def print_report(self, report):
        """
        Print the report to the console.
        """
        print(json.dumps(report, indent=4))

# Example usage:
# reporting = ReportingTool()
# assessment_results = {'compatibility': 'Compatible', 'estimated_costs': 5000, 'challenges': []}
# migration_plan = {'steps': ['Step 1', 'Step 2'], 'resource_allocation': {'VMs': 10}, 'timeline': '1 month'}
# post_migration_analysis = {'cost_saving': 1000, 'performance_improvement': '20%'}
# report = reporting.generate_report(assessment_results, migration_plan, post_migration_analysis)
# reporting.save_report_to_file(report, 'migration_report.json')
# reporting.print_report(report)
