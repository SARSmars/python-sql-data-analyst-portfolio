from bs4 import BeautifulSoup

# Test BeautifulSoup
html_doc = "<html><head><title>Test</title></head><body><p>Hello, World!</p></body></html>"
soup = BeautifulSoup(html_doc, 'html.parser')

# Print the title to test
print(soup.title.string)