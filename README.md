# Wikipedia Automation
* https://en.wikipedia.org/w/index.php?search

## Scenarios Automated:
1. Search a keyword in wiki
2. User is able to click and view the search result

* Search functionality has chosen for automating wikipedia. Because Search is critical functionality and most commonly used by user.
  And this functionality shouldn't fail in any case

## Implementation
  * Language used: Python (3.10)
  * Frameworks used: Selenium, behave, Cucumber
  * Page Object Method (POM), is used to implement the framework, all the
functionalities which lie inside that page becomes methods of the corresponding
class.
  * All the feature files contains in feature folder and all the steps and pages objects are resides in steps and pages
    folders respectively.
  * base_page.py contains all the reusable libraries like click, send_keys, wait etc

# Links

* [Github link to clone project](https://github.com/vishnumj005/wikipedia-bdd-automation.git)
* please note: the currently used version for python is 3.10.
* Install requirements before executing the scripts
  file before running the script.

# How to run test?

1. Via Terminal

    * Run `behave --tags=@{specific_tag}`
    * Run `behave --tags={tag1,tag2}`
    * Run `behave <path to feature file>`

2. Via PyCharm
    * Run directly from the feature file

3. Run Script with allure reporting
   * Run `behave -f allure_behave.formatter:AllureFormatter -o <path to result>`
   * Then Run `allure serve`

4. Run Script through Jenkins
   1. Create new pipeline
   2. Choose pipeline script from SCM
   3. Select github project and add URL
   4. Change branch specifier to */main
   5. Give jenkins file (jenkins/jenkins_file) in script path 
   6. Save the configuration
   7. Run the script
   * note: uncomment line number 7 from jenkins_file to run in Linux/mac machine
   
# Folder Structure

	.
	├── Root
	│     ├── steps                                 # Step definitions
	│     │     ├── search_steps.py
	│     │     ├── url_navigation_steps.py                           
	│     ├── feature
	│     │     ├── search.feature    # Test scenarios
	│     ├── config                             # Configurations
	│     │     ├── browser
	│     │     │     └──driverfactory.py
	│     │     ├── constants
	│     │     │     └──constants.py
	│     │     ├── base_config.py
	│     ├── pages                             # Pages
	│     │     ├── base
	│     │     │     └──base_page.py
	│     │     ├── search_pages.py
	│     │     ├── url_navigation_page.py
	│     │     └── schema.py
    │     ├── environment.py                    # Environments
    │     ├── requriements.txt                            # Required libraries
    │     ├── jenkins                                     #Jenkin related files
                 ├── jenkins_file
