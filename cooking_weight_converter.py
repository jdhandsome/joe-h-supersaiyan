weight_values = {
    "cup" : 1,
    "gallon" : 0.0625,
    "liter" : 0.2366,
    "milliliter" : 236.6,
    "fl oz" : 8,
    "pint" : .5,
    "quart" : 0.25,
    "tablespoon" : 16,
    "teaspoon" : 48
}
temp_dict = {} #temp dictionary to house the converted weight as a base of 1

weight_to_convert = input('input unit to convert: ')
weight_to_convert = weight_to_convert.lower()
amount_to_convert = input('how much to convert: ')
x = float(amount_to_convert)

if weight_to_convert in weight_values: #checks if weight entered is in dictionary
    t_value = 1
    for w in weight_values: #loops through the pairs
        if weight_to_convert == w:
            get_num = float(weight_values[w])
            temp_dict[w] = 1
            t_value = get_num
    for w in weight_values:
        if weight_to_convert != w:
            temp_dict[w] = weight_values[w] / t_value #creates  dictionary where the weight to convert is the primary key

    for t in temp_dict: #iterate over temp dict

        conv_number = temp_dict[t] * x #convert temp dict value to desired amount

        print(t, conv_number) # return information


else:
    print("input not valid")
