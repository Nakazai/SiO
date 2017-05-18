# Created by Jamal
Feature: Add admin

  Scenario Outline: Admin succesfully added
    Given a admin form
    When i fill in "<firstname>","<lastname>","<email>","<union_position>","<username>"
    And  register the admin form
    Then i will see the new admin added

    Examples: Admins
        | firstname | lastname | email        | union_position | username |
        | sara      | bara     | fb@gmail.com | leader         | sara     |


   Scenario Outline: Admin not added
    Given a admin form
    When i fill in "<firstname>","<lastname>","<email>","<union_position>","<username>"
    And  cancel the admin form
    Then i will be redirected to overview of all admins

    Examples: Admins
        | firstname | lastname | email        | union_position | username |
        | sara      | bara     | fb@gmail.com | leader         | sara     |



