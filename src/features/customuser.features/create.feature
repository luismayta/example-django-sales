@customuser.create
Feature: Proccess of user

  @customuser.register.user
  Scenario: A user register
    When make "user" with:
      | id | email             | first_name | last_name |
      | 10 | miemail@gmail.com | Diana      | Rojas     |
    Then "post" the "user" to the resource "register":
    And the response of "user" must be:
      | status_code |
      |         200 |