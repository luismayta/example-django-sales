@customuser
Feature: Proccess of user

  @customuser.create.register.user
  Scenario: A user register
    When make "user" with:
      | id | username | email             | first_name | last_name | password |
      | 10 | devdiana | miemail@gmail.com | Diana      | Rojas     |   123456 |
    Then "post" the "user" to the resource "users":
    And the response of "user" must be:
      | status_code |
      |         201 |
