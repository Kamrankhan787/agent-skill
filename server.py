from mcp.server.fastmcp import FastMCP
import httpx
import sys

# Initialize FastMCP
# The name provided here will be shown in the MCP client
mcp = FastMCP("Demo Weather Server")

# ---------------------------------------------------------------------------
# TOOLS
# Tools are functions the AI can choose to execute.
# FastMCP automatically generates the JSON schema based on type hints and docstrings.
# ---------------------------------------------------------------------------

@mcp.tool()
async def get_weather(location: str) -> str:
    """
    Get the current weather for a specified location.
    
    Args:
        location: The city and state/country, e.g., "San Francisco, CA"
    """
    # NOTE: Always use stderr for logging to avoid breaking the stdio transport!
    print(f"Fetching weather for {location}...", file=sys.stderr)
    
    # Mock implementation for demonstration
    return f"The weather in {location} is currently 72°F and sunny."


@mcp.tool()
def calculate_travel_time(distance_miles: float, speed_mph: float) -> str:
    """
    Calculate how long it takes to travel a certain distance.
    """
    if speed_mph <= 0:
        return "Speed must be greater than 0."
    
    hours = distance_miles / speed_mph
    return f"It will take approximately {hours:.2f} hours."

# ---------------------------------------------------------------------------
# RESOURCES
# Resources expose static or dynamic read-only data.
# They are accessed via custom URIs.
# ---------------------------------------------------------------------------

@mcp.resource("config://app/settings")
def get_app_settings() -> str:
    """Get the current application settings as a string."""
    return '{"theme": "dark", "version": "1.0.4", "debug": true}'

# ---------------------------------------------------------------------------
# PROMPTS
# Prompts are reusable templates users can invoke.
# ---------------------------------------------------------------------------

@mcp.prompt()
def analyze_weather(location: str) -> str:
    """Create a prompt requesting a weather analysis."""
    return f"Please analyze the weather for {location} and tell me what I should pack for a weekend trip."

# Vercel needs an ASGI 'app' to serve HTTP requests (which enables SSE transport for MCP)
# FastMCP exposes a Starlette ASGI app via .sse_app()
app = mcp.sse_app()

from starlette.responses import HTMLResponse
def homepage(request):
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>MCP Server Running</title>
        <style>
            body { font-family: system-ui, -apple-system, sans-serif; background: #0a0a0a; color: #ededed; display: flex; align-items: center; justify-content: center; height: 100vh; margin: 0; }
            .container { text-align: center; background: #1a1a1a; padding: 3rem; border-radius: 12px; border: 1px solid #333; box-shadow: 0 8px 32px rgba(0,0,0,0.5); }
            h1 { color: #fff; margin-top: 0; }
            p { color: #a0a0a0; font-size: 1.1rem; }
            .code { background: #000; padding: 10px 15px; border-radius: 6px; font-family: monospace; color: #4ade80; font-size: 1.2rem; margin-top: 1rem; display: inline-block; border: 1px solid #222; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🚀 MCP Server is Live</h1>
            <p>This is a Model Context Protocol (MCP) server designed for AI agents.<br>There is no frontend web application here.</p>
            <p>Connect your AI client to the SSE endpoint:</p>
            <div class="code">/sse</div>
        </div>
    </body>
    </html>
    """
    return HTMLResponse(html_content)

app.add_route("/", homepage)

if __name__ == "__main__":
    # Start the server using stdio transport
    # Note: FastMCP handles the stdio transport setup automatically.
    mcp.run()
