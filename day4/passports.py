import re

class PassportValidator: 
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    valid_eyecolors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    
    def __init__(self, passport):
        self.passport = passport

    def hasRequiredFields(self):
        if all(key in self.passport.keys() for key in self.required_fields):
            return True

    def validateBirthYear(self): 
        if PassportValidator.validateNumberInSpan(self.passport['byr'], 1920, 2002): 
            return True
    
    def validateIssueYear(self): 
        if PassportValidator.validateNumberInSpan(self.passport['iyr'], 2010, 2020): 
            return True

    def validateExpirationYear(self): 
        if PassportValidator.validateNumberInSpan(self.passport['eyr'], 2020, 2030): 
            return True
    
    def validatePid(self):
        if self.passport['pid'].isnumeric() and len(self.passport['pid']) is 9: 
            return True
    
    def validateEyeColor(self):
        if self.passport['ecl'] in self.valid_eyecolors:
            return True

    def validateHairColor(self):
        reg = re.compile("^#[0-9,A-F,a-f]{6}$")
        if reg.match(self.passport['hcl']):
            return True

    def validateHeight(self):
        val = self.passport['hgt'][:-2]
        unit = self.passport['hgt'][-2:]
        if unit == "cm" and PassportValidator.validateNumberInSpan(val, 150, 193):
            return True
        elif unit == "in" and PassportValidator.validateNumberInSpan(val, 59, 76):
            return True

        return False

    def hasValidFields(self):
        if not self.hasRequiredFields(): 
            return False
        if not self.validateBirthYear():
            return False
        if not self.validateIssueYear():
            return False
        if not self.validateExpirationYear():
            return False
        if not self.validatePid():
            return False
        if not self.validateEyeColor():
            return False
        if not self.validateHairColor():
            return False 
        if not self.validateHeight():
            return False

        return True
    
    @staticmethod
    def validateNumberInSpan(number, lower, upper):
        if number.isnumeric() and int(number) >= lower and int(number) <= upper: 
            return True

with open("../data/day4.txt") as f: 
    lines = f.read()
    passports = lines.split('\n\n')
    valid_part1 = 0
    valid_part2 = 0

    for pp in passports: 
        removedNewLines = pp.replace("\n", " ").rstrip()
        ppDict = dict(kvp.split(":") for kvp in removedNewLines.split(" "))
        pwValidator = PassportValidator(ppDict)
        if pwValidator.hasRequiredFields():
            valid_part1 += 1
        if pwValidator.hasValidFields():
            valid_part2 += 1
       

print(valid_part1)
print(valid_part2)