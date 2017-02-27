import db_helpers
import os
import sys


def get_vacancy_description_and_payment(vacancy):
    result = {}
    result['profession'] = vacancy['profession'] or ''
    result['candidat'] = vacancy['candidat'] or ''
    result['payment_from'] = vacancy['payment_from'] or 0
    result['payment_to'] = vacancy['payment_to'] or 0
    return result


if __name__ == '__main__':

    input_filename = sys.argv[1] if len(sys.argv) >= 2 else 'full_vacancies.json'
    if not os.path.exists(input_filename):
        print("Передайте путь к файлу базы данных с вакансиями из superjob api "
              "в качестве параметра командной стороки. \n"
              "Например: python get_vacancy_description_and_payment.py "
              "full_vacancies.json <out_db_filename>")
        sys.exit(2)

    full_vacancies = db_helpers.get_object_from_file(input_filename)
    informative_vacancies = [get_vacancy_description_and_payment(vacancy) for vacancy
                             in full_vacancies]
    out_filename = sys.argv[2] if len(sys.argv) == 3 else 'informative_vacancies.json'
    db_helpers.save_object_to_file(informative_vacancies, out_filename)
    print("Done!")