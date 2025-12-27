def get_dashboard_data():
  return {
    "user": {
      "name": "John Doe",
      "email": "john@example.com",
      "avatar": "👤",
      "plan": "Professional",
    },
    "stats": {
      "total_comments": 1247,
      "replies_sent": 892,
      "videos_monitored": 12,
      "response_rate": 71.5,
    },
    "recent_activity": [
      {"video": "How to build a bot", "comments": 45, "time": "2 hours ago"},
      {"video": "Python Tutorial 2024", "comments": 89, "time": "5 hours ago"},
      {"video": "FastAPI Basics", "comments": 23, "time": "1 day ago"},
    ],
    "monitored_videos": [
      {
        "title": "How to build a bot",
        "url": "https://youtube.com/watch?v=123",
        "status": "active",
        "comments": 145,
        "auto_reply": True,
      },
      {
        "title": "Python Tutorial 2024",
        "url": "https://youtube.com/watch?v=456",
        "status": "active",
        "comments": 289,
        "auto_reply": True,
      },
      {
        "title": "FastAPI Basics",
        "url": "https://youtube.com/watch?v=789",
        "status": "paused",
        "comments": 67,
        "auto_reply": False,
      },
    ],
  }
