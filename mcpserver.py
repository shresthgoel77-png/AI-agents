from mcp.server.fastmcp import FastMCP
from calculator import add, subtract, multiply, divide, calculate_percentage

# Initialize the FastMCP server
mcp = FastMCP("Personal Calculator")

@mcp.tool()
def add_numbers(a: float, b: float) -> float:
    """Add two numbers together."""
    return add(a, b)

@mcp.tool()
def subtract_numbers(a: float, b: float) -> float:
    """Subtract the second number from the first."""
    return subtract(a, b)

@mcp.tool()
def multiply_numbers(a: float, b: float) -> float:
    """Multiply two numbers together."""
    return multiply(a, b)

@mcp.tool()
def divide_numbers(a: float, b: float) -> float:
    """Divide the first number by the second number."""
    return divide(a, b)

@mcp.tool()
def get_percentage(value: float, percentage: float) -> float:
    """Calculate a specific percentage of a given value (e.g., 18% of 750)."""
    return calculate_percentage(value, percentage)

if __name__ == "__main__":
    # Run the server using stdin/stdout streams for MCP communication
    mcp.run()