import csv

from src.main.game_picker import Games


def data_setup():
        test_data_reader = csv.DictReader(open('./resources/testData.csv'))
        return test_data_reader


if __name__ == "__main__":
    data = data_setup()
    user_interests = input("What are your interests? ")
    Games().select_games(data, user_interests)
