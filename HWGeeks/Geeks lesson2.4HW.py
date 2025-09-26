import requests

def main():
    url = "https://api.github.com"  # открытый API GitHub
    response = requests.get(url)

    if response.status_code == 200:
        print("Успешный запрос!")
        print("JSON-ответ от GitHub API:")
        print(response.json())  # печатаем словарь из JSON
    else:
        print(f"Ошибка: {response.status_code}")

if __name__ == "__main__":
    main()
