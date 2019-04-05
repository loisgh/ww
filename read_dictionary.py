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
        with open(in_dict, 'r') as dict_file:
            dict_data = dict_file.read()
        return dict_data

    @staticmethod
    def readfromDictionary(filename):
        dict_data = None
        if readDictionary.doesFileExist(filename):
            dict_data = readDictionary.get_dictionary(filename)
            dictionary = readDictionary.parseDictionary(dict_data)
            readDictionary.printDictionary(dictionary)
        return dict_data


    @staticmethod
    def parseDictionary(dict_data):
        dictionary = {}
        dictionary_list = dict_data.split('\n')
        for item in dictionary_list:
            items = item.split(" – ")
            key = items[0]
            value = items[1].split(", ")
            dictionary[key] = value
        return dictionary

    @staticmethod
    def printDictionary(dictionary):
        for key, values in dictionary.items():
            print(key)
            for value in values:
                print(value)


readDictionary.readfromDictionary('dictionary.txt')




