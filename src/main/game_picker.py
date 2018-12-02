class Games:

    @staticmethod
    def select_games(data, interests):
        for line in data:
            if line['mainGenre'] == interests or line['subGenre'] == interests:
                print("We have found this game that matches the interests you provided " + line["name"])
