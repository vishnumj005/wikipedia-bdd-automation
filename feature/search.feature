@feature_wiki_search
Feature: Validating the search feature

  @sc_search
  Scenario Outline: Attempt search with a valid keyword
    Given user navigate to wikipedia search page
    When attempt search with <keyword>
    Then verify the search result is shown
    Examples:
    |keyword |
    |dog     |

  @sc_search
  Scenario Outline: Validate wikipedia page for search results
    Given user navigate to wikipedia search page
    When attempt search with <keyword>
    Then verify the search result is shown
    And click on search result
    And verify wikipedia page is open
    Examples:
    |keyword |
    |dog     |
