list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды

количество_участников = len(list_players)

middle_index = len(list_players) // 2

первая_команда = list_players[:middle_index]
вторая_команда = list_players[middle_index:]

print( первая_команда)
print( вторая_команда)