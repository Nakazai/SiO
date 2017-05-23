# Created by Jamal
Feature: Login to site

  Scenario Outline: Login success
    Given a user
    When i log in as "<username>" with "<password>"
    Then i can see my home site

    Examples: User
        | username          | password               |
        | foo               | bar                    |


  Scenario Outline: Login fails
    When i log in with invalid "<username>" and "<password>"
    Then i will see error message

    Examples: Users
        | username          | password               |
        | anonymous         | none                   |




