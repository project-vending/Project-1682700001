 
import os

# Define the directory
directory = "Rest_API_Development_with_FastAPI"

# Define subdirectories
sub_directories = ["app", "data", "tests"]

# Create the main directory if it does not exist
if not os.path.exists(directory):
    os.mkdir(directory)

# Create subdirectories if they do not exist
for sub_directory in sub_directories:
    sub_directory_path = os.path.join(directory, sub_directory)
    if not os.path.exists(sub_directory_path):
        os.mkdir(sub_directory_path)

# Create empty files in the subdirectories
app_files = ["main.py"]
data_files = ["database.py"]
tests_files = ["test_main.py"]

for file in app_files:
    file_path = os.path.join(directory, "app", file)
    open(file_path, "w").close()

for file in data_files:
    file_path = os.path.join(directory, "data", file)
    open(file_path, "w").close()

for file in tests_files:
    file_path = os.path.join(directory, "tests", file)
    open(file_path, "w").close()

print("File structure created successfully.")
