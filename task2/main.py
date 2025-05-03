import requests


class HTTPStatusException(Exception):
    pass


def process_response(response):
    code = response.status_code
    if 100 <= code < 400:
        print(f"Status: {code}, Body: {response.text}")
    elif 400 <= code < 600:
        raise HTTPStatusException(
            f"Error status: {code}, Body: {
                response.text}")


def main():
    urls = [
        "https://httpstat.us/200",
        "https://httpstat.us/226",
        "https://httpstat.us/300",
        "https://httpstat.us/418",
        "https://httpstat.us/510"
    ]
    for url in urls:
        try:
            resp = requests.get(url)
            process_response(resp)
        except HTTPStatusException as e:
            print(f"Exception: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
