# Rule Engine API

A comprehensive API for creating, combining, and evaluating rules. This application is built with Flask and provides a user-friendly interface to work with rules.

## Table of Contents

- [Technologies Used](#technologies-used)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Technologies Used

- **Python**: Programming language used for backend development.
- **Flask**: Web framework used to build the web application.
- **Docker**: Containerization tool to package the application.

## Features

- Create rules based on user-defined logic.
- Combine multiple rules into a single logical entity.
- Evaluate rules against provided data.
- User-friendly web interface to interact with the API.
- Health check endpoint to monitor the service status.

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Docker (for containerization)

### Step-by-Step Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/PiyushSinghcodes/rule_engine_api.git
   cd rule_engine_api
   ```

2. **Create a Virtual Environment** (optional but recommended)
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scriptsctivate`
   ```

3. **Install Dependencies**
   Ensure `requirements.txt` is populated with the necessary packages. If it's empty, you can manually add the following lines:
   ```
   Flask
   ```

4. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the Application**
   To run the application locally, use:
   ```bash
   python app.py
   ```

### Docker Installation 

1. **Build the Docker image:**
   ```bash
   sudo docker build -t rule_engine_api .
   ```

2. **Run the Docker container:**
   ```bash
   sudo docker run -p 8080:8080 rule_engine_api
   ```

## Usage

After running the app, open your browser and go to `http://127.0.0.0:8080` to access the Rule Engine API. Follow the prompts to create, combine, and evaluate rules.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue.

Project By---  PIYUSH SINGH
https://www.linkedin.com/in/piyush-singh908?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=ios_app
