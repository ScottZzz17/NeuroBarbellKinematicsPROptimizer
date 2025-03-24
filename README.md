# Neuro Barbell Kinematics PROptimizer

Neuro Barbell Kinematics PROptimizer (PersonalTrainer) is a cutting-edge project that analyzes bench press performance using computer vision and biomechanics. It tracks barbell kinematics (position, velocity, and acceleration) to calculate work done and power output. The project is designed to evolve into an AI-powered workout advisor that suggests training programs to help users improve their personal records (PRs).

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [How It Works](#how-it-works)
- [Docker Integration](#docker-integration)
- [Future Plans](#future-plans)
- [Security and Open Sourcing Docker Files](#security-and-open-sourcing-docker-files)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Overview

The PersonalTrainer project leverages video analysis to extract kinematic data from bench press movements. By tracking the barbell's motion, it computes:
- **Vertical displacement, velocity, and acceleration**
- **Work done and average/instantaneous power output**

The project is set up to run in a Docker container, ensuring a consistent and isolated environment, making it easier to deploy and share.

## Features

- **Video Processing:** Uses OpenCV to track the barbell marker.
- **Biomechanical Analysis:** Computes key parameters like work and power.
- **Data Smoothing and Repetition Detection:** Implements a moving average filter and peak/valley detection.
- **Dockerized Environment:** Ensures consistent dependencies and simplifies deployment.
- **Planned AI Integration:** Future enhancements include an AI module that analyzes performance data to recommend personalized workouts aimed at increasing your PR.

## How It Works

1. **Video Capture & Calibration:**  
   - The application processes a bench press video.
   - A known calibration distance converts pixel measurements into real-world units.

2. **Marker Tracking:**  
   - OpenCV tracks a selected ROI (e.g., the bottom of the barbell plate).
   - The marker’s vertical positions are recorded over time.

3. **Data Analysis:**  
   - The raw position data is filtered using a moving average.
   - Repetitions are detected by identifying peaks and valleys.
   - Velocity and acceleration are computed.
   - Using basic physics (work = m * g * h and P = F * v), the application calculates the workout’s work output and power.

4. **Docker Integration:**  
   - The Dockerfile defines the environment, dependencies, and the command to run the application.
   - The `docker-compose.yml` file makes it easy to build and run the containerized application with a single command.

## Docker Integration

Docker is used in this project to ensure that the environment is consistent across different systems. Here’s what each component does:

- **Dockerfile:**  
  Contains instructions to build an image for the PersonalTrainer project. It installs Python, dependencies (OpenCV, NumPy, SciPy), and copies the application code.

- **docker-compose.yml:**  
  Defines the service configuration, allowing you to build and run the container effortlessly. It also supports port mapping and volume mounting for development convenience.

### Example Commands

- **Build the Docker Image:**  
  ```bash
  docker build -t personaltrainer .
  ```

## Future Plans

1. **AI Integration:**  
   - Develop an AI module that ingests the kinematic data.  
   - Utilize machine learning (e.g., neural networks) to analyze performance patterns.  
   - Generate personalized workout plans and adjustments to optimize training and help increase PRs.

2. **Enhanced Biomechanical Analysis:**  
   - Integrate more detailed biomechanics using user-provided measurements (e.g., shoulder-to-elbow, elbow-to-wrist).  
   - Expand the analysis to include joint angles and leverage for more precise power estimations.

3. **User Interface & Reporting:**  
   - Build a user-friendly interface for data visualization and workout recommendations.  
   - Generate detailed reports on performance improvements over time.

4. **Cloud Deployment & Scalability:**  
   - Containerize additional services (e.g., a REST API for AI recommendations).  
   - Deploy to cloud platforms for scalability and remote access.

## Security and Open Sourcing Docker Files

It is generally safe to have Dockerfiles and docker-compose files publicly available on GitHub as long as they do not contain sensitive data (e.g., passwords, API keys, or private credentials). These files are intended to define your environment and installation steps, allowing others to replicate your setup and contribute to your project.

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/PersonalTrainer.git
   cd PersonalTrainer
   ```
   
2. Install Dependencies:
If running locally (outside of Docker), create a virtual environment and install the requirements:

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows, use: .venv\Scripts\activate
pip install -r requirements.txt
```

3. Set Up Docker:
Ensure Docker Desktop is installed and running on your machine.

## Usage

- **Run the Application Locally:**

  ```bash
  python main.py
  ```

  - **Run the Application in Docker:**

  ```bash
  docker-compose up
  ```

  Follow the on-screen prompts to process your bench press video and analyze your performance data.

## Contributing

Contributions are welcome! Please fork the repository, create a new branch for your feature or bug fix, and submit a pull request. For major changes, please open an issue first to discuss what you’d like to change.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact Information

For further discussion, collaboration, or a private demonstration of the system’s capabilities, please contact:
- **Email:** szaragoza2@wisc.edu  
- **LinkedIn:** [https://www.linkedin.com/in/scott-zaragoza-198401329/](https://www.linkedin.com/in/scott-zaragoza-198401329/)
