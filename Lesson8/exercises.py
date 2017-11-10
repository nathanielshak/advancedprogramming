# 1. round_sum

# This problem is on CodingBat; go to http://codingbat.com/prob/p179960 to work
# on it. When you're done, come back here.


# 2. Find last letters

def find_last_letters(word):
  ret = {}
  # TODO
  return ret


# 3. Words by length

def words_by_length(words):
  ret = {}
  # TODO
  return ret

def words_by_length_challenge(words):
  ret = {}
  # TODO
  return ret

def word_appears(words_dict, word):
  # TODO
  return False


# 4A. Splitting lists

def split_list(items, count):
  ret = []
  # TODO
  return ret

def split_list_challenge(items, count):
  ret = []
  # TODO
  return ret


# 4B. Finding items in nested lists

def which_list(lists, item):
  # TODO
  return -1


# Don't forget to figure out the Big O runtime of parts A and B!


# You don't need to change anything below here - everything below here just
# tests whether your code works correctly. You can run this file as
# "python exercises.py" and it will tell you if anything is wrong.












def test_find_last_letters():
  expected = {'c': 0, 'h': 1, 'a': 2, 'l': 4, 'e': 8, 'n': 6, 'g': 7}
  ret = find_last_letters('challenge')
  if ret != expected:
    print 'find_last_letters should return %r, but it returned %r' % (
        expected, ret)
  else:
    print 'find_last_letters is correct'

def test_words_by_length():
  animals = ['cat', 'dog', 'bird', 'sheep', 'rat', 'horse', 'human', 'lion']
  expected = {3: ['cat', 'dog', 'rat'],
              4: ['bird', 'lion'],
              5: ['sheep', 'horse', 'human']}
  ret = words_by_length(animals)
  if ret != expected:
    print 'find_last_letters(%r) should return %r, but it returned %r' % (
        animals, expected, ret)
    return
  else:
    print 'find_last_letters is correct'

  cases = [
    # (word, expected_result)
    ('cat', True),
    ('sheep', True),
    ('capybara', False),
    ('donut', False),  # don't be silly; this isn't an animal
  ]
  for word, expected_result in cases:
    result = word_appears(expected, word)
    if expected_result != result:
      print 'word_appears(%r) should return %r, but it returned %r' % (
          word, expected_result, result)
      return
  print 'word_appears is correct'

  ret = words_by_length_challenge(animals)
  if not ret:
    return  # don't print anything if the challenge wasn't attempted

  if ret != expected:
    print 'find_last_letters_challenge(%r) should return %r, but it returned %r' % (
        animals, expected, ret)
  else:
    print 'find_last_letters_challenge is correct'

def test_split_list():
  cases = [
    # (input_list, sublist_size, expected_result)
    ([1, 3, 5, 7], 2, [[1, 3], [5, 7]]),
    ([1, 3, 5, 7, 9, 11, 13], 3, [[1, 3, 5], [7, 9, 11], [13]]),
    ([1, 3, 5, 7], 10, [[1, 3, 5, 7]]),
    ([], 3, []),
  ]
  for input_list, sublist_size, expected_result in cases:
    result = split_list(input_list, sublist_size)
    if result != expected_result:
      print 'split_list(%r, %r) should return %r, but it returned %r' % (
          input_list, sublist_size, expected_result, result)
      return
  print 'split_list is correct'

  which_list_input = [[1, 3, 5], [7, 9, 11], [13]]
  which_list_cases = [(1, 0), (5, 0), (9, 1), (13, 2), (17, -1)]
  for item, expected_result in which_list_cases:
    result = which_list(which_list_input, item)
    if result != expected_result:
      print 'which_list(%r, %r) should return %r, but it returned %r' % (
          which_list_input, item, expected_result, result)
      return
  print 'which_list is correct'

  # check if the challenge was attempted
  if split_list_challenge([1], 1):
    for input_list, sublist_size, expected_result in cases:
      result = split_list_challenge(input_list, sublist_size)
      if result != expected_result:
        print 'split_list_challenge(%r, %r) should return %r, but it returned %r' % (
            input_list, sublist_size, expected_result, result)
        return
    print 'split_list_challenge is correct'


if __name__ == '__main__':
  test_find_last_letters()
  test_words_by_length()
  test_split_list()
