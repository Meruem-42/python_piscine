class CsvReader() :
    def __init__ (self, filename=None, sep=’,’, header=False, skip_top=0, skip_bottom=0) :

    def __enter__(self) :
        try :
            self.file = open(filename, "r")
            return self
        except Exception as e :
            return None

    def __exit__(self) :
        self.file.close()

    def getdata(self):
        """ Retrieves the data/records from skip_top to skip bottom.
            Returns:
            nested list (list(list, list, ...)) representing the data.
        """


    def getheader(self):
        """ Retrieves the header from the csv file.
            Returns:
            list: representing the data (when self.header is True).
            None: (when self.header is False).
        """
        header = []
        if self.header == True :
            self.file.read()

