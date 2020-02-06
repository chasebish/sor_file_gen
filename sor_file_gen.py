# !usr/bin/python3

import string
import random
import argparse

def arg_parser():
    parser = argparse.ArgumentParser(description='Generates random sor files')
    parser.add_argument('-rows', type = int,
                        help="number of rows to generate", dest='input_rows')
    parser.add_argument('-columns', type=int,
                        help="number of rows to generate", dest="input_columns")
    parser.add_argument('-num_range', type=int, default=25000, required=False,
                        help="max value for random ints and floats", dest="num_range")
    args = parser.parse_args()

    if not ((args.input_rows or args.input_columns)):
      parser.error("Please specify number of rows and columns.")

    return args

def main():
  args = arg_parser()
  file_gen(args.input_rows, args.input_columns, args.num_range)


def file_gen(rows, columns, num_range):
  ROWS = rows
  COLUMNS = columns
  FLOAT_INT_RANGE = num_range

  bool_text = ""
  int_text = ""
  float_text = ""
  string_text = ""
  random_text = ""

  def make_bool():
    return str(random.randint(0, 1))

  def make_int():
    return str(random.randint(0, FLOAT_INT_RANGE))

  def make_float():
    return str(random.random() * FLOAT_INT_RANGE)

  def make_string():
    string_length = random.randint(3, 15)
    allowed_chars = string.ascii_letters + string.digits
    return ''.join(random.choice(allowed_chars) for i in range(string_length))

  def make_random():
    random_choice = random.randint(0, 10)
    if random_choice < 5:
      return make_bool()
    elif random_choice < 8:
      return make_int()
    elif random_choice < 10:
      return make_float()
    else:
      return make_string()

  # loop through rows
  for i in range(0, ROWS):

    # loop through columns
    for j in range(0, COLUMNS):

      # bool creation
      bool_text += "<" + make_bool() + ">"
      # int creation
      int_text += "<" + make_int() + ">"
      # float creation
      float_text += "<" + make_float() + ">"
      # string creation
      string_text += "<" + make_string() + ">"
      # random creation
      make_random()
      random_text += "<" + make_random() + ">"

      # add newline or space
      end = "\n"
      if (j < COLUMNS - 1):
        end = " "
      bool_text += end
      int_text += end
      float_text += end
      string_text += end
      random_text += end

  BOOL_PATH = str(ROWS) + '_bool.txt'
  INT_PATH = str(ROWS) + '_int.txt'
  FLOAT_PATH = str(ROWS) + '_float.txt'
  STRING_PATH = str(ROWS) + '_string.txt'
  RANDOM_PATH = str(ROWS) + '_random.txt'

  bool_file = open(BOOL_PATH, 'w')
  int_file = open(INT_PATH, 'w')
  float_file = open(FLOAT_PATH, 'w')
  string_file = open(STRING_PATH, 'w')
  random_file = open(RANDOM_PATH, 'w')

  bool_file.write(bool_text)
  int_file.write(int_text)
  float_file.write(float_text)
  string_file.write(string_text)
  random_file.write(random_text)

main()