# Simplified fake MCP calendar functions for assignment
# (Because real MCP OAuth setup is long and not required for your internship task)

def get_todays_meetings():
    return [
        {"title": "Team Sync", "time": "10:00 AM"},
        {"title": "Project Standup", "time": "4:00 PM"}
    ]

def get_week_meetings():
    return [
        {"title": "Team Sync - Monday 10AM"},
        {"title": "Client Review - Wednesday 3PM"},
        {"title": "Project Planning - Friday 2PM"}
    ]
