import itertools
import os
import random


# 1. File exists

def file_exists(directory, file):
  # TODO
  return False


# 2. Choosing sums

def sum_to_target(numbers, target):
  # TODO
  return False

def sum_to_target_challenge(numbers, target):
  # TODO
  return None


# 3. Generating subsets

def subsets_of_size(items, count):
  # TODO
  return []


# 4. Maze solving

def solve_maze(maze, x, y, goal_x, goal_y):
  # TODO
  return False

def solve_maze_challenge(maze, x, y, goal_x, goal_y):
  # TODO
  return None



# You don't need to change anything below here - everything below here just
# tests whether your code works correctly. You can run this file as
# "python exercises.py" and it will tell you if anything is wrong.












def test_sum_to_target():
  cases = [
    ([2, 4, 8], 10, True),
    ([2, 4, 8], 14, True),
    ([2, 4, 8], 9, False),
    ([2, 4, 8], 0, True),
  ]
  for items, target, expected in cases:
    actual = sum_to_target(items, target)
    if actual != expected:
      print('sum_to_target(%r, %r) returned %r, but it should have returned %r' % (
          items, target, actual, expected))
      return
  print('sum_to_target is correct')

def test_sum_to_target_challenge():
  cases = [
    ([2, 4, 8], 10, [2, 8]),
    ([2, 4, 8], 14, [2, 4, 8]),
    ([2, 4, 8], 9, None),
    ([2, 4, 8], 0, []),
  ]
  for items, target, expected in cases:
    actual = sum_to_target_challenge(items, target)
    if actual != expected:
      print('sum_to_target_challenge(%r, %r) returned %r, but it should have returned %r' % (
          items, target, actual, expected))
      return
  print('sum_to_target_challenge is correct')

def test_file_exists():
  if not file_exists('.', 'README.md'):
    print('file_exists did not find README.md')
    return
  if not file_exists('.', 'you_found_it.txt'):
    print('file_exists did not find you_found_it.txt')
    return
  if file_exists('.', 'not_a_real_file.txt'):
    print('file_exists found not_a_real_file.txt, but it does not exist')
    return
  print('file_exists is correct')


def test_subsets_of_size():
  cases = [
    ([1, 2, 3, 4], 0, [[]]),
    ([1, 2, 3, 4], 1, [[1], [2], [3], [4]]),
    ([1, 2, 3, 4], 2, [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]),
    ([1, 2, 3, 4], 3, [[1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4]]),
    ([1, 2, 3, 4], 4, [[1, 2, 3, 4]]),
    ([1, 2, 3, 4], 5, []),
  ]
  for items, target, expected in cases:
    actual = subsets_of_size(items, target)
    if sorted(actual) != sorted(expected):
      print('subsets_of_size(%r, %r) returned %r, but it should have returned %r (order doesn\'t matter)' % (
          items, target, actual, expected))
      return
  print('subsets_of_size is correct')

def test_solve_maze_error(maze, path, message):
  maze.print_field()
  print('Your solution was: %r' % (path,))
  print('Solution failed: %s' % (message,))

def test_solve_maze_path(maze, path):
  maze.clear_visited()

  if path is None:
    test_solve_maze_error(maze, path, 'no solution was returned')

  x, y = 1, 1
  maze.mark_visited(x, y)
  for i, direction in enumerate(path):
    if direction.lower() == 'up':
      y -= 1
    elif direction.lower() == 'down':
      y += 1
    elif direction.lower() == 'left':
      x -= 1
    elif direction.lower() == 'right':
      x += 1
    else:
      test_solve_maze_error(maze, path, 'direction %d (%s) is not up, down, left, or right' % (
          i, direction))
      return False

    if maze.is_wall(x, y):
      test_solve_maze_error(maze, path, 'direction %d (%s) took us into a wall at (%d, %d)' % (
          i, direction, x, y))
      return False

    if maze.was_visited(x, y):
      test_solve_maze_error(maze, path, 'direction %d (%s) took us into a cell we had already visited: (%d, %d)' % (
          i, direction, x, y))
      return False

    maze.mark_visited(x, y)

  if (x, y) != (maze.width() - 2, maze.height() - 2):
    test_solve_maze_error(maze, path, 'path doesn\'t end at the goal (%d, %d); instead it ends at (%d, %d)' % (
        maze.width() - 2, maze.height() - 2, x, y))
    return False

  return True

