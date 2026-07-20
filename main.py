##main py file

def check_status (reading, normal_range, watrning_range):
    ##compare reading against mnormal & warnings / critical

    if normal_range[0] < reading < normal_range[0]:
        return "Normal"
    elif warning_range[0] < reading < warning_range[1]:
        return "Warning"
    else:
        return "Critical"



## daashboard reading


coolant_temp = 210
oil_temp = 210
oil_pressure = 220
transmission_temp = 180

print("Coolant Temp:", coolant_temp)
print("Oil Temp:", oil_temp)
print("Oil Pressure", oil_pressure)
print("Transmission Temp:", transmission_temp)
