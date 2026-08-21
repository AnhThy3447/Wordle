class Wordle:
    def __init__(self, word):
        self.word = word
        self.letter_list = []
        self.create_letter_list(word)

    def create_letter_list(self, word):
        unique_letters = []
        for i in range(5):
            self.letter_list.append([word[i], i, 1])
            if word[i] not in unique_letters:
                unique_letters.append(word[i])
            else:
                same_letter = []
                for letter, index, _ in self.letter_list:
                    if letter == word[i]:
                        same_letter.append(index)
                num_same_letter = len(same_letter)
                for j in same_letter:
                    self.letter_list[j] = [word[i], j, num_same_letter]

    def check_letter(self, guess_word):
        guess_label = [0, 0, 0, 0, 0]
        right_letter = []
        checked_letters = []

        # Check right letter first
        for i in range(5):
            if guess_word[i] == self.word[i]:
                guess_label[i] = "green"
                right_letter.append(guess_word[i])

        # Label yellow and grey
        for i in range(5):
            letter = guess_word[i]
            checked_letters.append(letter)
            if guess_label[i] == "green":
                continue
            if guess_word[i] in self.word and \
               right_letter.count(letter) + checked_letters.count(letter) <= self.letter_list[i][2]:
                guess_label[i] = "gold1"
            else:
                guess_label[i] = "grey"
        return guess_label