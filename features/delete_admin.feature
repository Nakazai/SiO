# Created by Jamal
Feature: Delete admin

  Scenario Outline: Delete admin succesfully
#    Given a form
    Given a overview of admins
    When i click delete on a admin
    And i get redirect to a confirmation message that tells me if i am sure to delete the admin
#    And i edit "<end_date>"
    And i see "<firstname>","<lastname>","<email>","<union_position>","<username>"
    And i confirm delete
    Then i will see admin does not exist anymore

    Examples: Admins
         | firstname | lastname | email        | union_position | username |
         | sara      | bara     | sa@gmail.com | leader         | sara     |


   Scenario Outline: Admin not deleted
#    Given a form
    Given a overview of admins
    When i click delete on a admin
    And i get redirect to a confirmation message that tells me if i am sure to delete the admin
    And i see "<firstname>","<lastname>","<email>","<union_position>","<username>"
    And  i cancel the action
    Then i will still see admin exist

    Examples: Admins
         | firstname | lastname | email        | union_position | username |
         | sara      | bara     | sa@gmail.com | leader         | sara     |