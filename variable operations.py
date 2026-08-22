# printing a simple message
name = input("Enter your name: ")
print(f"Hello {name}")

# making the name to print in upper and lower case
print(name.upper())
print(name.lower())

#Quote from a honourable person
print('A man asked Prophet Muhammad (PBUH) if he should leave his camel untied and trust in God or tie it first.\n The Prophet replied,"Tie it and put your trust in God"')

#Trying to remove prefix and suffix
google_url = "https://www.google.com"
google_link = google_url.removeprefix('https://')
print(f"Google link is {google_link}")
website = "google.com"
website_name = website.removesuffix('.com')
print(f"Website name is {website_name}")