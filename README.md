# Explain Like I'm 5

> A Flask-powered API that transforms complex text into simplified explanations using AI, with multiple reading levels from "Explain Like I'm 5" to advanced technical writing.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Installation](#installation)
- [Configuration](#configuration)
- [API Documentation](#api-documentation)
- [Project Structure](#project-structure)
- [Usage Examples](#usage-examples)


## 🎯 Overview

The ELI5 Converter is a Flask-based REST API that uses Hugging Face's language models to automatically simplify complex text. Whether you're explaining quantum physics to a child or translating technical documentation for a general audience, this tool adapts content to match your target reading level.

### Key Capabilities

- **Multiple Reading Levels**: Four preset difficulty levels (ELI5, Basic, Intermediate, Advanced)
- **AI-Powered**: Uses Google's FLAN-T5 model via Hugging Face Inference API
- **Scalable Architecture**: Built with Flask's app factory pattern for easy expansion
- **Production-Ready**: Modular design with separation of concerns

## ✨ Features

-  **Four Reading Levels**: From kindergarten to professional
-  **Hugging Face Integration**: Powered by state-of-the-art language models
-  **Clean Architecture**: Follows Flask best practices with blueprints
-  **Environment-Based Config**: Secure API key management
-  **Modular Design**: Easy to extend with new features
-  **RESTful API**: Simple JSON-based endpoints

## 🏛️ Architecture

### Technology Stack

- **Framework**: Flask 2.0+
- **AI Model**: Google FLAN-T5 Large (via Hugging Face)
- **HTTP Client**: Requests
- **Configuration**: python-dotenv

### Design Patterns

This project implements the **App Factory Pattern**, providing:
- Clean separation between configuration and runtime
- Easy testing through dependency injection
- Scalable blueprint-based routing
- Environment-specific configurations

### Request Flow

```
Client Request → Flask Route → Service Layer → Hugging Face API → Response
     ↓              ↓              ↓                    ↓             ↓
  POST /api/eli5  routes.py  hf_client.py        FLAN-T5 Model   JSON
```

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Hugging Face account (free tier)

### Step-by-Step Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/explain-like-im-5.git
   cd explain-like-im-5
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   # Create .env file
   cp .env.example .env
   
   # Edit .env with your API key
   ```

5. **Run the application**
   ```bash
   python run.py
   ```

The server will start at `http://localhost:5000`

## ⚙️ Configuration

### Environment Variables

Create a `.env` file in the project root:

```env
# Required
HF_API_KEY=your_huggingface_api_key_here

# Optional
SECRET_KEY=your_secret_key_for_sessions
FLASK_ENV=development
FLASK_DEBUG=True
```

### Getting Your Hugging Face API Key

1. Sign up at [huggingface.co](https://huggingface.co)
2. Navigate to Settings → Access Tokens
3. Create a new token with "read" permissions
4. Copy the token to your `.env` file

## 📚 API Documentation

### Endpoint: Simplify Text

**POST** `/api/eli5`

Converts complex text into a simplified explanation at the specified reading level.

#### Request

```json
{
  "text": "Quantum entanglement is a physical phenomenon that occurs when pairs of particles interact in ways such that the quantum state of each particle cannot be described independently.",
  "level": "eli5"
}
```

#### Parameters

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `text` | string | Yes | The text to simplify |
| `level` | string | No | Reading level (default: "eli5") |

#### Reading Levels

| Level | Description | Use Case |
|-------|-------------|----------|
| `eli5` | Explain Like I'm 5 | Very simple, child-friendly explanations |
| `basic` | Simple terms | General audience, no technical background |
| `intermediate` | High school level | Some technical knowledge assumed |
| `advanced` | Professional language | Technical audience, clear but detailed |

#### Response

**Success (200 OK)**
```json
{
  "result": "Imagine two magic toys that are connected. When you play with one toy, the other toy knows what happened, even if it's very far away!"
}
```

**Error (400 Bad Request)**
```json
{
  "error": "Text is required"
}
```

**Error (500 Internal Server Error)**
```json
{
  "result": "Error generating explanation"
}
```

### Example cURL Request

```bash
curl -X POST http://localhost:5000/api/eli5 \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Photosynthesis is the process by which plants convert light energy into chemical energy",
    "level": "basic"
  }'
```

## 📁 Project Structure

```
explain-like-im-5/
│
├── app/
│   ├── __init__.py              # App factory and initialization
│   ├── routes.py                # API endpoints and request handling
│   ├── config.py                # Configuration management
│   │
│   ├── services/
│   │   └── hf_client.py         # Hugging Face API integration
│   │
│   └── utils/
│       └── text_levels.py       # Reading level prompts and presets
│
├── templates/                   # HTML templates (for future frontend)
│   └── index.html
│
├── static/                      # Static assets (CSS, JS)
│   ├── css/
│   └── js/
│
├── .env                         # Environment variables (not in git)
├── .env.example                 # Example environment file
├── .gitignore                   # Git ignore rules
├── requirements.txt             # Python dependencies
├── run.py                       # Application entry point
└── README.md                    # This file
```

### Key Files Explained

#### `run.py`
Application entry point. Initializes and runs the Flask development server.

#### `app/__init__.py`
Implements the app factory pattern. Creates and configures the Flask application instance.

#### `app/routes.py`
Defines all API endpoints using Flask Blueprints. Handles request validation and response formatting.

#### `app/services/hf_client.py`
Encapsulates all Hugging Face API interactions. Provides a clean interface for text simplification.

#### `app/utils/text_levels.py`
Contains prompt templates for different reading levels. Easy to modify or extend.

#### `app/config.py`
Centralizes configuration management using environment variables.

## 💡 Usage Examples

### Python (using requests)

```python
import requests

url = "http://localhost:5000/api/eli5"
payload = {
    "text": "The mitochondria is the powerhouse of the cell",
    "level": "eli5"
}

response = requests.post(url, json=payload)
print(response.json()["result"])
```


## 🛠️ Development

### Adding a New Reading Level

1. **Update `app/utils/text_levels.py`:**
   ```python
   LEVEL_PROMPTS = {
       # ... existing levels ...
       "technical": "Explain this with technical precision and industry jargon"
   }
   ```

2. That's it! The new level is now available via the API.

### Swapping the AI Model

To use a different Hugging Face model, update `app/services/hf_client.py`:

```python
# Change this line
HF_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
```

Popular alternatives:
- `facebook/bart-large-cnn` - Better for summarization
- `google/flan-t5-xl` - Larger, more capable model
- `microsoft/DialoGPT-large` - Better for conversational tone

### Running Tests

```bash
# Install testing dependencies
pip install pytest pytest-flask

# Run tests
pytest tests/

# With coverage
pytest --cov=app tests/
```

### Code Style

This project follows PEP 8 guidelines. Format code using:

```bash
# Install formatter
pip install black

# Format all files
black app/ run.py
```

## 🚢 Deployment

### Production Considerations

1. **Use a Production Server**
   ```bash
   pip install gunicorn
   gunicorn -w 4 -b 0.0.0.0:8000 run:app
   ```

2. **Set Production Environment Variables**
   ```env
   FLASK_ENV=production
   FLASK_DEBUG=False
   SECRET_KEY=use_a_strong_random_key_here
   ```

3. **Enable HTTPS** (required for production)

4. **Add Rate Limiting**
   ```bash
   pip install flask-limiter
   ```

### Deployment Platforms

#### Heroku
```bash
# Add Procfile
echo "web: gunicorn run:app" > Procfile

# Deploy
heroku create your-app-name
git push heroku main
```

#### Docker
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["gunicorn", "-b", "0.0.0.0:8000", "run:app"]
```

## 🔧 Troubleshooting

### Common Issues

**Issue**: `ImportError: No module named 'flask'`
- **Solution**: Ensure virtual environment is activated and dependencies are installed

**Issue**: `401 Unauthorized` from Hugging Face
- **Solution**: Check that your API key is valid and properly set in `.env`

**Issue**: Model loading timeout
- **Solution**: Hugging Face models "cold start" on first request. Wait 30-60 seconds and retry.

**Issue**: `Error generating explanation`
- **Solution**: Check Hugging Face API status and your rate limits

### Debug Mode

Enable detailed logging:

```python
# In app/__init__.py
import logging
logging.basicConfig(level=logging.DEBUG)
```

## 🗺️ Roadmap

### Planned Features

- [ ] Frontend UI with React/Vue
- [ ] User authentication and session management
- [ ] Request history and saved explanations
- [ ] Batch processing for multiple texts
- [ ] Custom prompt templates
- [ ] Caching layer for repeated queries
- [ ] Analytics dashboard
- [ ] Multi-language support
- [ ] PDF and document upload support
- [ ] Browser extension