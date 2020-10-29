
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = []

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(1, 99)

    def add_member(self, member):
        if "id" in member:
            member["last_name"] = self.last_name
            self._members.append(member)
          
        else:
            member["id"] = self._generateId()
            member["last_name"] = self.last_name
            self._members.append(member)
        return None

        # fill this method and update the return
        

    def delete_member(self, id):
        for person in range(len(self._members)):
            print("hello",person)
            if self._members[person]['id'] == id:
                self._members.pop(person)
                print("hey", self._members)
                return None


        # fill this method and update the return

    def get_member(self, id):
        for x in self._members:
            if x["id"] == id:
                return x 
        return "person doesn't exist"
    def get_member_name(self, name):
        for x in self._members:
            if x["name"] == name:
                return x 
        return "person doesn't exist"

         
        # fill this method and update the return
        
  
    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        if len(self._members) > 0:
            return self._members
        return "Thier are no users"
