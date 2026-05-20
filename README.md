# Google Search Chatbot

A Django chatbot that searches Google and returns top 5 results using SerpAPI.

## Project Structure

```
google_chatbot/
├── chatbot/
│   ├── views.py         # main logic - search and return results
│   └── urls.py          # chatbot routes
├── chatbot_project/
│   ├── settings.py      # project settings
│   └── urls.py          # main URL file
├── templates/
│   └── index.html       # chat UI
├── manage.py            # Django command tool
└── README.md            # this file
```

## Requirements

- Python 3.9+
- Django 4.2
- SerpAPI library

## Setup and Run

### Step 1 - Clone or open project folder
```bash
cd google_chatbot
```

### Step 2 - Create virtual environment
```bash
python3 -m venv venv
```

### Step 3 - Activate virtual environment
```bash
source venv/bin/activate
```

### Step 4 - Install required packages
```bash
pip install django google-search-results
```

### Step 5 - Run database migrations
```bash
python3 manage.py migrate
```

### Step 6 - Start the server
```bash
python3 manage.py runserver
```

### Step 7 - Open browser
```
http://127.0.0.1:8000
```

## How It Works

1. User types keyword in chat box
2. JavaScript sends POST request to /search/
3. Django receives keyword in views.py
4. SerpAPI searches Google with the keyword
5. Top 5 results returned with title, URL and description
6. Results displayed in chat UI

## API Used

- **SerpAPI** - searches Google and returns results as JSON
- Free plan: 250 searches per month
- Website: https://serpapi.com

## Endpoints

| URL | Method | Description |
|-----|--------|-------------|
| `/` | GET | Shows chat UI |
| `/search/` | POST | Returns top 5 Google results |

## Example Request

```json
POST /search/
{
    "keyword": "Python Django"
}
```

## Example Response

```json
{
    "keyword": "Python Django",
    "results": [
        {
            "title": "Django Web Framework",
            "url": "https://www.djangoproject.com/",
            "description": "Django is a high-level Python web framework..."
        }
    ]
}
```
