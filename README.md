# seleniumpython_Swaglabs

Selenium Python framework
(Python, Selenium, Pytest, PageObject Model, HTML Reports)

1. Create new Project and install Required Packages/plugins

* Selenium: Selenium Libraries
* Pytest: Python UnitTest framework
* pytest-html: Pytest HTML Reports
* pytest-xdist: Run Test Parallel
* Openpyxl: MS Excel Support
* Allure-pytest: to generate allure reports

2. Create Folder Structure

 Project Name
 pageObjects(Package)
 testCases(Package)
 utilities(Package)
 Configurations(Folder)
 Logs(Folder)
 Screenshots(Folder)
 Reports(Folder)
 Run.bat

3. Automating Login Test Cases

i.    Create LOginPage Object Class under "pageObjects"
ii.   Create LoginTest under "testCases"
iii.  Create confitest.py under "testCases"

4. Capture Screenshots on failures

i. Update Login test with Screenshot under "testCases"


5. Read Common values from ini file

i.   Add "config.ini" file in "Configurations" folder
ii.  Create "readProperties.py" utility file under utilities package
     to read common data
iii. Replace hard coded values in login test case


6. Adding Logs to test case

i.  Add custonLogger.py under utilities package
ii. Add logs to Login test case


7. Run Tests on Desired Browser/Cross Browser/Parallel

i.  update conftest.py with required Fixtures which will accept
    command line argument(browser)
ii. Pass browser name as argument in command line


Run Pytest
 
 pytest -v -s testCases/test_login.py
 
 pytest -v -s testCases/test_login.py --browser chrome
 
 pytest -v -s --html=Reports\report.html testCases/test_login.py --browser chrome
 

