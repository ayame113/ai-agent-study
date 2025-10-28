import requests
from mcp.server.fastmcp import FastMCP

mcp = FastMCP(name="weather-tool")

@mcp.tool()
def weather_forecast() -> list[dict]:
    """長野県の天気予報を取得する。"""
    url = "https://www.jma.go.jp/bosai/forecast/data/forecast/200000.json"

    response = requests.get(url)
    data = response.json()

    return data
