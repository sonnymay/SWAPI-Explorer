import requests
import json

class StarWarsAPI:
    def __init__(self):
        self.base_url = 'https://swapi.dev/api/'

    def get_resource(self, category, id):
        url = f'{self.base_url}{category}/{id}/'
        response = requests.get(url)
        data = json.loads(response.text)
        return data

    def get_film(self, id):
        return self.get_resource('films', id)

    def get_person(self, id):
        return self.get_resource('people', id)

def main():
    api = StarWarsAPI()

    while True:
        print('1. Get information about a film')
        print('2. Get information about a person')
        print('3. Quit')
        choice = input('Choose an option: ')

        if choice == '1':
            film_id = input('Enter the id of the film: ')
            film_info = api.get_film(film_id)
            print(json.dumps(film_info, indent=4))
        elif choice == '2':
            person_id = input('Enter the id of the person: ')
            person_info = api.get_person(person_id)
            print(json.dumps(person_info, indent=4))
        elif choice == '3':
            break
        else:
            print('Invalid choice. Please try again.')

if __name__ == '__main__':
    main()
