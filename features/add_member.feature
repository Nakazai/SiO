# Created by Jamal at 18.04.2017
Feature: Add member
  # Enter feature description here

  Scenario Outline: Member succesfully added
    Given a form
    When i fill in "<firstname>","<lastname>","<email>","<gender>","<date_of_birth>","<reg_date>","<end_date>"
    And  register the form
    Then i will see the new member added

    Examples: Members
        | firstname | lastname | email        | gender | date_of_birth | reg_date   | end_date    |
        | foo       | bar      | fb@gmail.com | female | 1990-02-01    | 2017-01-01 | 2017-06-03  |


   Scenario Outline: Member not added
    Given a form
    When i fill in "<firstname>","<lastname>","<email>","<gender>","<date_of_birth>","<reg_date>","<end_date>"
    And  cancel the form
    Then i will be redirected to overview of all members

    Examples: Members
        | firstname | lastname | email        | gender | date_of_birth | reg_date   | end_date    |
        | foo       | bar      | fb@gmail.com | female | 1990-02-01    | 2017-01-01 | 2017-06-03  |