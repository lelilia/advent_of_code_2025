# Advent of Code 2025 - day 2


INPUT = "input2"


def check_valid_1(left, right):
    sum = 0
    len_left = len(str(left))
    len_right = len(str(right))
    start =int(str(left)[:(len_left)//2]) if len_left > 1 else 1
    for chunk in range(start,int(str(right)[:(len_right+1)//2])+1 ):
        len_chunk = len(str(chunk))
        if left <= (id := chunk * 10 ** (len_chunk) + chunk) <= right:
            sum += id
    return sum


def check_valid_2(left, right):
    len_left = len(str(left))
    len_right = len(str(right))

    seen = []
    for chunk in range(1, int(str(right)[:(len_right+1)//2])+1 ):
        chunk_str = str(chunk)
        for length in range(len_left, len_right + 1):
            id = int(chunk_str * (length // len(chunk_str)))
            if left <= id <= right:
                if id not in seen:
                    seen.append(id)
    return sum(seen)


def solve(data, check_func=check_valid_1):
    sum_invalid = 0
    data = data.split(",")
    for d in data:
        left, right = d.split("-")
        left, right = int(left), int(right)
        sum_invalid += check_func(left, right)
    return sum_invalid


if __name__ == "__main__":
    with open(INPUT) as f:
        data = f.read()

    print("Part 1:", solve(data, check_valid_1))
    print("Part 2:", solve(data, check_valid_2))

    with open("testinput2") as f:
        test_data = f.read()
    assert (res:=solve("95-115", check_valid_1)) == 99, f"expected 99 got {res}"
    assert (res:=solve("998-1012", check_valid_1)) == 1010, f"expected 1010 got {res}"
    assert (res:=solve(test_data, check_valid_1)) == 1227775554
    assert (res:=solve("11-22", check_valid_2)) == (exp:=33), f"expected {exp} got {res}"
    assert (res:=solve("95-115", check_valid_2)) == (exp:=210), f"expected {exp} got {res}"
    assert (res:=solve("998-1012", check_valid_2)) == (exp:=999+1010), f"expected {exp} got {res}"
    assert (res:=solve("1188511880-1188511890", check_valid_2)) == (exp:=1188511885), f"expected {exp} got {res}"
    assert (res:=solve("222220-222224", check_valid_2)) == (exp:=222222), f"expected {exp} got {res}"
    assert (res:=solve("1698522-1698528", check_valid_2)) == (exp:=0), f"expected {exp} got {res}"
    assert (res:=solve(test_data, check_valid_2)) == (exp:=4174379265), f"expected {exp} got {res}"