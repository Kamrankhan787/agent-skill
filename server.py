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

if __name__ == "__main__":
    # Start the server using stdio transport
    # Note: FastMCP handles the stdio transport setup automatically.
    mcp.run()
