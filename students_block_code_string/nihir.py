string1 = 'abc'
string2 = 'xyz'

string1_updated = string2[0:2] + string1[2:len(string1)]
string2_updated = string1[0:2] + string2[2:len(string2)]

result = string1_updated + ' ' + string2_updated
