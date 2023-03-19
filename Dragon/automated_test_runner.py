import subprocess
import os

# Location of the tests_folder and dragon.py
tests_folder = "tests_folder"
dragon_script = "dragon.py"

# Get a list of all the test cases
test_cases = [f for f in os.listdir(tests_folder) if f.endswith(".txt")]

# Store the results in a list
results = []

# Loop through each test case
for test in test_cases:
    test_name = test.split(".")[0]
    output_file = "outputs_folder/output" + test_name[4:] + ".txt"

    # Run the dragon.py script with the current test case
    try:
        output = subprocess.check_output(["python", dragon_script, tests_folder + "/" + test], universal_newlines=True)

        # Read the contents of the expected output file
        with open(output_file, "r") as f:
            expected_output = f.read()

        print("outputs:")
        print(output)
        print(expected_output)

        # Compare the actual output to the expected output
        if output.strip() == expected_output.strip():
            results.append(test_name + ": accepted")
        else:
            results.append(test_name + ": rejected")
    except subprocess.CalledProcessError as e:
        results.append(test_name + ": rejected")

# Write the results to a file
with open("automated_tests_results.txt", "w") as f:
    f.write("\n".join(results))
