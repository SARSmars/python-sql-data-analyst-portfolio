# Example text messages with different phone number formats for regex practice
import re
text1 = "Call me at 987-654-3210 when you arrive."
text2 = "My office number is (012) 345 6789, feel free to reach out."
text3 = "Emergency? Dial +91 9988776655 immediately!"

# You can use these strings to practice extracting phone numbers using the regex module.

pattern = '\d{10}'  
# Example regex pattern to match 10-digit phone numbers
# Note: The regex pattern can be modified to match different formats as needed.

result = re.findall(pattern, text1)
print("Found phone numbers in text1:", result)
result = re.findall(pattern, text2)
print("Found phone numbers in text2:", result)
result = re.findall(pattern, text3)
print("Found phone numbers in text3:", result) 

pattern = '\d{3}-\d{3}-\d{4} | \d{10} | \(\d{3}\) \d{3} \d{4}'

matches = re.findall(pattern, text1)
print("Matches in text1:", matches)
matches = re.findall(pattern, text2)
print("Matches in text2:", matches)
matches = re.findall(pattern, text3)
print("Matches in text3:", matches)
# The regex pattern can be adjusted to match different phone number formats.


# Example text messages with different email ID formats for regex practice
email_text1 = "john.doe@example.com ."
email_text2 = "support_team123@mycompany.in ."
email_text3 = "username+test@sub.org"

pattern = '[a-z0-9A-Z._+]*@[a-z]*\.[a-z]*'

matches = re.findall(pattern, email_text1)
print("Matches in email_text1:", matches)
matches = re.findall(pattern, email_text2)
print("Matches in email_text2:", matches)
matches = re.findall(pattern, email_text3)
print("Matches in email_text3:", matches)

# Example text message with differnet order number for Regex Practice

order_text1 = "Your order number is order-20240. Please keep it for reference."
order_text2 = "order# 987654321 has been shipped."
order_text3 = "Thank you for shopping! order: 55992025"
pattern = 'order[^\d]*(\d*)'

matches = re.findall(pattern, order_text1)
print("Matches in text1:", matches)
matches = re.findall(pattern, order_text2)
print("Matches in text2:", matches)
matches = re.findall(pattern, order_text3)
print("Matches in text3:", matches)