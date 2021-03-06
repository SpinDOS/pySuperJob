from superjob_api import make_superjob_request
import sys
import db_helpers


def get_moscow_programmers():
    catalogue_id = 48 # id каталога "Разработка, программирование"
    town_id = 4 # id города Москва
    vacancies_count = 100 # api запрещает запрашивать больше 100 вакансий
    keyword = 'Программист'
    params={'town': town_id, 'catalogues': catalogue_id, 'count': vacancies_count, 'keyword': keyword}
    return make_superjob_request('vacancies/', params)


def print_response_error(error):
    if error['code'] == 400:
        print('Неверный ключ api. Установите его с помощью переменной окружения SUPERJOB_API_KEY')
    else:
        print("Неизвестная ошибка: " + str(error))


if __name__ == '__main__':
    response = get_moscow_programmers()
    if 'error' in response:
        print_response_error(response['error'])
        sys.exit(1)
    vacancies = response['objects']
    out_filename = sys.argv[1] if len(sys.argv) == 2 else 'full_vacancies.json'
    db_helpers.save_object_to_file(vacancies, out_filename)
    print("Done")
