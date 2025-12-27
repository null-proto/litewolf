# 🐺 liteWolf [Bot]

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)](https://fastapi.tiangolo.com/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

> 🚀 Monitor, reply, and automate YouTube comments in real-time. Self-hosted, privacy-focused, and developer-friendly.

## ✨ Features

- **⚡ Real-Time Monitoring** - WebSocket-based live comment feed with instant notifications
- **🤖 Auto-Reply System** - Customizable reply templates with smart keyword detection
- **🎯 Keyword Filtering** - Target specific comments based on keywords or patterns
- **📊 Live Analytics** - Track engagement metrics with beautiful real-time dashboards
- **🔍 Comment Search** - Powerful search across all your videos with filters
- **🔐 Secure OAuth 2.0** - Official Google authentication, no API keys stored
- **📚 REST API** - Full-featured API for integration with other tools


## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Google Cloud Project with YouTube Data API v3 enabled
- OAuth 2.0 credentials (`API_TOKEN`)

### Installation

#### python virtual environment
```bash
# Clone the repository
git clone https://github.com/null-proto/litewolf
cd litewolf

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up credentials
cp .env.example .env
# Add your credentials to .env

```
#### Poetry

```bash
# Clone the repository
git clone https://github.com/null-proto/litewolf
cd litewolf

# Install dependencies
poetry install

```

### Get Google API Credentials

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project
3. Enable **YouTube Data API v3**
4. Generate new **API Token**
5. Put the token on `.env` or `.envrc` file eg.`API_TOKEN="xxxx"`

### Run the Server

```bash
# Set up credentials and Run
poetry run app

# You can also run as python module
python -m litewolf
```

## 📖 Usage
```
$ poetry run app --help
usage: 
  python -m litewolf [flags] [options]
or:
  poetry run app [flags] [options]

options:
  -h, --help       show this help message and exit
  --debug          prints debug messages
  -p, --port PORT  port number
  --host HOST      ip address
  -v, --version    show program's version number and exit
```

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details.

## 🙏 Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/) - Modern web framework
- [Google YouTube API](https://developers.google.com/youtube/v3) - YouTube Data API
- [Uvicorn](https://www.uvicorn.org/) - ASGI server


---

<p align="center">
  Made with ❤️ by <a href="https://github.com/null-proto">NP</a>
</p>
