import os
# with open("binary_file.bin", "wb") as file:  # Open for writing in binary mode
#     file.write(b"Binary content")  # Data must be a bytes object


user = os.getlogin()
print(f"Logged in as: {user}")