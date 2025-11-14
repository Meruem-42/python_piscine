from the_bank import Account, Bank

if __name__ == "__main__":
    bank = Bank()

    william = Account("William John", value=1000.0)
    smith = Account("Smith Jane", value=1000.0)

    bank.add(william)
    bank.add(smith)

    # First transfer: should fail (no zip/addr attributes -> accounts corrupted)
    if bank.transfer("Smith Jane", "William John", 100.0):
        print("Success")
    else:
        print("Failed")

    # Fix both accounts
    bank.fix_account("William John")
    bank.fix_account("Smith Jane")

    # Second transfer: should succeed
    if bank.transfer("Smith Jane", "William John", 100.0):
        print("Success")
    else:
        print("Failed")
