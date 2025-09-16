
def main():
    text = input("Text:").lower()
    count_l = count_letters(text)
    #print(count_l)
    count_w = count_words(text)
    #print(count_w)
    count_s = count_sentences(text)
    #print(count_s)
    average_l = (count_l /count_w ) * 100
    average_s = (count_s /count_w) * 100
    #print(average_l,average_s)
    index = compute_readability(average_l , average_s)
    if index < 1:
        print("Before Grade 1")
    elif index > 16:
        print("Grade 16+")
    else:
        print(f"Grade {round(index)}")

def count_letters(s):
    letters_count = 0
    for c in s:
        if c.isalpha():
            letters_count += 1
    return letters_count

def count_words(s):
    word_count = 1
    for c in s:
        if " " in c:
            word_count +=1
    return word_count

def count_sentences(s):
    sentence_count = 0
    for c in s:
        if "." in c or "!" in c or "?" in c:
            sentence_count += 1
    return sentence_count


def compute_readability(l,s):
    index = 0.0588 * l - 0.296 * s - 15.8
    return index


if __name__ == "__main__":
    main()
