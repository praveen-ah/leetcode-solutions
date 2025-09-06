def guess(word):
    secret = "acckzz"
    count = 0
    for i in range(len(secret)):
        if secret[i] == word[i]:
            count += 1
    return count


def findSecretWord(words):
    def match(w1, w2):
        return sum(c1 == c2 for c1, c2 in zip(w1, w2))

    while True:
        count_candidate = []
        for word in words:
            count_store = [0] * 7
            for w in words:
                if word != w:
                    matches = match(word, w)
                    count_store[matches] += 1
            count_candidate.append((max(count_store), word))

        cnt, best_word = min(count_candidate)

        matches = guess(best_word)
        if matches == len(best_word):
            print("correct_guess")
            break

        words = [w for w in words if match(best_word, w) == matches]


secret = "acckzz"
words = ["acckzz", "ccbazz", "eiowzz", "abcczz"]
findSecretWord(words)
