from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import json

persons = []
total_person = 0
with open("users.json") as f: #change it back to users.json when ready
    credentials = json.load(f)

for info in credentials:
    persons.append({
        "dpid": info["dpid"],
        "username": info["username"],
        "password": info["password"],
        "crn": info["crn"],
        "transaction": info["transaction"]
    })
    total_person += 1

driver = webdriver.Chrome()
driver.get("https://meroshare.cdsc.com.np")
driver.fullscreen_window()

for num in range(total_person):
    driver.implicitly_wait(10)
    for_next_user = 0           # this is to break out of the loop to continue the share filling process for next users.
    no_luck = 1                 # this is for the case where no div is found with 'Ordinary Shares'.

    branch = driver.find_element(By.ID, 'selectBranch')
    branch.click()
    branchId = driver.find_element(By.CLASS_NAME, 'select2-search__field')
    branchId.click()
    branchId.send_keys(persons[num]["dpid"])
    branchId.send_keys(Keys.ENTER)

    user = driver.find_element(By.ID, 'username')
    user.send_keys(persons[num]["username"])

    passer = driver.find_element(By.ID, 'password')
    passer.send_keys(persons[num]["password"])

    time.sleep(2)
    passer.submit()

    driver.implicitly_wait(5)

    link = driver.find_element(By.LINK_TEXT, 'My ASBA')
    link.click()

    driver.implicitly_wait(5)


    reportSelector = driver.find_element(By.LINK_TEXT, 'Apply for Issue')
    reportSelector.click()
    time.sleep(3)
    main_divs = driver.find_elements(By.CSS_SELECTOR, '.company-list')

    target_text = 'Ordinary Shares'

    for main_div in main_divs:
        span_elements = main_div.find_elements(By.CSS_SELECTOR, ".isin")
        # print(span_elements)
        for i, span_element in enumerate(span_elements):
            current_text = span_element.text.strip()

            if target_text in current_text:
                print(f"Span element {i + 1}'s text matches the target text: {current_text}")

                try:
                    apply_btn = main_div.find_element(By.CSS_SELECTOR, "button.btn-issue")
                    time.sleep(1)
                    apply_btn.click()
                    bank = driver.find_element(By.XPATH, '//*[@id="selectBank"]')
                    time.sleep(1)
                    bank.click()
                    bank.send_keys(Keys.DOWN)
                    time.sleep(1)
                    bank.send_keys(Keys.ENTER)
                    account = driver.find_element(By.XPATH, '/html/body/app-dashboard/div/main/div/app-issue/div/wizard/div/wizard-step[1]/form/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div/select')
                    time.sleep(1)
                    account.click()
                    account.send_keys(Keys.DOWN)
                    time.sleep(1)
                    account.send_keys(Keys.ENTER)
                    applied = driver.find_element(By.ID, 'appliedKitta')
                    time.sleep(1)
                    applied.send_keys('10')
                    crn = driver.find_element(By.ID, 'crnNumber')
                    time.sleep(1)
                    crn.send_keys(persons[num]["crn"])
                    dis = driver.find_element(By.ID, 'disclaimer')
                    time.sleep(1)
                    dis.click()
                    link = driver.find_element(By.XPATH, '/html/body/app-dashboard/div/main/div/app-issue/div/wizard/div/wizard-step[1]/form/div[2]/div/div[5]/div[2]/div/button[1]').click()
                    time.sleep(10)
                    trans = driver.find_element(By.ID, 'transactionPIN')
                    trans.send_keys(persons[num]["transaction"])
                    final = driver.find_element(By.XPATH, '/html/body/app-dashboard/div/main/div/app-issue/div/wizard/div/wizard-step[2]/div[2]/div/form/div[2]/div/div/div/button[1]').click()
                    time.sleep(10)
                except Exception as e:
                    print("Could not find Apply button:", e)
                    # If couldn't find the Apply button, it could be because the user has already applied
                    # so breaking could be the correct option rather than qutting the driver?
                    # driver.quit()
                for_next_user = 1
                break
            else:
                print(f"Span element {i+1}'s text doesn't match the text.")
        if for_next_user == 1:
            no_luck = 0
            break

    # after looking into all the divs i.e. the company list, if still no match found then we have to quit the driver instead of going for next participant
    if no_luck == 1:
        # this is the case where we've looked into all the possible span elements but no match was found so we don't need to look for next user.
        exit_route = driver.find_element(By.XPATH, '/html/body/app-dashboard/header/div[2]/div/div/div/ul/li[1]')
        exit_route.click()
        print('No Ordinary Shares found at the moment.')
        driver.quit()
    else:
        print(f"Share filled for {i+1} person")
        exit_route = driver.find_element(By.XPATH, '/html/body/app-dashboard/header/div[2]/div/div/div/ul/li[1]')
        exit_route.click()
print('IPO has been filled for all users!')
driver.quit()
