from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = webdriver.Edge(EdgeChromiumDriverManager().install())

driver.maximize_window()
driver.get("https://www.crunchbase.com")
wait = WebDriverWait(driver, 25)
#Advanced dropdown
wait.until(EC.element_to_be_clickable(
    (By.XPATH, '/html/body/chrome/div/app-header/div[1]/div[2]/nav-menu/button/span[1]/nav-action-item-header-layout/div/span'))).click()
#Select Company
wait.until(EC.element_to_be_clickable(
    (By.XPATH,'//*[@id="mat-menu-panel-0"]/div/div/mat-nav-list/nav-groups/nav-action-item[1]/nav-menu-action-item/a/nav-action-item-layout/span'))).click()
#search Bangkok
wait.until(EC.element_to_be_clickable(
    (By.XPATH,'//*[@id="mat-input-32"]'))).send_keys('Bangkok')
wait.until(EC.element_to_be_clickable(
    (By.XPATH,'//*[@id="mat-option-175"]/span/div/div[2]/span[1]'))).click()

#first company select
# wait.until(EC.element_to_be_clickable(
#     (By.XPATH,'/html/body/chrome/div/mat-sidenav-container/mat-sidenav-content/div/discover/page-layout/div/div/div[2]/section[2]/results/div/div/div[3]/sheet-grid/div/div/grid-body/div/grid-row[1]/grid-cell[2]/div/field-formatter/identifier-formatter/a/div/div'))).click()
# Company_Name=wait.until(EC.element_to_be_clickable(
#     (By.XPATH,'/html/body/chrome/div/mat-sidenav-container/mat-sidenav-content/div/ng-component/entity-v2/page-layout/div/div/profile-header/div/header/div/div/div/div[2]/div[1]/h1'))).text()
# Company_Website=wait.until(EC.element_to_be_clickable(
#     (By.XPATH,'/html/body/chrome/div/mat-sidenav-container/mat-sidenav-content/div/ng-component/entity-v2/page-layout/div/div/div/page-centered-layout[2]/div/row-card/div/div[1]/profile-section/section-card/mat-card/div[2]/div/fields-card/ul/li[5]/label-with-icon/span/field-formatter/link-formatter/a'))).text()
# Founder_Name=wait.until(EC.element_to_be_clickable(
#     (By.XPATH,'/html/body/chrome/div/mat-sidenav-container/mat-sidenav-content/div/ng-component/entity-v2/page-layout/div/div/div/page-centered-layout[3]/div/div/div[1]/row-card[2]/profile-section/section-card/mat-card/div[2]/div/fields-card[1]/ul/li[4]/field-formatter/identifier-multi-formatter/span/a'))).text()
# Email_id=wait.until(EC.element_to_be_clickable(
#     (By.XPATH,'/html/body/chrome/div/mat-sidenav-container/mat-sidenav-content/div/ng-component/entity-v2/page-layout/div/div/div/page-centered-layout[3]/div/div/div[1]/row-card[2]/profile-section/section-card/mat-card/div[2]/div/fields-card[3]/ul/li[1]/field-formatter/blob-formatter/span'))).text()



#loop
Company_Name_List=[]
Company_Website_List=[]
Founder_Name_List=[]
Email_id_List=[]
for i in range(1,6):
    wait.until(EC.element_to_be_clickable(
        (By.XPATH,'/html/body/chrome/div/mat-sidenav-container/mat-sidenav-content/div/discover/page-layout/div/div/div[2]/section[2]/results/div/div/div[3]/sheet-grid/div/div/grid-body/div/grid-row['+str(i)+']/grid-cell[2]/div/field-formatter/identifier-formatter/a/div/div'))).click()
    Company_Name=wait.until(EC.element_to_be_clickable(
        (By.XPATH,'/html/body/chrome/div/mat-sidenav-container/mat-sidenav-content/div/ng-component/entity-v2/page-layout/div/div/profile-header/div/header/div/div/div/div[2]/div[1]/h1'))).text()
    Company_Name_List.append(Company_Name)
    Company_Website=wait.until(EC.element_to_be_clickable(
        (By.XPATH,'/html/body/chrome/div/mat-sidenav-container/mat-sidenav-content/div/ng-component/entity-v2/page-layout/div/div/div/page-centered-layout[2]/div/row-card/div/div[1]/profile-section/section-card/mat-card/div[2]/div/fields-card/ul/li[5]/label-with-icon/span/field-formatter/link-formatter/a'))).text()
    Company_Website_List.append(Company_Website)
    Founder_Name=wait.until(EC.element_to_be_clickable(
        (By.XPATH,'/html/body/chrome/div/mat-sidenav-container/mat-sidenav-content/div/ng-component/entity-v2/page-layout/div/div/div/page-centered-layout[3]/div/div/div[1]/row-card[2]/profile-section/section-card/mat-card/div[2]/div/fields-card[1]/ul/li[4]/field-formatter/identifier-multi-formatter/span/a'))).text()
    Founder_Name_List.append(Founder_Name)
    Email_id=wait.until(EC.element_to_be_clickable(
        (By.XPATH,'/html/body/chrome/div/mat-sidenav-container/mat-sidenav-content/div/ng-component/entity-v2/page-layout/div/div/div/page-centered-layout[3]/div/div/div[1]/row-card[2]/profile-section/section-card/mat-card/div[2]/div/fields-card[3]/ul/li[1]/field-formatter/blob-formatter/span'))).text()
    Email_id_List.append(Email_id)
    driver.back()

print(Company_Name_List)
time.sleep(300)