class Comment:
    def __init__(self, sku=None, text=None, owner=None):
        """
        Constructor to intialise object
        sku - Number
        text - String
        owner - String
        """
        self.sku = sku
        self.text = text
        self.owner = owner

    def set_sku(self, sku):
        """
        Set sku parameter
        """

        self.sku = sku

    def get_sku(self):
        """
        Get sku parameter
        """
        return self.sku

    def set_text(self, text):
        """
        Set text parameter
        """
        self.text = text

    def get_text(self):
        """
        Get text parameter
        """
        return self.text

    def set_owner(self, owner):
        """
        Set owner parameter
        """
        self.owner = owner

    def get_owner(self):
        """
        Get owner parameter
        """
        return self.owner

    def __repr__(self):
        """
        String representation of object
        """
        return f'Comment: "{self.sku} - {self.text}" - written by: {self.owner}'
