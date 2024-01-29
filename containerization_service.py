import subprocess
import os
import logging

class ContainerizationService:
    def __init__(self, app_directory, target_image_name):
        self.app_directory = app_directory
        self.target_image_name = target_image_name

    def containerize_application(self):
        """
        Containerizes the application located in the specified directory and tags it with the provided image name.
        """
        try:
            # Check if Dockerfile exists in the application directory
            dockerfile_path = os.path.join(self.app_directory, 'Dockerfile')
            if not os.path.isfile(dockerfile_path):
                raise FileNotFoundError("Dockerfile not found in the application directory.")

            # Build the Docker image
            build_command = f'docker build -t {self.target_image_name} {self.app_directory}'
            subprocess.run(build_command, check=True, shell=True)
            logging.info(f"Successfully built the Docker image: {self.target_image_name}")

            # Push the Docker image to Google Container Registry (GCR)
            gcr_image_name = f'gcr.io/your-project-id/{self.target_image_name}'
            tag_command = f'docker tag {self.target_image_name} {gcr_image_name}'
            push_command = f'docker push {gcr_image_name}'

            subprocess.run(tag_command, check=True, shell=True)
            subprocess.run(push_command, check=True, shell=True)
            logging.info(f"Successfully pushed the Docker image to GCR: {gcr_image_name}")

            return True

        except subprocess.CalledProcessError as e:
            logging.error(f"An error occurred while containerizing the application: {e}")
            return False
        except FileNotFoundError as e:
            logging.error(e)
            return False
        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")
            return False

if __name__ == "__main__":
    # Example usage:
    # Replace 'your-app-directory' with the path to your application directory
    # Replace 'your-image-name' with the desired Docker image name
    containerization_service = ContainerizationService('your-app-directory', 'your-image-name')
    success = containerization_service.containerize_application()
    if success:
        print("Application containerization completed successfully.")
    else:
        print("Application containerization failed. Check logs for details.")
