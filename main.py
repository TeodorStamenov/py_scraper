from selenium import webdriver
from selenium.webdriver.common.by import By

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

mainPath = 'https://ethplorer.io/address/0xdbdb4d16eda451d0503b854cf79d55697f90c8df#chart=candlestick&transfers='

for page in range(1,3):
    url = mainPath + str(page)
    print("Page: " + url)
    driver.get(url)
    driver.refresh()
    table = driver.find_element_by_css_selector('div[id=address-token-transfers] table')
    for row in table.find_elements_by_css_selector('tr'):
        for cell in row.find_elements_by_tag_name('td.d-md-table-cell div.transfers-qty-value'):
            print(cell.text)
    print("\n\n\n")



# driver.get("https://etherscan.io/token/0xdbdb4d16eda451d0503b854cf79d55697f90c8df")

# chromedriver_autoinstaller.install()

# elements = driver.find_elements_by_css_selector('span.myFnExpandBox_searchVal')
# for element in elements:
    # x = element.find_elements_by_css_selector('td:nth-child(2) > span > a')
    # print(element.text)

# table = driver.find_element_by_xpath('//*[@id="maindiv"]/div[2]/table/tbody')

# table = driver.find_element_by_xpath('/html/body/div[2]/div[2]/table/tbody')
# print(table)


# table_id = driver.find_elements(By.CSS_SELECTOR, '.table.table-md-text-normal')
# print(table_id)

# rows = table_id.find_elements(By.TAG_NAME, "tr")  # get all of the rows in the table
# for row in rows:
#     # Get the columns (all the column 2)
#     col = row.find_elements(By.TAG_NAME, "td")[1]  # note: index start from 0, 1 is col 2
#     print(col.text)  # prints text from the element