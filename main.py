from sel_functions import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import sys
import canva
##
import time

def main(driver):
    cookie = ClassWait(driver, By.XPATH, "/html/body/header/div[1]/div/div/form/button", 10)
    cookie.WaitConditionsButtons()

    tbody_XPATH = "/html/body/main/section[2]/div/div[2]/div[1]/table/tbody"
    tbody = driver.find_element("xpath", tbody_XPATH)

    for i_tr in range(1, len(tbody.find_elements(By.XPATH , "./*"))+1):
        tr_XPATH = tbody_XPATH+"/tr["+str(i_tr)+"]"
        tr = driver.find_element(By.XPATH, tr_XPATH)
        print("@@@@@@@@@@@@@@@@@@")
        for i_td in range(1, len(tr.find_elements(By.XPATH , "./*"))+1):
            td_XPATH = tr_XPATH+"/td["+str(i_td)+"]"
            td = driver.find_element(By.XPATH, td_XPATH)
            print(td.text)

    '''
    element = driver.find_element("xpath", "/html/body/main/section[2]/div/div[2]/div[1]/table/tbody/tr[4]")
    print(element)
    text = driver.find_element("xpath", "/html/body/main/section[2]/div/div[2]/div[1]/table/tbody/tr[4]/td[4]")
    print(text.text)
    '''

    while True:
        pass

    #destination = ClassWait(driver, By.CLASS_NAME, "BpkInput_bpk-input__ZDdkM SingleDestControls_fsc-large-above-tablet__Mjg0Y SingleDestControls_fsc-docked-middle-above-tablet__MmIwM SingleDestControls_fsc-docked-last-on-tablet__MDI0N LocationSelector_fsc-location-input__NDRiO", 5)
    #destination.WaitConditionsInputBox()



if __name__ == "__main__":
    driver_name = 'chromedriver.exe'
    driver_path = r"C:\Users\simon\OneDrive\Desktop\Python\PythonDriver"
    driver = canva.screen(driver_name, driver_path)
    main(driver)
