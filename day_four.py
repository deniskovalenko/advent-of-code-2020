
import re

def read_passports():
    filename = 'day_4_input.txt'
    passport_data = []
    with open(filename) as infile:
        current_passport_fields = []
        count = 0
        for line in infile:
            # print("line number ", count)
            count+=1
            if line == '\n':
                passport_data.append(current_passport_fields)
                current_passport_fields = []
            else: 
                l = line.strip() #get rid of \n or spaces
                fileds = l.split(' ')
                current_passport_fields = current_passport_fields + fileds

        return passport_data


def number_validation_function(digits, min, max):
    def validate(string):
        if len(string) != digits:
            return False
        string = int(string)
        return string >= min and string <= max
    return validate

def height_validation_function(string):
    units = string[-2:]
    try:
        value = int(string[:-2])
    except Exception:
        return False
    if units == "in":
        return value >= 59 and value <= 76
    if units == "cm":
        return value >= 150 and value <= 193

    return False

def hair_color_validation_function(string):
    if len(string) != 7:
        return False
    if string[0] != "#":
        return False

    for c in string[1:]:
        if c not in {'a','b','c','d','e','f', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}: #don't judge, I suck at Regex and never done it in Python :) 
            return False
    return True
    # "# followed by exactly six characters 0-9 or a-f."

def eye_color(string):
    # exactly one of: amb blu brn gry grn hzl oth
    colors = {'amb','blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}
    return string in colors

def passport_validation_function(id):
    #a nine-digit number, including leading zeroes.
    #todo check this...
    try:
        numeric = int(id)
    except Exception:
        return False
    return numeric >= 0 and numeric <= 999999999


def is_passport_valid(array_of_fields):
    #what's up if some other fields?
    required_fields = {"byr": number_validation_function(4, 1920, 2002),
                       "iyr": number_validation_function(4, 2010, 2020),
                        "eyr": number_validation_function(4, 2020, 2030)
                        , "hgt": height_validation_function
                        , "hcl": hair_color_validation_function
                        , "ecl": eye_color
                        , "pid": passport_validation_function
                        }
    optional_fields = {"cid"}

    for field in array_of_fields:
        name, data = field.split(":")
        if name in required_fields:
            validation_fun = required_fields[name]
            if not validation_fun(data):
                # print(name, " didn't pass validation")
                return False
            required_fields.pop(name)
        elif name in optional_fields:
            a = 3
            # print("optional found")
        else: 
            print("weird filed", name)
    
    return  len(required_fields) == 0

def count_valid_documents():
    passports = read_passports()
    print("Lenght of passports: ", len(passports))
    
    valid_counter = 0
    for passport in passports:
        # print(passport)
        if is_passport_valid(passport):
            # print("valid")
            valid_counter += 1
    return valid_counter


# print(number_validation_function(4, 2010, 2020)("123"))

# print(re.search(r'#([a-f]){6}', "#abcdef"))
print(count_valid_documents())



"""
--- Day 4: Passport Processing ---

You arrive at the airport only to realize that you grabbed your North Pole Credentials instead of your passport. While these documents are extremely similar, North Pole Credentials aren't issued by a country and therefore aren't actually valid documentation for travel in most of the world.

It seems like you're not the only one having problems, though; a very long line has formed for the automatic passport scanners, and the delay could upset your travel itinerary.

Due to some questionable network security, you realize you might be able to solve both of these problems at the same time.

The automatic passport scanners are slow because they're having trouble detecting which passports have all required fields. The expected fields are as follows:

    byr (Birth Year)
    iyr (Issue Year)
    eyr (Expiration Year)
    hgt (Height)
    hcl (Hair Color)
    ecl (Eye Color)
    pid (Passport ID)
    cid (Country ID)

Passport data is validated in batch files (your puzzle input). Each passport is represented as a sequence of key:value pairs separated by spaces or newlines. Passports are separated by blank lines.

Here is an example batch file containing four passports:

ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in

The first passport is valid - all eight fields are present. The second passport is invalid - it is missing hgt (the Height field).

The third passport is interesting; the only missing field is cid, so it looks like data from North Pole Credentials, not a passport at all! Surely, nobody would mind if you made the system temporarily ignore missing cid fields. Treat this "passport" as valid.

The fourth passport is missing two fields, cid and byr. Missing cid is fine, but missing any other field is not, so this passport is invalid.

According to the above rules, your improved system would report 2 valid passports.

Count the number of valid passports - those that have all required fields. Treat cid as optional. In your batch file, how many passports are valid?

"""