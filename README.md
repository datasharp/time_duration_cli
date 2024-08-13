# Time Duration Calculator CLI Tool

A command-line tool for calculating the duration between two times.

## How to Install

To install the Time Duration Calculator CLI Tool, follow these steps:

1. **Clone the Repository:**  
   First, clone the repository to your local machine using the following command:

   ```bash
   git clone https://github.com/your-username/time-duration-calculator.git

2. **Navigate into the Project Directory:**

    ```bash
    cd time-duration-calculator


3. **Install the Dependencies:**
 
    ```bash
    pip install .

4. **Run the Tool:**

    ```bash
    timediff 8:30 AM 10:22 PM

## Features

- **AM/PM Functionality**: Supports time input in both 12-hour formats with AM/PM.

## Upcoming Features

- **Case-Insensitive AM/PM Input**: Will accept both uppercase and lowercase for AM/PM (e.g., `8:30 am` or `8:30 AM`).
- **Default to PM**: If AM/PM is not specified, the tool will assume PM by default.
- **Start/End Time Capture**: Will provide an option to start a timer and later capture the end time, calculating the duration between them.

## Example Usages

### Basic Usage with AM/PM

```bash
python time_duration.py 8:30 AM 10:22 PM
