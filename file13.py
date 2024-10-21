import os
entries = os.listdir('d://batches')
print(entries)
os.mkdir('new_directory')
os.makedirs('parent_dir/sub_dir')
os.remove('file_to_delete.txt')
os.rmdir('empty_directory')
os.rename('old_name.txt', 'new_name.txt')
os.replace('old_file.txt', 'new_file.txt') #will replace target if exists
if os.path.exists('file_or_directory'):
    print("Exists")
if os.path.isfile('file.txt'):
    print("It's a file")
if os.path.isdir('directory'):
    print("It's a directory")
file_path = os.path.join('folder', 'subfolder', 'file.txt')
file_info = os.stat('file.txt')
print(file_info.st_size)  # File size
exit_status = os.system('ls')  # Executes 'ls' on Linux/Mac or 'dir' on Windows
pid = os.getpid()
print(f"Current process ID: {pid}")
parent_pid = os.getppid()
print(f"Parent process ID: {parent_pid}")
os._exit(0)  # Exit with status 0 (success)
path = os.getenv('PATH')
print(path)
os.putenv('MY_ENV_VAR', 'some_value')
env_vars = os.environ  #returns dictionary
print(env_vars)
cwd = os.getcwd()
print(f"Current working directory: {cwd}")
os.chdir('/path/to/directory')
abs_path = os.path.abspath('file.txt')
print(abs_path)
filename = os.path.basename('/path/to/file.txt')
print(filename)  # Outputs 'file.txt'
directory = os.path.dirname('/path/to/file.txt')
print(directory)  # Outputs '/path/to'
head, tail = os.path.split('/path/to/file.txt')
print(f"Directory: {head}, File: {tail}")
drive, path = os.path.splitdrive('C:/path/to/file.txt')
print(f"Drive: {drive}, Path: {path}")
root, ext = os.path.splitext('file.txt')
print(f"Root: {root}, Extension: {ext}")
user = os.getlogin()
print(f"Logged in as: {user}")
















