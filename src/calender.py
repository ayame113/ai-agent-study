"""iCal MCP Server - HTTPからiCalendarファイルを取得し、予定を返すMCPサーバー"""

from datetime import datetime, timedelta
from typing import Any
from zoneinfo import ZoneInfo

import requests
from icalendar import Calendar
from mcp.server.fastmcp import FastMCP

# 自分のカレンダー共有URL
url = "https://lms.ealps.shinshu-u.ac.jp/2025/t/calendar/export_execute.php?userid=3084&authtoken=33a178247ef905974c0942acf237be99a1d368c3&preset_what=all&preset_time=custom"

# Fast MCPサーバーのインスタンスを作成
mcp = FastMCP("ical-mcp-server")


def fetch_ical(url: str) -> str:
    """HTTPからiCalendarファイルを取得"""
    response = requests.get(url, allow_redirects=True)
    response.raise_for_status()
    return response.text


def parse_ical_events(ical_content: str, days_ahead: int = 30) -> list[dict[str, Any]]:
    """iCalendarコンテンツをパースしてイベントのリストを返す"""
    cal = Calendar.from_ical(ical_content)
    events = []

    # 現在時刻と範囲の終了時刻を設定
    now = datetime.now(ZoneInfo("UTC"))
    end_date = now + timedelta(days=days_ahead)

    for component in cal.walk():
        if component.name == "VEVENT":
            event = {}

            # イベントの開始時刻
            dtstart = component.get('dtstart')
            if dtstart:
                start_dt = dtstart.dt
                # dateオブジェクトの場合はdatetimeに変換
                if not isinstance(start_dt, datetime):
                    start_dt = datetime.combine(start_dt, datetime.min.time())
                    start_dt = start_dt.replace(tzinfo=ZoneInfo("UTC"))
                elif start_dt.tzinfo is None:
                    start_dt = start_dt.replace(tzinfo=ZoneInfo("UTC"))

                # 指定された範囲内のイベントのみを含める
                if start_dt < now or start_dt > end_date:
                    continue

                event['start'] = start_dt.isoformat()
            else:
                continue

            # イベントの終了時刻
            dtend = component.get('dtend')
            if dtend:
                end_dt = dtend.dt
                if not isinstance(end_dt, datetime):
                    end_dt = datetime.combine(end_dt, datetime.min.time())
                    end_dt = end_dt.replace(tzinfo=ZoneInfo("UTC"))
                elif end_dt.tzinfo is None:
                    end_dt = end_dt.replace(tzinfo=ZoneInfo("UTC"))
                event['end'] = end_dt.isoformat()

            # イベントのサマリー（タイトル）
            summary = component.get('summary')
            if summary:
                event['summary'] = str(summary)

            # イベントの説明
            description = component.get('description')
            if description:
                event['description'] = str(description)

            # イベントの場所
            location = component.get('location')
            if location:
                event['location'] = str(location)

            # イベントのUID
            uid = component.get('uid')
            if uid:
                event['uid'] = str(uid)

            # イベントのステータス
            status = component.get('status')
            if status:
                event['status'] = str(status)

            events.append(event)

    # 開始時刻でソート
    events.sort(key=lambda x: x['start'])

    return events


@mcp.tool()
async def fetch_ical_events(days_ahead: int = 30) -> str:
    """HTTPからiCalendar形式のファイルを取得し、今後の予定を返します。

    Args:
        days_ahead: 今後何日分の予定を取得するか（デフォルト: 30日）

    Returns:
        今後の予定のリスト
    """

    try:
        # iCalファイルを取得
        ical_content = fetch_ical(url)

        # イベントをパース
        events = parse_ical_events(ical_content, days_ahead)

        if not events:
            return f"今後{days_ahead}日間に予定されているイベントはありません。"

        # 結果をフォーマット
        result = f"今後{days_ahead}日間の予定（{len(events)}件）:\n\n"

        for i, event in enumerate(events, 1):
            result += f"{i}. {event.get('summary', '（タイトルなし）')}\n"
            result += f"   開始: {event['start']}\n"
            if 'end' in event:
                result += f"   終了: {event['end']}\n"
            if 'location' in event:
                result += f"   場所: {event['location']}\n"
            if 'description' in event:
                desc = event['description']
                # 説明が長い場合は最初の100文字のみ表示
                if len(desc) > 100:
                    desc = desc[:100] + "..."
                result += f"   説明: {desc}\n"
            result += "\n"

        return result

    except requests.exceptions.RequestException as e:
        return f"エラー: iCalファイルの取得に失敗しました: {str(e)}"
    except Exception as e:
        return f"エラー: {str(e)}"
