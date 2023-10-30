import pyshorteners

long_url = input ("Enter your url:")

def short_url(url):

    type_tiny = pyshorteners.Shortener()

    short_url = type_tiny.tinyurl.short(url)

    return short_url

shortened_url=short_url(long_url)


print("The Shortened URL is: "+shortened_url)

