from mcp.server.fastmcp import FastMCP

import requests

mcp = FastMCP(name="menu-tool")

@mcp.tool()
def weather_forecast() -> dict:
    """Get the weather forecast for Nagano Prefecture."""
    url = "https://www.jma.go.jp/bosai/forecast/data/forecast/200000.json"

    response = requests.get(url)
    data = response.json()

    return data


@mcp.tool()
def sum(a: int, b: int) -> int:
    """Add two numbers together."""
    return a + b

## 2. 食材から献立を返すmcpサーバー

menus = {
    "野菜炒め": ["キャベツ", "人参", "ピーマン", "もやし", "醤油"],
    "豚の生姜焼き": ["豚肉", "生姜", "醤油"],
    "お好み焼き": ["キャベツ", "小麦粉", "卵", "豚肉", "ソース"],
    "餃子": ["豚肉", "キャベツ", "ニラ", "餃子の皮", "醤油"],
}

# class MenuResponse(TypedDict):
#     menu: str
#     ingredients: list[str]

@mcp.tool()
def menu(ingredient: str) -> list[dict[str, list[str]|str]]:
    """Return a menu based on the given ingredient."""
    result = []
    for k, v in menus.items():
        if ingredient in v:
            result.append({
                "menu": k,
                "ingredients": v,
            })
    return result
