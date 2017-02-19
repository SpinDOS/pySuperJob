import db_helpers
import os
import sys


def get_useful_info(vacancy):
    result = {}
    result['profession'] = vacancy['profession']
    result['candidat'] = vacancy['candidat']
    result['payment_from'] = vacancy['payment_from']
    result['payment_to'] = vacancy['payment_to']
    return result


if __name__ == '__main__':

    input_filename = sys.argv[1] if len(sys.argv) >= 2 else 'full_vacancies.plat'
    if not os.path.exists(input_filename):
        print("Передайте путь к файлу базы данных с вакансиями из superjob api "
              "в качестве параметра командной стороки. "
              "Например: python get_useful_info.py full_vacancies.plat <out_db_filename>")
        sys.exit(2)

    full_vacancies = db_helpers.get_object_from_file(input_filename)
    informative_vacancies = [get_useful_info(vacancy) for vacancy in full_vacancies]
    out_filename = sys.argv[2] if len(sys.argv) == 3 else 'informative_vacancies.plat'
    db_helpers.save_object_to_file(informative_vacancies, out_filename)
    print("Done!")