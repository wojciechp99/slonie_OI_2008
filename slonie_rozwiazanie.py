def get_values(file_name):
    try:
        with open(file_name) as file:
            values = file.readlines()

            number_of_elephants = int(values[0])
            weights = list(map(int, values[1].split()))
            original = [int(i) - 1 for i in values[2].split()]
            swap_to = [int(j) - 1 for j in values[3].split()]

        return elephants(number_of_elephants, weights, original, swap_to)
    except:
        return """Wrong file name, try something like: 
C:/Users/username/Desktop/slo1.in or slo1.in if file is in the same directory"""


def elephants(number, weight, original, swapped_list):
    answer = 0
    minimum_weight = min(weight)

    belongs_to_cycle = [False for _ in range(number)]
    array = [0 for _ in range(number)]
    for index in range(number):
        array[swapped_list[index]] = original[index]

    for i in range(0, number):
        if not belongs_to_cycle[i]:
            minimum_value = float("inf")
            sum_of_weight = 0
            current = i
            length_of_cycle = 0

            while True:
                minimum_value = min(minimum_value, weight[current])
                sum_of_weight += weight[current]
                current = array[current]
                belongs_to_cycle[current] = True
                length_of_cycle += 1
                if current == i:
                    break

            answer += min(sum_of_weight + (length_of_cycle - 2) * minimum_value,
                          sum_of_weight + minimum_value + (length_of_cycle + 1) * minimum_weight)
    return answer


if __name__ == "__main__":
    # import sys
    # argument_from_terminal = sys.argv[1]  # takes argument from terminal example: python slonie_rozwiazanie.py slo1.in
    # total_mass_of_swapped_elephants = get_values(argument_from_terminal)

    argument = input("Write file path: ")  # takes argument from input example: slo1.in
    total_mass_of_swapped_elephants = get_values(argument)
    print(total_mass_of_swapped_elephants)
