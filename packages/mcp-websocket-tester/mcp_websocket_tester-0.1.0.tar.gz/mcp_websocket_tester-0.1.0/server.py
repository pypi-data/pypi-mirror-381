from mcp.server.fastmcp import FastMCP
import asyncio
import websockets
import json
import base64
from typing import Dict, List, Optional
from dataclasses import dataclass
from enum import Enum
import time
import threading

class MessageFormat(Enum):
    TEXT = "text"
    JSON = "json"
    BINARY = "binary"

class WebSocketProtocol(Enum):
    WS = "ws"
    WSS = "wss"

@dataclass
class ConnectionInfo:
    url: str
    protocol: WebSocketProtocol
    connected_at: float
    message_count: int = 0
    last_activity: Optional[float] = None

mcp = FastMCP("Advanced WebSocket Testing Server")

# Enhanced connection storage with background listeners
active_connections: Dict[str, any] = {}
connection_metadata: Dict[str, ConnectionInfo] = {}
message_queues: Dict[str, List[str]] = {}
background_tasks: Dict[str, asyncio.Task] = {}

async def start_message_listener(connection_id: str):
    """Background task to continuously listen for incoming messages"""
    connection = active_connections[connection_id]
    try:
        async for message in connection:
            message_queues[connection_id].append(message)
            # Update last activity
            if connection_id in connection_metadata:
                connection_metadata[connection_id].last_activity = time.time()
    except websockets.exceptions.ConnectionClosed:
        # Connection closed, stop listening
        pass
    except Exception as e:
        print(f"Error in message listener for {connection_id}: {e}")

@mcp.tool()
async def connect_websocket(
    url: str, 
    protocol: str = "ws"
) -> str:
    """Connect to a WebSocket server and start background message listener."""
    try:
        connection = await websockets.connect(url)
        connection_id = str(id(connection))
        active_connections[connection_id] = connection
        connection_metadata[connection_id] = ConnectionInfo(
            url=url,
            protocol=WebSocketProtocol(protocol),
            connected_at=time.time()
        )
        message_queues[connection_id] = []
        
        # Start background message listener
        task = asyncio.create_task(start_message_listener(connection_id))
        background_tasks[connection_id] = task
        
        return f"Connected to {url} with ID: {connection_id}"
    except Exception as e:
        return f"Connection failed: {str(e)}"

@mcp.tool()
async def send_websocket_message(
    connection_id: str, 
    message: str, 
    message_format: str = "text"
) -> str:
    """Send a message through WebSocket connection with format support."""
    if connection_id not in active_connections:
        return "Error: Connection not found"
    
    try:
        connection = active_connections[connection_id]
        metadata = connection_metadata[connection_id]
        
        # Format message based on type
        if message_format == MessageFormat.JSON.value:
            json.loads(message)  # Validate JSON
            formatted_message = message
        elif message_format == MessageFormat.BINARY.value:
            formatted_message = message.encode('utf-8')
        else:  # TEXT
            formatted_message = message
        
        await connection.send(formatted_message)
        metadata.message_count += 1
        metadata.last_activity = time.time()
        
        return f"Sent {message_format} message: {message}"
    except Exception as e:
        return f"Error sending message: {str(e)}"

@mcp.tool()
async def receive_websocket_message(
    connection_id: str,
    timeout: int = 10
) -> str:
    """Receive the next message from WebSocket connection."""
    if connection_id not in active_connections:
        return "Error: Connection not found"
    
    start_time = time.time()
    while time.time() - start_time < timeout:
        if message_queues[connection_id]:
            message = message_queues[connection_id].pop(0)
            # Format response based on type
            if isinstance(message, bytes):
                return f"Binary message (base64): {base64.b64encode(message).decode()}"
            elif _is_json(message):
                return f"JSON message: {message}"
            else:
                return f"Text message: {message}"
        await asyncio.sleep(0.1)
    
    return "Error: Timeout waiting for message"

