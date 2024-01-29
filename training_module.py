import webbrowser

class TrainingModule:
    def __init__(self):
        self.documentation_url = "https://github.com/your-repository-name/your-project-name/blob/main/documentation.md"
        self.training_videos = {
            "Migration Readiness": "https://www.example.com/migration-readiness-video",
            "Automated Migration Planning": "https://www.example.com/automated-migration-planning-video",
            "Data Migration": "https://www.example.com/data-migration-video",
            "Application Containerization": "https://www.example.com/application-containerization-video",
            "Network and Security": "https://www.example.com/network-security-video",
            "GCP Migration Services": "https://www.example.com/gcp-migration-services-video",
            "Post-Migration Optimization": "https://www.example.com/post-migration-optimization-video",
            "Monitoring and Reporting": "https://www.example.com/monitoring-reporting-video",
            "Rollback Strategies": "https://www.example.com/rollback-strategies-video"
        }

    def open_documentation(self):
        """
        Open the online documentation in the default web browser.
        """
        webbrowser.open(self.documentation_url)

    def play_training_video(self, topic):
        """
        Open a training video in the default web browser based on the provided topic.
        :param topic: str
        """
        url = self.training_videos.get(topic)
        if url:
            webbrowser.open(url)
        else:
            print(f"No training video found for topic: {topic}")

    def list_available_training_resources(self):
        """
        List all available training resources.
        """
        print("Available Documentation:")
        print(f"- Online Documentation: {self.documentation_url}")
        print("\nAvailable Training Videos:")
        for topic, url in self.training_videos.items():
            print(f"- {topic}: {url}")

# Example usage:
if __name__ == "__main__":
    training_module = TrainingModule()
    training_module.list_available_training_resources()
    # To open documentation:
    # training_module.open_documentation()
    # To play a specific training video:
    # training_module.play_training_video("Migration Readiness")
