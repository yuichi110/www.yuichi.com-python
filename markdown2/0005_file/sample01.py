import os

def list_file(path, indent_level):
  # show directory name
  print('{}[{}]'.format(' ' * indent_level, path))

  for file_name in os.listdir(path):
    if file_name.startswith('.'):
      continue
    abs_filepath = path + '/' + file_name
    if os.path.isdir(abs_filepath):
      list_file(abs_filepath, indent_level + 1)
    else:
      print('{}- {}'.format(' ' * indent_level, file_name))

list_file('/python', 0)