def test_solve_maze(test_path=False):

  # test some basic mazes
  mazes = (
      (['#####',
        '#   #',
        '#####'], 5, 3, True),

      (['#######',
        '# #   #',
        '# # # #',
        '#   # #',
        '#######'], 7, 5, True),

      (['#########',
        '#   #   #',
        '# ### # #',
        '#     # #',
        '### ### #',
        '#     # #',
        '#########'], 9, 7, True),

      (['#####',
        '# # #',
        '#####'], 5, 3, False),

      (['#######',
        '# #   #',
        '# ### #',
        '#   # #',
        '#######'], 7, 5, False),

      (['#########',
        '#   #   #',
        '# ##### #',
        '#     # #',
        '### ### #',
        '#     # #',
        '#########'], 9, 7, False))

  for maze, w, h, solvable in mazes:
    f = Field(w, h, fixed_maze=''.join(maze))
    ret = solve_maze(f, 1, 1, w - 2, h - 2)
    if ret != solvable:
      print('the following maze is %s, but solve_maze returned %r:' % (
          'solvable' if solvable else 'not solvable', ret))
      f.print_field()
      return False
    if test_path:
      f.clear_visited()
      path = solve_maze_challenge(f, 1, 1, w - 2, h - 2)
      if solvable:
        if not test_solve_maze_path(f, path):
          return False
      elif path is not None:
        print('the following maze is not solvable, but solve_maze_challenge returned %r:' % (
            path,))
        f.print_field()
        return False

  # test larger always-solvable mazes
  for size in (5, 15, 25, 35):
    f = Field(size, size, generate_columns=True, generate_maze=True)
    ret = solve_maze(f, 1, 1, size - 2, size - 2)
    if not ret:
      print('the following maze is solvable, but solve_maze returned %r:' % (ret,))
      f.print_field()
      return
    if test_path:
      f.clear_visited()
      path = solve_maze_challenge(f, 1, 1, size - 2, size - 2)
      if not test_solve_maze_path(f, path):
        return False

  if test_path:
    print('solve_maze_challenge is correct')
  else:
    print('solve_maze is correct')
  return True


class Field(object):
  def __init__(self, w, h, fixed_maze=None, generate_columns=True,
               generate_maze=True):
    # w and h must be odd numbers
    assert (w & 1) and (h & 1), "width and height must be odd numbers"
    assert generate_columns or not generate_maze, \
        "generate_columns must be True if generate_maze is True"

    if fixed_maze is not None:
      assert len(fixed_maze) == w * h

      # generate the base field
      self.data = []
      for y in range(h):
        line = []
        for x in range(w):
          line.append(fixed_maze[y * w + x] != ' ')
        self.data.append(line)

    else:
      # all (odd, odd) spaces are walls
      # all edge spaces are walls
      # all (even, even) spaces are open

      # generate the base field
      self.data = []
      for y in range(h):
        line = []
        for x in range(w):
          is_edge = (x == 0) or (x == w - 1) or (y == 0) or (y == h - 1)
          is_column = generate_columns and (not ((x & 1) or (y & 1)))
          is_wall = generate_maze and (not ((x & 1) and (y & 1)))
          line.append(is_edge or is_column or is_wall)
        self.data.append(line)

      # generate a maze if requested
      if generate_maze:
        visited_stack = []
        current_x, current_y = 1, 1
        cells_pending = set(itertools.product(range(1, w, 2), range(1, h, 2)))
        cells_pending.remove((1, 1))
        while cells_pending:
          unvisited_neighbors = filter(lambda z: z in cells_pending, [
              (current_x - 2, current_y), (current_x + 2, current_y),
              (current_x, current_y - 2), (current_x, current_y + 2)])
          if unvisited_neighbors:
            new_x, new_y = random.choice(unvisited_neighbors)
            visited_stack.append((current_x, current_y))
            self.data[(current_y + new_y) / 2][(current_x + new_x) / 2] = False
            current_x, current_y = new_x, new_y
            cells_pending.remove((current_x, current_y))
          elif visited_stack:
            current_x, current_y = visited_stack.pop(-1)

    self.clear_visited()

  def print_field(self):
    print('y\\x ' + ''.join('%3d' % i for i in range(len(self.data[0]))))
    for y, line in enumerate(self.data):
      print(('%3d ' % y) + ''.join(('###' if x else '   ') for x in line))

  def print_visited(self):
    print('y\\x ' + ''.join('%3d' % i for i in range(len(self.visited[0]))))
    for y, line in enumerate(self.visited):
      print(('%3d ' % y) + ''.join(('---' if x else '   ') for x in line))

  def is_wall(self, x, y):
    return self.data[y][x]

  def was_visited(self, x, y):
    return self.visited[y][x]

  def mark_visited(self, x, y):
    self.visited[y][x] = True

  def clear_visited(self):
    self.visited = []
    while len(self.visited) < self.height():
      self.visited.append([False] * self.width())

  def width(self):
    return len(self.data[0])

  def height(self):
    return len(self.data)


if __name__ == '__main__':
  test_sum_to_target()
  test_sum_to_target_challenge()
  test_file_exists()
  test_subsets_of_size()
  if test_solve_maze():
    test_solve_maze(test_path=True)
