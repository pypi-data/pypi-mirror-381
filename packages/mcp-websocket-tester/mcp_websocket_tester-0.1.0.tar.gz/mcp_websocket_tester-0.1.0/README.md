# MCP WebSocket Testing Server

A powerful Model Context Protocol (MCP) server for testing WebSocket applications. Provides AI assistants with comprehensive WebSocket testing capabilities including connection management, message sending/receiving, and automated test scenarios.

## 🚀 Features

- **Multiple Protocol Support**: WS and WSS protocols
- **Message Format Support**: Text, JSON, and Binary message formats
- **Real-time Monitoring**: Background message listeners and connection diagnostics
- **Automated Testing**: Run complex test scenarios with multiple steps
- **Queue Management**: Handle incoming messages with proper queuing system
- **Comprehensive Diagnostics**: Monitor connection health and performance

## 📦 Installation

### Prerequisites
- Python 3.13 or higher
- [UV package manager](https://github.com/astral-sh/uv) (recommended) or pip

### Quick Start
```bash
# Clone the repository
git clone <https://github.com/Kabir08/WebsocketMcp>
cd mcp-websocket-tester

# Install dependencies
uv sync

# Or with pip
pip install -e .


## ⚙️ MCP Client Configuration

### Claude Desktop Configuration

Add this to your Claude Desktop configuration file:

**macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`  
**Windows**: `%APPDATA%/Claude/claude_desktop_config.json`  
**Linux**: `~/.config/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "websocket-tester": {
      "command": "uvx",
      "args": ["mcp-websocket-tester"]
    }
  }
}