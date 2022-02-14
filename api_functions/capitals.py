import json
import random

# TODO:
# load json data
# sort it correctly
# generate a questions



def load_json():
    with open('./data/country-list-with-ids.json', 'r', encoding='utf-8') as file:
        data=file.read()
        return json.loads(data)


def get_random_capital(data):
    # how to get a captial
    # data[NUM]['country']
    # data[NUM]['capital']
    # list goes out of bounds if we hit the acutally max num due to indexing at 0
    max_num = len(data) - 1
    random_num = random.randrange(0, max_num)
    question = {'country': data[random_num]['country'],
                'capital': data[random_num]['capital'],
                }

    return question

def get_choices(data, question):
    max_num = len(data) - 1
    # should init choices in first func with correct
    choices = []
    i = 0
    while i < 3:
        random_num = random.randrange(0, max_num)
        country = data[random_num]['capital']
        if country == question['capital']:
            continue
        elif country in choices:
            continue
        else:
            choices.append(country)
            i = i + 1


    return choices


def gen_rand_choices(question, choices):
    country = question['capital']
    choices.append(country)
    random.shuffle(choices)


    return choices



def make_json(question, rand_choices):
    country = question['country']
    response = {
              'question': f'What is the Capital of {country}',
              'choices': rand_choices,
              'correct': question['capital'],
              }
    return response


def get_capital_question():
    data = load_json()
    question = get_random_capital(data)
    choices = get_choices(data, question)
#    print(choices)
    rand_choices = gen_rand_choices(question, choices)
#    print(rand_choices)
    correct = question['country']
    return make_json(question, rand_choices)
#    print(json.dumps(make_json(question, rand_choices)))








if __name__ == "__main__":
    """
    data = load_json()
    question = get_random_capital(data)
    choices = get_choices(data, question)
#    print(choices)
    rand_choices = gen_rand_choices(question, choices)
#    print(rand_choices)
    correct = question['country']
    print(json.dumps(make_json(question, rand_choices)))
    """
    get_capital_question()




