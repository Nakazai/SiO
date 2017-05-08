# Created by Jamal
Feature: Edit member

  Scenario Outline: Edit member succesfully
#    Given a form
    Given a overview of members
    When i click on update
#    And i edit "<end_date>"
    And i edit in "<firstname>","<lastname>","<email>","<date_of_birth>","<reg_date>","<end_date>"
    And  update the form
    Then i will see the new member added with correct email

    Examples: Members
        | firstname | lastname | email        | gender | date_of_birth | reg_date   | end_date    |
        | foo       | bar      | sa@gmail.com | female | 1990-02-01    | 2017-01-01 | 2017-06-03  |


   Scenario Outline: Member not edited
#    Given a form
    Given a overview of members
    When i click on update
    And i fill in "<reg_date>"
    And  cancel the form
    Then i will be redirected to overview of all members

    Examples: Members
        | firstname | lastname | email        | gender | date_of_birth | reg_date   | end_date    |
        | foo       | bar      | fb@gmail.com | female | 1990-02-01    | 2017-01-01 | 2017-06-03  |