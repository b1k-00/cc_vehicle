##main py file

from ranges import RANGES


def check_status (reading, normal_range, warning_range):
    ##compare reading against mnormal & warnings / critical

    if normal_range[0] <= reading <= normal_range[1]:
        return "Normal"
    elif warning_range[0] <= reading <= warning_range[1]:
        return "Warning"
    else:
        return "Critical"



##input details

coolant_temp = int(input("Enter Coolant Temp: "))
oil_temp = int(input("Enter Oil Temp: "))
oil_pressure = int(input("Enter Oil Pressure: "))
transmission_temp = int(input("Enter Transmission Temp: "))
battery_voltage = int(input("Enter Battery Voltage: "))

#status checks

coolant_status = check_status(coolant_temp, RANGES["coolant"]["normal"], RANGES["coolant"]["warning"])
oil_temp_status = check_status(oil_temp, RANGES["oil_temp"]["normal"], RANGES["oil_temp"]["warning"])
oil_pressure_status = check_status(oil_pressure, RANGES["oil_pressure"]["normal"], RANGES["oil_pressure"]["warning"])
transmission_temp_status = check_status(transmission_temp, RANGES["transmission_temp"]["normal"], RANGES["transmission_temp"]["warning"]))
battery_volt_status = check_status(battery_voltage RANGES["battery_voltage"]["normal"], RANGES["battery_voltage"]["warning"])

##output

print(f"Coolant: {coolant_temp} - {coolant_status}")
print(f"Oil Temp: {oil_temp} - {oil_temp_status}")
print(f"Oil Pressure: {oil_pressure} - {oil_pressure_status}")
print(f"Transmission: {transmission_temp} - {transmission_temp_status}")
print(f"Battery Voltage: {battery_voltage} - {battery_voltage_status}")

