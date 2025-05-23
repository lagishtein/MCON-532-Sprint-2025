import openai
import os
import pprint
from src.open_api_client import get_openai_client

def generate_response(prompt):
    client = get_openai_client()
    """Helper function to send prompt to OpenAI API and return response."""
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.5,
            max_tokens=500
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error calling OpenAI API: {e}")
        return None

# Step 1: Generate Basic Dictionary
prompt_1 = """
Create a Python dictionary where each student ID maps to another dictionary containing:
- "name": Student’s name (string)
- "grades": A list of grades (integers)
- "gpa": The GPA, calculated as (sum of grades / number of grades) / 25, rounded to two decimal places.
"""
basic_dict_code = generate_response(prompt_1)

# Step 2: Convert to Dictionary Comprehension
prompt_2 = f"""
Modify the following Python dictionary to use dictionary comprehension:
{basic_dict_code}
"""
dict_comprehension_code = generate_response(prompt_2)

# Step 3: Format Output for Readability using pprint
prompt_3 = f"""
Modify the following Python code to print the student data in a well-formatted structured output using pprint:
{dict_comprehension_code}
"""
formatted_output_code = generate_response(prompt_3)

# Step 4: Generate Unit Tests
prompt_4 = f"""
Write unit tests using unittest for the following Python dictionary.
The tests should check:
- The dictionary contains the correct number of students.
- Each student has a "name", "grades", and "gpa".
- The "grades" list contains only integers.
- The GPA is correctly calculated.
{dict_comprehension_code}
"""
unit_test_code = generate_response(prompt_4)

# Save generated code to files
if basic_dict_code and dict_comprehension_code and formatted_output_code and unit_test_code:
    with open("generated_students.py", "w") as f:
        f.write(dict_comprehension_code + "\n\n" + formatted_output_code)

    with open("test_students.py", "w") as f:
        f.write(unit_test_code)

    # Display results using pprint
    print("\n=== Step 1: Basic Dictionary ===")
    pprint.pprint(basic_dict_code)

    print("\n=== Step 2: Dictionary Comprehension ===")
    pprint.pprint(dict_comprehension_code)

    print("\n=== Step 3: Formatted Output (using pprint) ===")
    pprint.pprint(formatted_output_code)

    print("\n=== Step 4: Generated Unit Tests ===")
    pprint.pprint(unit_test_code)

    print("\nGenerated code has been saved to `generated_students.py` and `test_students.py`.")

else:
    print("\nFailed to generate all required outputs. Check API calls and try again.")
