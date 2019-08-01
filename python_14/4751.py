for tc in range(1, int(input()) + 1):
    word = input()
    l = len(word)
    print('..#.' * l + '.')
    print('.#.#' * l + '.')
    for i in range(l):
        print(f'#.{word[i]}.', end='')
    print('#')
    print('.#.#' * l + '.')
    print('..#.' * l + '.')
