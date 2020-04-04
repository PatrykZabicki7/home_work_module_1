# rozbije łańcuch tekstowy na listę wyrazów,
# sprawdzi, czy nie znajdują się w nim słowa niedozwolone,
# jeśli tak -- zamieni je na cztery gwiazdki (****)
# ponownie połączy listę w string i zwróci wartość.

def censor(text):
    banned_words = ["Java", "C#", "Ruby", "PHP"]
    list_of_words = text.split(" ")
    # print(list_of_words)
    for i in range(len(list_of_words)):
        print(i)
        if list_of_words[i] in banned_words:
            list_of_words[i] = "****"
            # print(list_of_words)
            new_sentence_with_censor = " ".join(list_of_words)
    return new_sentence_with_censor

print(censor("Java is the best, but PHP is the bestest!"))

# def censor(text):
#     forbidden = ["Java", "C#", "Ruby", "PHP"]
#     new_text = text.split(" ")
#     for i in range(len(new_text)):
#         if new_text[i] in forbidden:
#             new_text[i] = "****"
#     return new_text
# c = censor("Java is the best, but PHP is the bestest!")
# print(c)