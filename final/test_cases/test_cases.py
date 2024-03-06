import unittest
from functions.functions import *

class TestCases(unittest.TestCase):
    """Tests for functions in functions.py"""
    def testValidPart(self):
        """Here are a bunch of values I think should work"""
        validNames = ["Danny Srour", "Danny-Srour", "Danny'"]
        validCompany = ["Apple Inc.", "Google", "Microsoft"]
        validAddress = ["123 Main St.", "123 Main St. #2", "123-125 Main St."]
        validCity = ["New York", "San Francisco", "Chicago"]
        validZip = ["10001", "94105", "60601"]
        validState = ["NY", "CA", "IL"]
        validEmail = ["danny.srour@example.com", "danny+srour@example.com", "danny_srour@example.com"]
        validPhone = ["1234567890", "123-456-7890", "123.456.7890"]
        validNumber = ["1", "100", "9999"]
        validExistence = ["Danny Srour", "Apple Inc.", "123 Main St."]



        for name in validNames:
            self.assertTrue(isNameValid(name))

        for company in validCompany:
            self.assertTrue(isCompanyValid(company))

        for address in validAddress:
            self.assertTrue(isAddressValid(address))

        for city in validCity:
            self.assertTrue(isCityValid(city))

        for zip in validZip:
            self.assertTrue(isZipCodeValid(zip))   

        for state in validState:
            self.assertTrue(isStateValid(state))

        for email in validEmail:
            self.assertTrue(isEmailValid(email))

        for phone in validPhone:
            self.assertTrue(isPhoneValid(phone)) 

        for number in validNumber:
            self.assertTrue(isNumberValid(number))

        for existence in validExistence:
            self.assertTrue(existenceCheck(existence))

    

    def testInvalidPart(self):
        """Here are a bunch of values I think should not work"""
        invalidNames = ["Danny Srour!", "Danny Srour#", "Danny Srour$"]
        invalidCompany = ["Apple~", "Google`", "Microsoft^"]
        invalidAddress = ["123 Main St.!", "123 Main St.@", "123-125 Main St.%"]
        invalidCity = ["New York!", "San Francisco@", "Chicago$"]
        invalidZip = ["1000a", "94b105", "60c601"]
        invalidState = ["NYS", "CAL", "ILL"]
        invalidEmail = ["danny.srour@example*", "danny.srour@~", "danny_srour.com^"]
        invalidPhone = ["123456789", "123-456-789", "123.456.789"]
        invalidNumber = ["1a", "100b", "9999c"]
        invalidExistence = [""]

        for name in invalidNames:
            self.assertFalse(isNameValid(name))

        for company in invalidCompany:
            self.assertFalse(isCompanyValid(company))

        for address in invalidAddress:
            self.assertFalse(isAddressValid(address))

        for city in invalidCity:
            self.assertFalse(isCityValid(city))

        for zip in invalidZip:
            self.assertFalse(isZipCodeValid(zip))   

        for state in invalidState:
            self.assertFalse(isStateValid(state))

        for email in invalidEmail:
            self.assertFalse(isEmailValid(email))

        for phone in invalidPhone:
            self.assertFalse(isPhoneValid(phone))

        for number in invalidNumber:
            self.assertFalse(isNumberValid(number))

        for existence in invalidExistence:
            self.assertFalse(existenceCheck(existence)) 