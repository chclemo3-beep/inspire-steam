# Clement Ngotho
# 2/11/2026
# String formatting

# Get string length
sentence = "I watch anime"

string_length = len(sentence)

print(f"The length is: {string_length}")

#Splitting = string
sentence_2 = "Mathematics Physics"
split = sentence_2.split(" ")

print(f"the first subject is:", split[0])

# Make everything CAPS
code = "uvbfw840srkf"

capitalized = code.upper()

print("New mpesa code:" ,capitalized)

# Replacing characters in a string

balance = "100kes"
amount_added = "50kes"

cleaned_balance = balance.replace("kes","")
print("Cleaned balance: ",cleaned_balance)

cleaned_amount_added = amount_added.replace("kes","")
print("Amount added: ",cleaned_amount_added)

new_balance = int(cleaned_balance) + int(cleaned_amount_added)
print("The new balance is: ",new_balance)

message = "CONFIRMED, you have received 40kes from Philip"
split_message = message.split(" ")

print(f"Money received: {split_message[4]}")