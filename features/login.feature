# Created by Jamal at 16.04.2017
Feature: Login to site
  # Enter feature description here

  Scenario Outline: Login success
    Given a user
    When i log in as "<username>" with "<password>"
    Then i see my dashboard

    Examples: Users
        | username          | password               |
        | foo               | bar                    |


  Scenario Outline: Login fails
    Given a user
    When i log in with invalid "<username>" and "<password>"
    Then i will see error message

    Examples: Users
        | username          | password               |
        | anonymous         | none                   |