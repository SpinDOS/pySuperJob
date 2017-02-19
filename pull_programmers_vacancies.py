from superjob_api import make_superjob_request
import sys
import db_helpers


def get_moscow_programmers():
    catalogue_id = 48 # id каталога "Разработка, программирование"
    town_id = 4 # id города Москва
    vacancies_count = 100 # api запрещает запрашивать больше 100 вакансий
    params={'town': town_id, 'catalogues': catalogue_id, 'count': vacancies_count, 'keyword': 'Программист'}
    return make_superjob_request('vacancies/', params)


def check_response_for_error(response):
    error = response.get('error', None)
    if error:
        if error['code'] == 400:
            print('Неверный ключ api. Установите его с помощью переменной окружения SUPERJOB_API_KEY')
        else:
            print("Неизвестная ошибка: " + str(error))
        sys.exit(1)


if __name__ == '__main__':
    response = get_moscow_programmers()
    check_response_for_error(response)
    vacancies = response['objects']
    out_filename = sys.argv[1] if len(sys.argv) == 2 else 'full_vacancies.plat'
    db_helpers.save_object_to_file(vacancies, out_filename)
    print("Done")
