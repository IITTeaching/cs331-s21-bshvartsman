import urllib
import urllib.request

def book_to_words(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    booktxt = urllib.request.urlopen(book_url).read().decode()
    bookascii = booktxt.encode('ascii','replace')
    return bookascii.split()

def radix_a_book(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    word_lst = book_to_words(book_url)
    longest_len = len(max(word_lst,key = len)) - 2
    sorted = count_sort(word_lst, longest_len + 1)
    for x in range(longest_len, -1, -1):
        sorted = count_sort(sorted, x)
    return sorted

def count_sort(word_lst, n):
    count = [0] * 128
    sorted = [None] * len(word_lst)

    for x in word_lst:
        if ((len(x) - 1) < n):
            c = 0
        else:
            c = ord(x.decode('ascii')[n])
        count[c] +=1
    for x in range(1, len(count)):
        count[x] += count[x -1]
    for x in range(len(word_lst) - 1, -1, -1):
        if len(word_lst[x]) - 1 < n:
            c = 0
        else:
            c = ord(word_lst[x].decode('ascii')[n])
        sorted[count[c] -1] = word_lst[x]
        count[c] -= 1
    return sorted

#Test Case (ran smoothly):
print(radix_a_book())