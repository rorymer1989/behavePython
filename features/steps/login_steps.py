from behave import given, when, then

@given("the user is on the search page")
def user_on_search_page(context):
    context.web.open()

@when('the user selects a departure city "{city}"')
def user_select_departure_city(context, city):
    context.web.select_option_city_departure(city)

@when('the user selects a destination city "{city}"')
def user_select_destination_city(context, city):
    context.web.select_option_city_destination(city)

@when("clicks on the Find Flights button")
def user_clicks_on_find_flights(context):
    context.web.click_button_find_flights()

@then("flights are presented on the search result page")
def flights_are_found(context):
    elements = context.web.valid_table_flights_from()
    assert len(elements) > 1