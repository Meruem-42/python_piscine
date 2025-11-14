from the_bank import Account, Bank

if __name__ == "__main__":
    bank = Bank()

    william = Account("William John", value=1000.0, zip="10001", addr="Sunset Boulevard")
    smith = Account("Smith Jane", value=1000.0, zip="90001", bref="some bad field")

    bank.add(william)
    bank.add(smith)

    # This should fail because Smith Jane's account is corrupted (attribute 'bref')
    if bank.transfer("Smith Jane", "William John", 100.0):
        print("Success")
    else:
        print("Failed")
