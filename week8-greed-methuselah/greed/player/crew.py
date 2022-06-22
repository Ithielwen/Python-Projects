class Roster:
  """A collection of members.

    The responsibility of a cast is to keep track of a collection of members. It has methods for 
    adding, removing and getting them by a group name.

    Attributes:
        _members (dict): A dictionary of members { key: group_name, value: a list of members }
    """

  def __init__(self):
    """Constructs a new member."""
    self._members = {}
      
  def add_member(self, group, member):
    """Adds an member to the given group.
    
    Args:
      group (string): The name of the group.
      member (member): The member to add.
    """
    if not group in self._members.keys():
      self._members[group] = []
        
    if not member in self._members[group]:
      self._members[group].append(member)

  def get_members(self, group):
    """Gets the members in the given group.
    
    Args:
      group (string): The name of the group.

    Returns:
      List: The members in the group.
    """
    results = []
    if group in self._members.keys():
      results = self._members[group].copy()
    return results

  def get_all_members(self):
    """Gets all of the members in the cast.
    
    Returns:
      List: All of the members in the cast.
    """
    results = []
    for group in self._members:
      results.extend(self._members[group])
    return results

  def get_first_member(self, group):
    """Gets the first member in the given group.
    
    Args:
      group (string): The name of the group.
        
    Returns:
      List: The first member in the group.
    """
    result = None
    if group in self._members.keys():
      result = self._members[group][0]
    return result

  def remove_member(self, group, member):
    """Removes an member from the given group.
    
    Args:
      group (string): The name of the group.
      member (member): The member to remove.
    """
    if group in self._members:
      self._members[group].remove(member)