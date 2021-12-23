from selenium import webdriver
import pandas as pd

driver = webdriver.Chrome('chromedriver.exe')
# driver = webdriver.Chrome()
driver.get('https://en.wikipedia.org/wiki/List_of_largest_companies_by_revenue')
driver.maximize_window()

countries_names = driver.find_elements_by_xpath('//tbody/tr/td[1]/a')
industry = driver.find_elements_by_xpath('//tbody/tr/td[2]')
revenue = driver.find_elements_by_xpath('//tbody/tr/td[3]')
profit = driver.find_elements_by_xpath('//tbody/tr/td[4]')
employees = driver.find_elements_by_xpath('//tbody/tr/td[5]')
headquators = driver.find_elements_by_xpath('//tbody/tr/td[6]')

largest_company_result = []

for i in range(len(employees)):
    temporary_data = {'Country': countries_names[i].text,
                      'Industry': industry[i].text,
                      'Revenue': revenue[i].text,
                      'Profit': profit[i].text,
                      'Employees': employees[i].text,
                      'Headquarters': headquators[i].text}
    largest_company_result.append(temporary_data)

df_data = pd.DataFrame(largest_company_result)
# df_data

df_data.to_csv('largest_company_result.csv', index=False)

driver.close()
