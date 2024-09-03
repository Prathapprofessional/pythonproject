I embarked on a comprehensive journey to develop and deploy a full-stack application, starting with a Python-based Flask backend for managing to-do items. The application featured RESTful endpoints to handle CRUD (Create, Read, Update, Delete) operations and was thoroughly tested using automated tests with pytest. For manual testing, we used Tkinter to create a GUI for interacting with the backend.

To enhance the developer experience and facilitate API documentation, we integrated Swagger UI into our Flask application, providing an interactive interface for exploring and testing API endpoints directly from the browser.

Version control was managed using Git, with the project pushed to GitHub. We used GitHub Actions to automate our CI/CD pipeline, which included running automated tests and deploying the application. For the frontend, we set up GitHub Pages to serve static HTML files, allowing users to interact with the API through a web interface.

Containerization was achieved by creating a Dockerfile to package our Flask application into a Docker container, which was validated locally using Docker commands. We then deployed our Dockerized application using Kubernetes, orchestrated via Docker Desktop. Configured Kubernetes deployment and service YAML files to manage and expose our application using both NodePort and LoadBalancer services.

Throughout the project,  employed tools and technologies such as Python, Flask, Docker, Kubernetes, GitHub, GitHub Pages, Swagger UI, pytest for automated testing, Tkinter for manual testing, and GitHub Actions for CI/CD.

This summary encapsulates the key stages of the project, highlighting the tools and technologies involved and demonstrating the integration of modern development practices, including automated and manual testing, continuous integration, and deployment.
