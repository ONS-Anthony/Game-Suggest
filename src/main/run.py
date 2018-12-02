import csv


def data_setup():
    with open('./resources/testData.csv', 'r') as test_data_file:
        test_data = csv.DictReader(test_data_file)
        return test_data


if __name__ == "__main__":
    data = data_setup()
