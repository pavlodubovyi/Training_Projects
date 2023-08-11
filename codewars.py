class Cube(object):
    # This cube needs help
    # Define a constructor which takes one integer, or handles no args
    
    def get_side(self):
        """Return the side of the Cube"""
        return self.__side

    def set_side(self, new_side):
        """Set the value of the Cube's side."""
        self.__side = new_side