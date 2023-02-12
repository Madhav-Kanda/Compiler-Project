import subprocess 
import os

# Run a test file and return the result (accepted or rejected)
def run_test(test_file):
    try:
        result = subprocess.run(["python3", "dragon.py", test_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return "accepted" 
    except subprocess.CalledProcessError as error:
        return "rejected"

# List of test files in the test folder
test_folder = "tests_folder"
tests = [f"{test_folder}/{file}" for file in os.listdir(test_folder) if file.endswith(".txt")]

# Open a file to store the results
with open("automated_test_results.txt", "w") as results_file:
    # Run each test and store the results in the file
    for i, test in enumerate(tests):
        result = run_test(test)
        results_file.write(f"{test} - {result}\n")



# if you want errors for the rejected test cases in the output run the following code instead of the above code

# import os
# import subprocess

# test_folder = "tests_folder"
# tests = [f"{test_folder}/{file}" for file in os.listdir(test_folder) if file.endswith(".txt")]

# with open("automated_test_results.txt", "w") as results_file:
#     for test in tests:
#         try:
#             subprocess.check_output(["python3", "dragon.py", test], stderr=subprocess.STDOUT)
#             results_file.write(f"{test} - accepted\n")
#             results_file.write("\n###########################################################\n\n")
#         except subprocess.CalledProcessError as e:
#             results_file.write(f"{test} - rejected\n\n")
#             results_file.write("ERROR:\n\n")
#             results_file.write(f"{e.output.decode()}\n")
#             results_file.write("\n###########################################################\n\n")
