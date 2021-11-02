import requests


with open('token_ya.txt', 'r') as file_object:
    token = file_object.read().strip()
headers = {
    'Accept': 'application/json',
    'Authorization': f'OAuth {token}'
}

def create_folder(headers, name_folder):
    """Метод создает папку указанную пользователем на яндекс диске и возвращает имя папки"""
    while True:
        name_folder = name_folder
        response = requests.put('https://cloud-api.yandex.net/v1/disk/resources', headers=headers,
                        params={'path': name_folder})
        if response.status_code == 409:
            print(f'Папка {name_folder} уже существует, повторите ввод')
            print(response.status_code)
            break
        else:
            print(f'Папка {name_folder} создана')
            print(response.status_code)
            break
    return response.status_code


def main():

    create_folder(headers,'Yandex_A')


if __name__ == '__main__':
    main()