@mcp.tool()
def get_queued_messages(connection_id: str) -> List[str]:
    """Get all queued messages for a connection."""
    if connection_id not in message_queues:
        return ["Error: Connection not found"]
    return [f"Message {i+1}: {msg}" for i, msg in enumerate(message_queues[connection_id])]

@mcp.tool()
def clear_message_queue(connection_id: str) -> str:
    """Clear all queued messages for a connection."""
    if connection_id not in message_queues:
        return "Error: Connection not found"
    message_queues[connection_id].clear()
    return "Message queue cleared"

@mcp.tool()
def get_connection_diagnostics(connection_id: str) -> Dict:
    """Get detailed diagnostics for a WebSocket connection."""
    if connection_id not in active_connections:
        return {"error": "Connection not found"}
    
    metadata = connection_metadata[connection_id]
    current_time = time.time()
    
    return {
        "connection_id": connection_id,
        "url": metadata.url,
        "protocol": metadata.protocol.value,
        "uptime_seconds": current_time - metadata.connected_at,
        "message_count": metadata.message_count,
        "last_activity": metadata.last_activity,
        "time_since_last_activity": current_time - metadata.last_activity if metadata.last_activity else None,
        "queued_messages": len(message_queues[connection_id]),
        "background_listener_active": connection_id in background_tasks and not background_tasks[connection_id].done(),
        "status": "active"
    }

@mcp.tool()
async def run_test_scenario(
    connection_id: str,
    scenario: List[Dict]
) -> str:
    """Run automated test scenario with multiple steps."""
    if connection_id not in active_connections:
        return "Error: Connection not found"
    
    results = []
    connection = active_connections[connection_id]
    
    for step in scenario:
        step_type = step.get("type")
        step_data = step.get("data", {})
        
        try:
            if step_type == "send":
                message = step_data.get("message", "")
                message_format = step_data.get("format", "text")
                await send_websocket_message(connection_id, message, message_format)
                results.append(f"✓ Sent: {message}")
                
            elif step_type == "receive":
                timeout = step_data.get("timeout", 5)
                expected = step_data.get("expected", "")
                response = await receive_websocket_message(connection_id, timeout)
                
                if expected and expected not in response:
                    results.append(f"✗ Receive failed: expected '{expected}', got '{response}'")
                else:
                    results.append(f"✓ Received: {response}")
                    
            elif step_type == "wait":
                wait_time = step_data.get("time", 1)
                await asyncio.sleep(wait_time)
                results.append(f"✓ Waited: {wait_time}s")
                
        except Exception as e:
            results.append(f"✗ Step failed: {str(e)}")
    
    return "\n".join(results)

@mcp.tool()
def list_protocols() -> List[str]:
    """List supported WebSocket protocols."""
    return [protocol.value for protocol in WebSocketProtocol]

@mcp.tool()
def list_message_formats() -> List[str]:
    """List supported message formats."""
    return [format.value for format in MessageFormat]

@mcp.tool()
async def close_connection(connection_id: str) -> str:
    """Close a WebSocket connection and cleanup."""
    if connection_id not in active_connections:
        return "Error: Connection not found"
    
    try:
        # Cancel background task
        if connection_id in background_tasks:
            background_tasks[connection_id].cancel()
        
        # Close connection
        await active_connections[connection_id].close()
        
        # Cleanup
        del active_connections[connection_id]
        del connection_metadata[connection_id]
        del message_queues[connection_id]
        if connection_id in background_tasks:
            del background_tasks[connection_id]
            
        return f"Closed connection: {connection_id}"
    except Exception as e:
        return f"Error closing connection: {str(e)}"

def _is_json(text: str) -> bool:
    """Check if text is valid JSON."""
    try:
        json.loads(text)
        return True
    except:
        return False

if __name__ == "__main__":
    mcp.run(transport="stdio")