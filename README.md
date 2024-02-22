
# A Project to Compare Selenium and Playwright in Python for UI/E2E Testing

## Introduction

In this project, we explore the capabilities of both  **Selenium**  and  **Playwright**  for automating end-to-end (E2E) UI tests in Python. These tools allow us to simulate user interactions, validate web application behavior, and ensure the quality of our frontend applications.

### Framework Overview

-   **Selenium**: Selenium is a widely-used open-source framework that automates web browsers. It provides a rich set of APIs to interact with web elements, perform actions (such as clicks and form submissions), and verify expected outcomes.
-   **Playwright**: Playwright is a newer tool that abstracts away the complexities of cross-browser testing. It supports multiple browsers (including Chromium, Firefox, and WebKit) and provides a unified API for E2E testing.

### Project Details

-   **Type of Framework**:
    -   **Primary Framework**: Pytest (for test organization and execution)
    -   **Secondary Frameworks**: Playwright and Selenium
-   **Configuration File**: We use a  `pytest.ini`  file for configuration.
-   **Reporting**: We generate an HTML report using  `pytest-html`.
-   **Dependencies**:
    -   `pytest`
    -   `pytest-playwright`
    -   `pytest-html`
    -   `pytest-parallel`
    -   `playwright`
    -   `selenium`
    -   `poetry`

### Environment Setup

1.  **Create a Conda Environment**:
  - Use Conda to create a virtual environment and activate it for the project.
	```shell
	PROJECT_NAME = python-project-template
	PYTHON_VERSION = 3.10

	conda create --name $PROJECT_NAME --yes python=$PYTHON_VERSION
	conda activate $PROJECT_NAME
	```

2.  **Clone the Repository**:
 -   Clone this repository to your local machine.
4.  **Install Dependencies**:

   -   Use Poetry to manage project dependencies:

        ```bash
        poetry install
        ```

