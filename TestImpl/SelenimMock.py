from Utils.Consts import By
def get(selenium_driver, website):
    return selenium_driver.get(website)


def MArgentinaTest(selenium_driver, data):
    get(selenium_driver, data[0]["website"])
    print(selenium_driver.title)
    for key,value in data[0].items():
        if key != "website":
            selenium_driver.find_element(By.ID, key).send_keys(value)
    selenium_driver.close()

