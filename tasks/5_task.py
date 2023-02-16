
def is_valid(v_1: str, v_2: str) -> None:
    if not isinstance(v_1, str) or not isinstance(v_2, str):
        raise TypeError("Invalid data was passed to the variable. "
                        "You need to pass numerical data of type string. For example 1.10.")

    if v_1.isalpha() or v_2.isalpha():
        raise ValueError("You need to pass numerical data. For example 1.10")


def compare_versions(version_1: str, version_2: str) -> int:
    is_valid(version_1, version_2)

    v1 = ' '.join(version_1.split(".")).split()
    v2 = ' '.join(version_2.split(".")).split()

    if v1[-1] == '0':
        v1.pop()
    elif v2[-1] == '0':
        v2.pop()

    count_zero_v1 = 0
    count_zero_v2 = 0
    if v1[0] == v2[0]:
        for i in range(1, len(v1)):
            for j in range(len(v1[i])):
                if v1[i][j] == "0":
                    count_zero_v1 += 1
                else:
                    break

        for i in range(1, len(v2)):
            for j in range(len(v2[i])):
                if v2[i][j] == "0":
                    count_zero_v2 += 1
                else:
                    break

    ver1 = [int(i) for i in v1]
    ver2 = [int(j) for j in v2]

    if count_zero_v1 > count_zero_v2:
        return -1
    elif count_zero_v1 < count_zero_v2:
        return 1
    elif ver1 > ver2:
        return 1
    elif ver1 < ver2:
        return -1
    return 0


if __name__ == '__main__':
    print(compare_versions('1.1.', '1.10'))
