km_to_m = lambda km: km * 1000
m_to_cm = lambda m: m * 100
cm_to_mm = lambda cm: cm * 10
feet_to_inches = lambda ft: ft * 12
inches_to_cm = lambda inch: inch * 2.54
def distance_converter(value, conv_type, func):
 print(f"{value} {conv_type} = {func(value)}")
d = float(input("Enter distance: "))
distance_converter(d, "km to m", km_to_m)
distance_converter(d, "m to cm", m_to_cm)
distance_converter(d, "cm to mm", cm_to_mm)
distance_converter(d, "feet to inches", feet_to_inches)
distance_converter(d, "inches to cm", inches_to_cm)