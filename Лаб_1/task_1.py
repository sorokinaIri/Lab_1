numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

sym_num_1 = sum(numbers[:4])
sym_num_2 = sum(numbers[5:])
sym_num_totol = sym_num_2 + sym_num_1
long_num = len(numbers)
av_num = sym_num_totol / long_num

numbers [4] = av_num


# TODO заменить значение пропущенного элемента средним арифметическим

print("Измененный список:", numbers)
