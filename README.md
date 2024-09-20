# glances_web_api
Glances web api, to interact with versions 3 and 4 of the glances linux tool

## AUTHOR: GUSTAVO WYDLER AZUAGA
## VERSION: 1
## RELEASE DATE: 09-20-2024

Glances Web API
- The Glances Web API provides a RESTful interface for accessing real-time system monitoring data. 
- It's built on top of the Glances monitoring tool and allows remote monitoring and data collection via HTTP.

## Features

**Real-time system metrics**: Access information on CPU, memory, disk usage, network traffic, and more.

**Some of the API endpoint calls**: Fetch various system statistics, including:
  - CPU load and usage
  - Memory and swap usage
  - Disk IO
  - Network interfaces
  - Processes and services
  - Containers and RAID devices

## Installation

To set up and run the glances web API, follow these instructions:

### Prerequisites

- **Python 3.x**: Ensure Python 3 is installed on your system.
- **Flask**: A lightweight WSGI web application framework.
- **Glances**: Glances should be installed and running on the machine.
```bash
   glances -w -B <your-server-ip>
```
## Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone https://github.com/kurogane13/glances_web_api.git
   glances_web_api

2. **Create a Virtual Environment (Recommended)**

   ```bash
    python3.8 -m venv venv
    source venv/bin/activate

3. **Depending on your system, you need to allow port 5000 through the firewall:**

   ```bash
   # For RHEL based systems:

   sudo firewall-cmd --permanent --add-port=5000/tcp
   sudo firewall-cmd --reload
   
   #For DEBIAN based systems (like Ubuntu):

   sudo ufw allow 5000/tcp
   sudo ufw reload

4. **Run the Application**

   - Start the Flask development server:
   ```bash
    python3.8 app.py
