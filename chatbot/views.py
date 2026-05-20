from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from serpapi import GoogleSearch
import json

# SerpAPI key
SERP_API_KEY = "638553bd01524065652656ba45a1e1c49346e0eda4547780e14dd4dc63a27b16"

# Show the chat UI page
def index(request):
    return render(request, 'index.html')

# Search Google using SerpAPI and return top 5 results
def google_search(keyword):
    params = {
        "q": keyword,          # keyword to search
        "num": 5,              # get top 5 results
        "api_key": SERP_API_KEY  # our SerpAPI key
    }

    search = GoogleSearch(params)   # create search object
    results_data = search.get_dict()  # get results as dictionary

    results = []
    # organic_results contains the actual search results
    for r in results_data.get("organic_results", [])[:5]:
        results.append({
            'title': r.get('title', ''),
            'url': r.get('link', ''),
            'description': r.get('snippet', '')
        })

    return results

# Accept keyword and return top 5 Google results
@csrf_exempt
def get_results(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        keyword = data.get('keyword', '')

        if not keyword:
            return JsonResponse({'error': 'Please enter a keyword'}, status=400)

        results = google_search(keyword)
        return JsonResponse({'keyword': keyword, 'results': results}, status=200)

    return JsonResponse({'error': 'Only POST method allowed'}, status=405)
