def data_input():
    return input().split()


def conc(set1, set2, k):
    list1 = list(set1)
    list2 = list(set2)
    new_set = set()
    for i in list1:
        for j in list2:
            new_set.add((i + j) % k)
    return new_set


def update_words_len(str, k):
    stack = []
    while len(str) > 0:
        if str[0] == 'a' or str[0] == 'b' or str[0] == 'c':
            stack.append({1})
        elif str[0] == '1':
            stack.append({0})
        elif str[0] == '*':
            if len(stack) == 0:
                return True, set()
            if stack[-1] != {0}:
                stack.pop()
                stack.append(set([i for i in range(k)]))
        elif str[0] == '+':
            if len(stack) < 2:
                return True, set()
            set1 = stack.pop()
            set2 = stack.pop()
            stack.append(set1 | set2)
        elif str[0] == '.':
            if len(stack) < 2:
                return True, set()
            set1 = stack.pop()
            set2 = stack.pop()
            stack.append(conc(set1, set2, k))
        else:
            return True, set()
        str = str[1:]

    if len(stack) == 1:
        return False, stack[0]
    else:
        return True, set()


def find_answer(input_tuple):
    input_str = input_tuple[0]
    k = int(input_tuple[1])
    l = int(input_tuple[2])
    words_len = update_words_len(input_str, k)
    if words_len[0]:
        return "ERROR"
    if l in words_len[1]:
        return "YES"
    return "NO"

if __name__ == '__main__':
    print(find_answer(data_input()))
