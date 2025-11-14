class Account(object):

    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.__dict__.update(kwargs)

        self.id = self.ID_COUNT
        Account.ID_COUNT += 1
        self.name = name
        if not hasattr(self, 'value'):
            self.value = 0

        if self.value < 0:
            raise AttributeError("Attribute value cannot be negative.")
        if not isinstance(self.name, str) :
            raise AttributeError("Attribute name must be a str object.")

    def transfer(self, amount):
        self.value += amount


class Bank(object) :
    """The bank"""
    def __init__(self) :
        self.accounts = []

    def add(self, new_account) :
        """ Add new_account in the Bank
            @new_account: Account() new account to append
            @return True if success, False if an error occured
        """
        if not isinstance(new_account, Account) :
            return False
        if not hasattr(new_account, "name"):
            return false
        if any(account.name == new_account.name for account in self.accounts) :
                return False
        self.accounts.append(new_account)
        return True

    def transfer(self, origin, dest, amount) :
        """ Perform the fund transfer
            @origin: str(name) of the first account
            @dest: str(name) of the destination account
            @amount: float(amount) amount to transfer
            @return True if success, False if an error occured
        """
        origin_acc = next((acc for acc in self.accounts if acc.name == origin), None)
        dest_acc = next((acc for acc in self.accounts if acc.name == dest), None)
        if origin_acc is None or dest_acc is None:
            return False
        for account in [origin_acc, dest_acc] :
            if not isinstance(account, Account) :
                return False
            if len(account.__dict__)%2 == 0 :
                return False
            if any(attr.startswith("b") for attr in account.__dict__) :
                return False
            if not any(attr.startswith("zip") or attr.startswith("addr") for attr in account.__dict__):
                return False
            if not all(hasattr(account, attr) for attr in ("name", "id", "value")):
                return false
            if not isinstance(account.__dict__["name"], str) :
                return False
            if not isinstance(account.__dict__["id"], int) :
                return False
            if not isinstance(account.__dict__["value"], (int, float)) :
                return False
        if amount < 0 or origin_acc.value < amount :
            return False
        if not origin_acc.name is dest_acc.name :
            origin_acc.transfer(-amount)
            dest_acc.transfer(amount)
        return True

        
        
        

    def fix_account(self, name) :
        """ fix account associated to name if corrupted
            @name:
            str(name) of the account
            @return True if success, False if an error occured
        """
        if not isinstance(name, str) :
            return False
        for account in self.accounts :
            if account.name == name :
                for attr in account.__dict__ :
                    if attr.startswith("b") :
                        delattr(attr)
                if not any(attr.startswith("zip") or attr.startswith("addr") for attr in account.__dict__):
                    setattr(account, "addr", "unknown")
                if not all(hasattr(account, attr) for attr in ("name", "id", "value")):
                    return false
                if len(account.__dict__)%2 == 0 :
                    setattr(account, "Fix_num", "NA")
                if not isinstance(account.__dict__["name"], str) :
                    return False
                if not isinstance(account.__dict__["id"], int) :
                    return False
                if not isinstance(account.__dict__["value"], (int, float)) :
                    return False
                return True
        return False


        

