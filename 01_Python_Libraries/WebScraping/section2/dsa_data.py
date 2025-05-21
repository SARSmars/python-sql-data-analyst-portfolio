from selenium import webdriver
from bs4 import BeautifulSoup
import time
from fpdf import FPDF


driver = webdriver.Chrome()  # or webdriver.Firefox()
driver.get('https://takeuforward.org/strivers-a2z-dsa-course/strivers-a2z-dsa-course-sheet-2/')

# Wait for content to load
time.sleep(3)

# Get page source after JS execution
soup = BeautifulSoup(driver.page_source, 'html.parser')
driver.quit()

accordion_items = soup.find_all('div', class_='accordion-item')

# Extract text from each accordion item
accordion_texts = []
for idx, item in enumerate(accordion_items, 1):
    text = item.get_text(separator='\n', strip=True)
    accordion_texts.append(f"Accordion Item {idx}:\n{text}\n\n")

# Save to PDF
pdf = FPDF()
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.set_font("Arial", size=12)

for text in accordion_texts:
    pdf.multi_cell(0, 10, text)

pdf.output("accordion_items.pdf")
print("Accordion items have been saved to accordion_items.pdf")