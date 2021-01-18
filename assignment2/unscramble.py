def unscramble():
    word = input("Enter word to find: ")
    ls = permutations(word)
    new_ls = []
    f = open("wordlist.txt", "r")
    content = f.read().splitlines()

    for line in content:
        if (len(line) == len(word)):
            for x in range(len(ls)):
                if ls[x] == line:
                    new_ls.append(line)
    print(new_ls)


def permutations(string):
    permutation_list = []
    if len(string) == 1:
        return [string]
    else:
        for char in string:
            [permutation_list.append(char + a)
             for a in permutations(string.replace(char, "", 1))]
    return permutation_list


unscramble()
