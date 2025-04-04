# MCP Jenkins Server

A Model Context Protocol (MCP) server that provides Jenkins integration tools.

## Features

- Get Jenkins server information
- List and inspect Jenkins jobs
- Get build information and console output
- Manage Jenkins views
- Trigger specific job builds

## Requirements

- Python 3.10+
- Jenkins server with API access
- Jenkins API token for authentication

## Installation

1. Clone this repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

Create a `.env` file with your Jenkins credentials:

```ini
JENKINS_URL=https://your-jenkins-server
JENKINS_USER=your-username
JENKINS_TOKEN=your-api-token
```

## CLI Configuration

To add this MCP server to your CLI, use the following configuration:

```json
{
  "mcpServers": {
    "mcp-jenkins-server": {
      "command": "uv",
      "args": [
        "--directory", 
        "C:\\Users\\Dean.Li\\Documents\\Cline\\MCP\\mcp-jenkins-server",
        "run",
        "server.py"
      ],
      "env": {
        "JENKINS_URL": "https://your-jenkins-server/",
        "JENKINS_USERNAME": "your-username",
        "JENKINS_PASSWORD": "your-password"
      },
      "disabled": false,
      "autoApprove": []
    }
  }
}
```

## Available Tools

This MCP server provides the following tools:

### `get_jenkins_info`
Get Jenkins server information

### `list_jobs`
List all Jenkins jobs

### `get_job_info`
Get information about a specific job
- Parameters:
  - `job_name`: Name of the job to inspect

### `get_build_info`
Get information about a specific build
- Parameters:
  - `job_name`: Name of the job
  - `build_number`: Build number to inspect

### `get_build_console_output`
Get console output for a specific build
- Parameters:
  - `job_name`: Name of the job
  - `build_number`: Build number to inspect

### `get_views`
List all Jenkins views

### `trriger_llm_demo_job_build`
Trigger the "LLM_Demo" job build
- Parameters:
  - `user`: User name to pass as build parameter

## Example Usage

```python
from mcp.client import Client

client = Client("http://localhost:8000")  # MCP server URL
response = client.call_tool("list_jobs")
print(response)
```

## License

MIT
