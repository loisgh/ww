import os

class readDictionary:

    @staticmethod
    def doesFileExist(filename):
        if os.path.isfile(filename):
            return True
        else:
            raise FileNotFoundError("File {} was not found".format(filename))

    @staticmethod
    def get_dictionary(in_dict):
        dict_file = open(in_dict,'r')
        dict_data = dict_file.read()
        return dict_data

    @staticmethod
    def readfromDictionary(filename):
        dict_data = None
        if readDictionary.doesFileExist(filename):
            dict_data = readDictionary.get_dictionary(filename)
            readDictionary.parseandprintDictionary(dict_data)
        return dict_data

    @staticmethod
    def parseandprintDictionary(dict_data):
        dictionary = dict_data.split('\n')
        for word in dictionary:
            definitions = word.split("–")
            for definition in definitions:
                defs = definition.strip().split(",")
                for each_def in defs:
                    print(each_def.strip())


readDictionary.readfromDictionary('dictionary.txt')




