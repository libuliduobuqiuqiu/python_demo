
def find_depulicates(arrs: list[int]) -> list[int]:
    res = []
    i = 0

    while i < len(arrs):
        t = arrs[i]
        if t >= 0 and t-1 != i:
            if arrs[t-1] == t:
                res.append(t)
                arrs[t-1] *= -1
            else:
                arrs[i], arrs[t-1] = arrs[t-1], t
                i -= 1
        i += 1

    return res


if __name__ == "__main__":
    a = [2, 1, 3, 4, 5, 1, 2]
    print(find_depulicates(a))
