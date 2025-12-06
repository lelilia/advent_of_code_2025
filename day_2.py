# Advent of Code 2025 - day 2

import re
import time

INPUT = "input2"


def regex_check(id: str, n_times: int = 2) -> int:
    res = re.findall(r"^(.*)\1{" + re.escape(str(n_times - 1)) + r"}$", id)
    return len(res)


def check_valid_1(left, right):
    sum_v = 0
    len_left = len(str(left))
    len_right = len(str(right))
    start = int(str(left)[: (len_left) // 2]) if len_left > 1 else 1
    for chunk in range(start, int(str(right)[: (len_right + 1) // 2]) + 1):
        len_chunk = len(str(chunk))
        if left <= (id := chunk * 10 ** (len_chunk) + chunk) <= right:
            sum_v += id
    return sum_v


def check_valid_2(left, right):
    len_left = len(str(left))
    len_right = len(str(right))

    seen = set()
    for chunk in range(1, int(str(right)[: (len_right + 1) // 2]) + 1):
        chunk_str = str(chunk)
        for length in range(len_left, len_right + 1):
            id = int(chunk_str * (length // len(chunk_str)))
            if left <= id <= right:
                seen.add(id)
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
    t0 = time.time()
    with open(INPUT) as f:
        data = f.read()

    for d in data.split(","):
        left_str, right_str = d.split("-")
        left, right = int(left_str), int(right_str)
        # print(left, right, len(right_str) - len(left_str))

    # assert(res:=solve("95-115", check_with_regex)) == (exp:=99), f"expected {exp} got {res}"

    print("Part 1:", solve(data, check_valid_1), "      ", time.time() - t0, "s")
    print("Part 2:", solve(data, check_valid_2), "      ", time.time() - t0, "s")

    assert (res := regex_check("99")) == (exp := 1), f"expected {exp} got {res}"
    assert (res := regex_check("111", 3)) == (exp := 1), f"expected {exp} got {res}"

    assert (res := solve("853-1994", check_valid_1)) == (
        exp := 14645
    ), f"expected {exp} got {res}"
    assert (res := solve("853-1994", check_valid_2)) == (
        exp := 16532
    ), f"expected {exp} got {res}"
    assert (res := solve("1919078809-1919280414", check_valid_1)) == (
        exp := 3838338383
    ), f"expected {exp} got {res}"
    assert (res := solve("1919078809-1919280414", check_valid_2)) == (
        exp := 5757530302
    ), f"expected {exp} got {res}"
    assert (res := solve("1212082623-1212155811", check_valid_1)) == (
        exp := 1212112121
    ), f"expected {exp} got {res}"
    assert (res := solve("1212082623-1212155811", check_valid_2)) == (
        exp := 2424233333
    ), f"expected {exp} got {res}"
    assert (res := solve("2389-4173", check_valid_1)) == (
        exp := 59085
    ), f"expected {exp} got {res}"
    assert (res := solve("2389-4173", check_valid_2)) == (
        exp := 59085
    ), f"expected {exp} got {res}"
    assert (res := solve("7490-11616", check_valid_1)) == (
        exp := 219675
    ), f"expected {exp} got {res}"
    assert (res := solve("7490-11616", check_valid_2)) == (
        exp := 230786
    ), f"expected {exp} got {res}"

    assert (res := solve("863031-957102", check_valid_1)) == (
        exp := 85578493
    ), f"expected {exp} got {res}"
    assert (res := solve("863031-957102", check_valid_2)) == (
        exp := 92871415
    ), f"expected {exp} got {res}"
    assert (res := solve("9393261874-9393318257", check_valid_1)) == (
        exp := 9393293932
    ), f"expected {exp} got {res}"
    assert (res := solve("9393261874-9393318257", check_valid_2)) == (
        exp := 9393293932
    ), f"expected {exp} got {res}"
    assert (res := solve("541406-571080", check_valid_1)) == (
        exp := 16681665
    ), f"expected {exp} got {res}"
    assert (res := solve("541406-571080", check_valid_2)) == (
        exp := 17792775
    ), f"expected {exp} got {res}"
    assert (res := solve("1207634-1357714", check_valid_1)) == (
        exp := 0
    ), f"expected {exp} got {res}"
    assert (res := solve("1207634-1357714", check_valid_2)) == (
        exp := 0
    ), f"expected {exp} got {res}"
    assert (res := solve("36706-61095", check_valid_1)) == (
        exp := 0
    ), f"expected {exp} got {res}"
    assert (res := solve("36706-61095", check_valid_2)) == (
        exp := 99999
    ), f"expected {exp} got {res}"
    assert (res := solve("863031-957102", check_valid_1)) == (
        exp := 85578493
    ), f"expected {exp} got {res}"
    assert (res := solve("863031-957102", check_valid_2)) == (
        exp := 92871415
    ), f"expected {exp} got {res}"
    assert (res := solve("3-20", check_valid_1)) == (
        exp := 11
    ), f"expected {exp} got {res}"
    assert (res := solve("3-20", check_valid_2)) == (
        exp := 11
    ), f"expected {exp} got {res}"

# ,,,36706-61095,6969667126-6969740758,761827-786237,5516637-5602471,211490-235924,282259781-282327082,587606-694322,960371-1022108,246136-353607,3-20,99-182,166156087-166181497,422-815,82805006-82876926,14165-30447,4775-7265,83298136-83428425,2439997-2463364,44-89,435793-511395,3291059-3440895,77768624-77786844,186-295,62668-105646,7490-11616,23-41,22951285-23017127

# with open("testinput2") as f:
#     test_data = f.read()
# assert (res:=solve("95-115", check_valid_1)) == 99, f"expected 99 got {res}"
# assert (res:=solve("998-1012", check_valid_1)) == 1010, f"expected 1010 got {res}"
# assert (res:=solve(test_data, check_valid_1)) == 1227775554
# assert (res:=solve("11-22", check_valid_2)) == (exp:=33), f"expected {exp} got {res}"
# assert (res:=solve("95-115", check_valid_2)) == (exp:=210), f"expected {exp} got {res}"
# assert (res:=solve("998-1012", check_valid_2)) == (exp:=999+1010), f"expected {exp} got {res}"
# assert (res:=solve("1188511880-1188511890", check_valid_2)) == (exp:=1188511885), f"expected {exp} got {res}"
# assert (res:=solve("222220-222224", check_valid_2)) == (exp:=222222), f"expected {exp} got {res}"
# assert (res:=solve("1698522-1698528", check_valid_2)) == (exp:=0), f"expected {exp} got {res}"
# assert (res:=solve(test_data, check_valid_2)) == (exp:=4174379265), f"expected {exp} got {res}"
