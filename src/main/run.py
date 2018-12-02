import csv


def data_setup():
    with open('./resources/testData.csv', 'r') as test_data_file:
        test_data = csv.DictReader(test_data_file)
        return test_data


def get_user_input():
    user_interest = input("What are your interests? ")
    return user_interest


if __name__ == "__main__":
    user_input = get_user_input()
    data = data_setup()
