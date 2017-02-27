import db_helpers
import sys
import os


def translate_languages_in_ru_string(ru_string):
    return ru_string.replace(' си ', ' c ')\
                    .replace(' си шарп ', ' c# ') \
                    .replace(' питон ', ' python ') \
                    .replace(' джава ', ' java ') \
                    .replace(' джаваскрипт ', ' javascript ') \
                    .replace(' паскаль ', ' pascal ') \
                    .replace(' 1с ', ' 1c ') \
                    .replace(' пхп ', ' php ')


def calculate_languages_statistics_from_raw(raw_statistics):
    new_statistics = {}
    for language, lang_statistic in raw_statistics.items():
        with_payment = lang_statistic['With payment']
        payment_sum = lang_statistic['Payment sum']
        new_statistics[language] = {'Count': lang_statistic['Total'],
                                    'Average_payment': (payment_sum / with_payment) if with_payment else None }
    return new_statistics


def is_char_part_of_word(char):
    return char.isalpha() or char.isnumeric()


def is_language_exists_in_string(language, string_to_check):
   string_to_check = '.{}.'.format(string_to_check)
   last_index = string_to_check.find(language)
   while last_index > 0:
       if not is_char_part_of_word(string_to_check[last_index - 1]) and \
               not is_char_part_of_word(string_to_check[last_index + len(language)]):
           return True
       last_index = string_to_check.find(language, last_index + 1)
   return False


def get_languages_statistics(vacancies, languages):
    statistics = {}
    for vacancy in vacancies:
        profession = translate_languages_in_ru_string(vacancy['profession'].lower())
        candidat = translate_languages_in_ru_string(vacancy['candidat'].lower())
        payment = (int(vacancy['payment_from']) + int(vacancy['payment_to'])) / 2

        for language in languages:
            if not is_language_exists_in_string(language, profession) and \
                    not is_language_exists_in_string(language, candidat):
                continue

            if language in statistics.keys():
                language_stats = statistics[language]
            else:
                language_stats = {'Total': 0, 'With payment': 0, 'Payment sum': 0}
                statistics[language] = language_stats

            language_stats['Total'] += 1
            if payment:
                language_stats['With payment'] += 1
                language_stats['Payment sum'] += payment

    return calculate_languages_statistics_from_raw(statistics)


def print_statistics(statistics):
    for language, lang_statistic in statistics.items():
        print('{}: {} вакансий, средняя зарплата = {}'.format(language,
                                                              lang_statistic['Count'],
                                                              lang_statistic['Average_payment']
                                                              or 'нет данных'))

if __name__ == '__main__':

    input_filename = sys.argv[1] if len(sys.argv) >= 2 else 'informative_vacancies.json'
    if not os.path.exists(input_filename):
        print("Передайте путь к файлу базы данных с обработанными вакансиями из superjob api "
              "в качестве параметра командной стороки. "
              "Например: python get_languages_statistics.py informative_vacancies.json <out_db_filename>")
        sys.exit(2)

    informative_vacancies = db_helpers.get_object_from_file(input_filename)
    languages = ['python', 'c', 'c++','c#', 'java', 'javascript',
                 'pascal', '1c', 'php', 'ruby', 'swift', 'delphi']
    statistics = get_languages_statistics(informative_vacancies, languages)
    print_statistics(statistics)