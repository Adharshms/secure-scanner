import requests

def scan_website(url):
    result = {}

    if not url.startswith("http"):
        url = "https://" + url

    try:
        response = requests.get(url, timeout=5)
        headers = response.headers

        result["https"] = url.startswith("https")
        result["headers"] = {
            "Content-Security-Policy": "Content-Security-Policy" in headers,
            "X-Frame-Options": "X-Frame-Options" in headers,
            "Strict-Transport-Security": "Strict-Transport-Security" in headers
        }

    except Exception as e:
        result["error"] = str(e)

    return result
