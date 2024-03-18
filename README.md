# Python Hash Cracker

## Description

This repository documents my journey in practicing cybersecurity concepts through the development of a Python hash cracking tool. The project is adopted from a [YouTube tutorial](https://www.youtube.com/watch?v=eHugvb5NeI4). My aim is to use this project to apply the knowledge acquired from various cybersecurity material.
The project makes use of a wordlist-based approach to attempt to crack hashed passwords for various hash algorithms, including MD5, SHA1, SHA224, SHA512, SHA256, and SHA384.

<h2>Languages and Utilities Used</h2>

- Made using Python

<h2>Environments Used </h2>

- <b>VSCode Codespaces</b>

---

### How It Works

The Python hash cracking tool utilizes a wordlist-based approach to attempt to crack hashed passwords (program currently only tested this with simple 1 word passwords). Here's how it works:

1. **Hash Algorithm Selection**: The user selects the hash algorithm corresponding to the hashed password they want to crack. Supported algorithms include MD5, SHA1, SHA224, SHA512, SHA256, and SHA384.

2. **Wordlist Input**: The user provides the location of a wordlist file containing potential passwords. The tool iterates through each word in the wordlist to generate hash values using the selected hash algorithm.

3. **Hash Comparison**: The generated hash values are compared against the target hashed password provided by the user. If a match is found, the corresponding plaintext password from the wordlist is identified as the cracked password.

4. **Output**: If a match is found, the tool displays the cracked password to the user. Otherwise, it indicates that the hashed password was not found in the wordlist.

---

## Steps Taken
1. Choose Hash Type and Wordlist
- Select Hash Type: Choose the desired hash type from the available options, including MD5, SHA1, SHA224, SHA512, SHA256, or SHA384.
- Provide Wordlist: Specify the location of the wordlist containing potential passwords to be tested against the hashed value.
2. Run the Script
- Execute the Python script and follow the on-screen prompts to initiate the hash cracking process.
  
---

## Example

```bash
$ python hash_crack.py
 _   _           _        ____                _             
| | | | __ _ ___| |__    / ___|_ __ __ _  ___| | _____ _ __ 
| |_| |/ _` / __| '_ \  | |   | '__/ _` |/ __| |/ / _ \ '__|
|  _  | (_| \__ \ | | | | |___| | | (_| | (__|   <  __/ |   
|_| |_|\__,_|___/_| |_|  \____|_|  \__,_|\___|_|\_\___|_|   
                                                            

Algorithms available: MD5 | SHA1 | SHA224 | SHA512 | SHA256 | SHA384
What is your chosen hash type?: md5
Enter wordlist location: wordlist.txt
Enter Hash: 5f4dcc3b5aa765d61d8327deb882cf99
[1;32mHash found:[0m password123
```

---

## Potential Misuse by Threat Actors

While this hash cracking tool is intended for educational purposes and ethical use, It could still be crucial to get in the mind of a threat actor, and learn how a they could potentially use/misuse similar tools for malicious purposes. Here are some scenarios:

- **Password Cracking**: A threat actor may utilize the wordlist-based approach supported by this script to crack hashed passwords obtained from compromised systems or data breaches. By selecting one of the supported hash algorithms and providing a wordlist containing common passwords or previously compromised passwords, they can systematically attempt to crack hashed passwords for unauthorized access.

- **Brute Force Attacks**: In addition to using wordlists, threat actors may leverage brute force attacks by using a similar script alongside this to systematically generate and test all possible password combinations after the hashes are cracked. While brute-forcing is more resource-intensive, it can be effective against weak or poorly configured password policies.

- **Credential Stuffing**: Once a threat actor has obtained a list of cracked passwords using this tool, they can automate login attempts across various online services through credential stuffing. By using the cracked passwords, along with other credentials to authenticate against multiple platforms, threat actors can gain unauthorized access to user accounts, potentially leading to further data breaches or account takeovers.

## Mitigating the Risk

To mitigate the risk of misuse and unauthorized access, it's crucial to implement strong password policies and security measures, including:

- **Complex Password Requirements**: Enforce password complexity requirements to ensure that users choose strong and unique passwords that are less susceptible to cracking attempts.

- **Multi-Factor Authentication (MFA)**: Implement multi-factor authentication (MFA) to add an extra layer of security beyond passwords. This can significantly reduce the risk of unauthorized access, even if passwords are compromised.

- **Regular Password Changes**: Encourage users to regularly change their passwords to minimize the impact of successful cracking attempts and enhance overall cybersecurity resilience. Can be quite bothersome if done manually, so some form of automated configuration is recommended.

By proactively addressing these security measures, organizations and/or individuals can reduce the likelihood of falling victim to password cracking attacks and protect against unauthorized access to potentially sensitive information.

---

# Disclaimer

- **Educational Purpose**: The primary objective of this project is to deepen my understanding of cybersecurity concepts, in this case its particularly in the area of password hashing and cracking techniques.
  
- **Hands-on Practice**:  I aim to gain practical experience in cybersecurity via implementing this hash cracking tool in Python, reinforcing theoretical knowledge with the added practical application.

- **Ethical Considerations**: It's important to note that this tool is intended for educational purposes only. I do not endorse or encourage unauthorized access or malicious activities.
