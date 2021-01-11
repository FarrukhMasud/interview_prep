import datetime


from collections import Counter


def solution(S):
    if not S or len(S) <= 1:
        return 0
    cntr = Counter(S)
    if len(cntr) == 1:
        return 0
    rev_cntr = dict()
    for k in cntr:
        count = cntr[k]
        rev_cntr.setdefault(count, []).append(k)
    # if everything is already unique then no need for deletion
    if len(cntr) == len(rev_cntr):
        return 0

    deletions = 0
    keys = set()
    for k in rev_cntr:
        letters = rev_cntr[k]
        if len(letters) <= 1:
            continue

        # iterate all for removal except 0th index one

        for i in range(len(letters) - 1, 0, -1):
            d = 1
            while (k - d) > 0:
                if (k - d) not in rev_cntr and (k - d) not in keys:
                    keys.add(k - d)
                    break
                d += 1
            deletions += d
    return deletions


print(solution("example"))
