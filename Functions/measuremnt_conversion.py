def convert_volume(fluid_ounce):
    ml = fluid_ounce * 29.5
    return ml
print("The volume in milliliters is ", str(convert_volume(2)))