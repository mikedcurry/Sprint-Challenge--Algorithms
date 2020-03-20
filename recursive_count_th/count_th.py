'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

count = 0

def count_th(word, count=0):
    if len(word) < 2:
        print('if')
        return count
    elif word[:2] == 'th':
        count += 1
        return count_th(word[1:], count)
    else:
      return count_th(word[1:], count)
