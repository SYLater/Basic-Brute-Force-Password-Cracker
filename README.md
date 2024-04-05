# Basic Brute-Force Password Cracker

This Python script uses Selenium to automate the process of guessing a password for a web application. It employs a multi-threaded approach to speed up the password guessing process by creating multiple threads, each with its own iterator.

## Features

- Brute-force password guessing using a combination of lowercase letters and numbers
- Multi-threaded implementation to improve the speed of the guessing process
- Automatically detects when the correct password is found and prints the elapsed time

## Prerequisites

- Python 3.x
- Selenium library (`pip install selenium`)
- Chrome WebDriver (Follow installation instructions [here](https://selenium-python.readthedocs.io/installation.html))

## Usage

1. Download the Chrome WebDriver and ensure it's in your system's `PATH` environment variable.
2. Save the Python script to a file (e.g., `password_cracker.py`).
3. Run the script using the following command:

   ```
   python password_cracker.py
   ```

   The script will start guessing the password and will print the correct password and the elapsed time when it's found.

## How it Works

1. The script creates a Selenium WebDriver instance and navigates to the target website.
2. It then creates 6 threads, each with its own iterator to generate password combinations.
3. Each thread calls the `guess_password` function, which sends the username and password combinations to the input fields and clicks the submit button.
4. The script checks the response from the website to see if the correct password has been found. If so, it prints the password and the elapsed time, and then exits.
5. If the correct password is not found, the script continues to generate new password combinations until the correct one is found.

## License

This project is licensed under the [MIT License](LICENSE).