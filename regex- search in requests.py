import re
#Check if users was trying to get access to php paths on your webservices, search in a text
request = "https://homepage/admin.php"
x = re.search("^http.*php$", request)

if x:
  print(f"YES! We have a match!, some one was trying to get access to\n{request}")
else:
  print("No match")