# ==========================================
# Python Requests Full Reference
# Author: ChatGPT
# ==========================================

import requests


# ==========================================
# 1) Simple GET Request
# ==========================================
def simple_get():
    url = "https://jsonplaceholder.typicode.com/posts/1"

    response = requests.get(url)

    print("Status Code:", response.status_code)
    print("Text Response:")
    print(response.text)


# ==========================================
# 2) GET Request with Parameters
# ==========================================
def get_with_params():
    url = "https://jsonplaceholder.typicode.com/comments"

    params = {
        "postId": 1
    }

    response = requests.get(url, params=params)

    print("Final URL:", response.url)
    print(response.json())


# ==========================================
# 3) Read JSON Response
# ==========================================
def read_json():
    url = "https://jsonplaceholder.typicode.com/users/1"

    response = requests.get(url)

    data = response.json()

    print("Name:", data["name"])
    print("Email:", data["email"])


# ==========================================
# 4) POST Request
# ==========================================
def post_data():
    url = "https://jsonplaceholder.typicode.com/posts"

    payload = {
        "title": "Python Requests",
        "body": "Learning requests library",
        "userId": 1
    }

    response = requests.post(url, json=payload)

    print("Status Code:", response.status_code)
    print(response.json())


# ==========================================
# 5) Custom Headers
# ==========================================
def custom_headers():
    url = "https://jsonplaceholder.typicode.com/posts/1"

    headers = {
        "User-Agent": "MyPythonApp"
    }

    response = requests.get(url, headers=headers)

    print(response.text)


# ==========================================
# 6) Download Image
# ==========================================
def download_image():
    image_url = "https://via.placeholder.com/300"

    response = requests.get(image_url)

    with open("downloaded_image.png", "wb") as file:
        file.write(response.content)

    print("Image downloaded successfully")


# ==========================================
# 7) Download Any File
# ==========================================
def download_file():
    file_url = "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf"

    response = requests.get(file_url)

    with open("sample.pdf", "wb") as file:
        file.write(response.content)

    print("File downloaded successfully")


# ==========================================
# 8) Timeout Example
# ==========================================
def timeout_example():
    url = "https://jsonplaceholder.typicode.com/posts"

    try:
        response = requests.get(url, timeout=3)
        print(response.status_code)
    except requests.exceptions.Timeout:
        print("Request timed out")


# ==========================================
# 9) Error Handling
# ==========================================
def error_handling():
    url = "https://wrong-url-example.com"

    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print("Error:", e)


# ==========================================
# 10) Session Example
# ==========================================
def session_example():
    session = requests.Session()

    response = session.get("https://jsonplaceholder.typicode.com/posts/1")

    print(response.json())


# ==========================================
# MAIN
# ==========================================
if __name__ == "__main__":
    simple_get()
    get_with_params()
    read_json()
    post_data()
    custom_headers()
    download_image()
    download_file()
    timeout_example()
    error_handling()
    session_example()
