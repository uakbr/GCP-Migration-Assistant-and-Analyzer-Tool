import click
from assessment_service import AssessmentService
from planning_service import PlanningService
from data_migration_service import DataMigrationService
from containerization_service import ContainerizationService
from network_configurator import NetworkConfigurator
from security_configurator import SecurityConfigurator
from gcp_migration_integration import GCPMigrationIntegration
from optimization_service import OptimizationService
from monitoring_service import MonitoringService
from reporting_tool import ReportingTool
from rollback_service import RollbackService
from training_module import TrainingModule

@click.group()
def cli():
    """GCP Migration Assistant and Analyzer Tool CLI."""
    pass

@cli.command()
@click.option('--project-id', prompt='Enter your GCP project ID', help='The GCP project ID where the resources are hosted.')
@click.option('--zone', prompt='Enter the zone of your resources', help='The zone of the resources to be migrated.')
def assess(project_id, zone):
    """Perform a migration readiness assessment."""
    assessment_service = AssessmentService()
    results = assessment_service.assess_migration_readiness(project_id, zone)
    click.echo("Assessment completed. Results:")
    click.echo(results)

@cli.command()
def plan():
    """Generate a detailed migration plan."""
    planning_service = PlanningService()
    plan = planning_service.create_migration_plan()
    click.echo("Migration plan created successfully.")
    click.echo(plan)

@cli.command()
def migrate_data():
    """Migrate data to GCP."""
    data_migration_service = DataMigrationService()
    data_migration_service.migrate()
    click.echo("Data migration completed successfully.")

@cli.command()
def containerize():
    """Assist in containerizing applications."""
    containerization_service = ContainerizationService()
    containerization_service.containerize()
    click.echo("Applications containerized successfully.")

@cli.command()
def configure_network():
    """Configure network settings for GCP."""
    network_configurator = NetworkConfigurator()
    network_configurator.configure()
    click.echo("Network configuration completed successfully.")

@cli.command()
def configure_security():
    """Configure security settings for GCP."""
    security_configurator = SecurityConfigurator()
    security_configurator.configure()
    click.echo("Security configuration completed successfully.")

@cli.command()
def integrate():
    """Integrate with GCP migration services."""
    gcp_migration_integration = GCPMigrationIntegration()
    gcp_migration_integration.integrate()
    click.echo("Integration with GCP migration services completed successfully.")

@cli.command()
def optimize():
    """Optimize the cloud deployment post-migration."""
    optimization_service = OptimizationService()
    optimization_service.optimize()
    click.echo("Post-migration optimization completed successfully.")

@cli.command()
def monitor():
    """Monitor the migration process."""
    monitoring_service = MonitoringService()
    monitoring_service.monitor()
    click.echo("Migration monitoring started successfully.")

@cli.command()
def report():
    """Generate a migration report."""
    reporting_tool = ReportingTool()
    reporting_tool.generate_report()
    click.echo("Migration report generated successfully.")

@cli.command()
def rollback():
    """Rollback the migration process in case of issues."""
    rollback_service = RollbackService()
    rollback_service.rollback()
    click.echo("Rollback completed successfully.")

@cli.command()
def train():
    """Provide user training and documentation."""
    training_module = TrainingModule()
    training_module.train()
    click.echo("User training and documentation provided successfully.")

if __name__ == '__main__':
    cli()
