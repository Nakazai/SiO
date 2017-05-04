# Created by Jamal
Feature: Delete member

  Scenario Outline: Delete member succesfully
#    Given a form
    Given a overview of members
    When i click delete on a member
#    And i edit "<end_date>"
    And i get redirect to a confirmation message that tells me if i am sure to delete the member
#    And i see "<firstname>","<lastname>","<email>","<gender>","<date_of_birth>","<reg_date>","<end_date>" to confirm delete
    And i see "<firstname>","<lastname>","<email>","<gender>","<date_of_birth>","<reg_date>","<end_date>"
    And i confirm delete
    Then i will see member does not exist anymore

    Examples: Members
        | firstname | lastname | email        | gender | date_of_birth | reg_date   | end_date    |
        | foo       | bar      | sa@gmail.com | female | 1990-02-01    | 2017-01-01 | 2017-06-03  |


   Scenario Outline: Member not deleted
#    Given a form
    Given a overview of members
    When i click delete on a member
    And i get redirect to a confirmation message that tells me if i am sure to delete the member
#    And i see "<firstname>","<lastname>","<email>","<gender>","<date_of_birth>","<reg_date>","<end_date>" to cancel
    And i see "<firstname>","<lastname>","<email>","<gender>","<date_of_birth>","<reg_date>","<end_date>"
    And i cancel the action
    Then i will still see member exist

    Examples: Members
        | firstname | lastname | email        | gender | date_of_birth | reg_date   | end_date    |
        | foo       | bar      | sa@gmail.com | female | 1990-02-01    | 2017-01-01 | 2017-06-03  |
