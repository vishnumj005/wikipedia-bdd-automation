from behave import step

from pages.search_pages import SearchPage


@step("attempt search with {keyword}")
def step_impl(context, keyword):
    context.keyword = keyword
    SearchPage(context).search_with_keyword(keyword)


@step("verify the search result is shown")
def step_impl(context):
    SearchPage(context).verify_search_result()


@step("click on search result")
def step_impl(context):
    SearchPage(context).click_search_result()


@step("verify wikipedia page is open")
def step_impl(context):
    SearchPage(context).verify_wikipedia_page()
