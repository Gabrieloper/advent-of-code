from typing import List


def evaluate_num(num: int) -> int:
    num_arr: List[int] = [int(x) for x in list(str(num))]
    is_valid = False
    num_len: int = len(num_arr)
    if num_len % 2 != 0:
        return 0
    midpoint = num_len // 2
    num_arr_half_1 = num_arr[:midpoint]
    num_arr_half_2 = num_arr[midpoint:]

    return num if num_arr_half_1 == num_arr_half_2 else 0


def parse_file_ids(id_ranges):
    total = 0
    id_arr: List[str] = id_ranges.split(",")
    print(id_arr)
    for id in id_arr:
        num_range = id.split("-")
        start = int(num_range[0])
        stop = int(num_range[1]) + 1
        for num in range(start, stop):
            total += evaluate_num(num)
    return total


if __name__ == "__main__":
    total = 0
    file = open("./files/day-2.txt")
    id_ranges: str = file.readline()
    total = parse_file_ids(id_ranges)
    print(total)
    file.close()
