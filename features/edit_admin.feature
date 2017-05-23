# Created by Jamal
Feature: Edit admin

  Scenario Outline: Edit admin succesfully
    Given a overview of admins
    When i click on update
    And i edit in "<firstname>","<lastname>","<email>","<union_position>","<username>"
    And  update the admin form
    Then i will see the new admin added with correct information

    Examples: Admins
         | firstname | lastname | email        | union_position | username |
         | sara      | bara     | fb@gmail.com | leader         | sara     |


   Scenario Outline: Admin not edited
    Given a overview of admins
    When i click on update
    And i edit in "<union_position>"
    And  cancel the admin form
    Then i will be redirected to overview of all admins

    Examples: Admins
         | union_position |
         | leader         |




