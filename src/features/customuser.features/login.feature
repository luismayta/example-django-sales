@customuser
Feature: Proccess of user

  @customuser.login.user
  Scenario: A user register
    When make "user" with:
      | id | email             | first_name | last_name | password |
      | 10 | miemail@gmail.com | Diana      | Rojas     |   123456 |
    Then "post" the "user" to the resource "users":
    And the response of "user" must be:
      | status_code |
      |         201 |
    Given Login with "miemail@gmail.com" and "123456"
