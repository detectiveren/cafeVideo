import secrets

# This is used to generate a secret key to put in the environment variables of the OS

generateSecretKey = secrets.token_hex(32)
print(f"Here's your generated secret key: {generateSecretKey}")
print("Place this in your environment variables. It should look like this (Windows Example)")
print("Variable Name: SECRET_CAFE_KEY")
print(f"Variable Value: {generateSecretKey}\n\n")
print("Commands for setting the environment variable Windows/Linux/macOS\n")
print(" Windows ")
print("---------")
print("Temporary Environment Variable Commands (you can choose either CMD or Powershell)")
print(f"CMD: set SECRET_CAFE_KEY={generateSecretKey}")
print(f"PowerShell: $env:SECRET_CAFE_KEY={generateSecretKey}")
print("Permanent Environment Variable Commands")
print(f"Powershell (for user): [System.Environment]::SetEnvironmentVariable(\"SECRET_CAFE_KEY\", \"{generateSecretKey}\", \"User\")")
print(f"Powershell (for everyone): [System.Environment]::SetEnvironmentVariable(\"SECRET_CAFE_KEY\", \"{generateSecretKey}\", \"Machine\")\n")
print(" Linux ")
print("-------")
print("Temporary Environment Variable Command")
print(f"export SECRET_CAFE_KEY={generateSecretKey}")
print("Permanent Environment Variable Command")
print(f"echo 'export SECRET_CAFE_KEY={generateSecretKey}' >> ~/.bashrc")
print("source ~/.bashrc\n")
print(" macOS ")
print("-------")
print("Temporary Environment Variable Command")
print(f"export SECRET_CAFE_KEY={generateSecretKey}")
print("Permanent Environment Variable Command")
print(f"echo 'export SECRET_CAFE_KEY={generateSecretKey}' >> ~/.zshrc")
print("source ~/.zshrc\n")


