from Utils.Consts import By
def get(selenium_driver, website):
    return selenium_driver.get(website)


def ArgentinaTest(selenium_driver, data):
    get(selenium_driver, data[0]["website"])
    for key,value in data[0].items():
        if key == "Number of Employees ":
            selenium_driver.find_element(By.ID, key).send_keys(value[3])
        elif key == "website":
            pass
        else:
            selenium_driver.find_element(By.ID, key).send_keys(value[1])
    selenium_driver.close()

