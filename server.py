from fastmcp import FastMCP
from run_browser.run_browser import run_browser

mcp = FastMCP("Fusion MAAS Agent 🚀")

@mcp.tool()
def browser_task(task: str) -> int:
    """Run a task in the browser"""
    return run_browser(task)

if __name__ == "__main__":
    mcp.run(transport="sse")