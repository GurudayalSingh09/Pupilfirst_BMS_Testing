def control_algorithm(data,ser):

    iteration = float(data[0])
    Ambient_temperature = float(data[1])
    cell_1_temperature  = float(data[3])
    cell_2_temperature  = float(data[4])
    current  = float(data[13])
    pack_voltage = float(data[14])
    cell_1_voltage  = float(data[5])
    cell_2_voltage  = float(data[6])
    current = float(data[13])
    power = float(data[12])


    def charge():
        ser.write(bytes("1", 'utf-8'))
        print("\nCharging....\n", end='\r')
    def Discharge():
        ser.write(bytes("2", 'utf-8'))
        print("\ndischarging....\n", end='\r')
    def Balance_1():
        ser.write(bytes("3", 'utf-8'))
        print("\nBalancing cell 1....\n", end='\r')
    def Balance_2():
        ser.write(bytes("4", 'utf-8'))
        print("\nBalancing cell 2\n", end='\r')
    def stop():
        ser.write(bytes("5", 'utf-8'))
        print("\nMonitoring...\n", end='\r')

# -----------------------------------Add Your Code/Algorithm here ----------------

# Instructions
        ## cell_1_voltage =  Voltage of Cell number 1
        ## cell_2_voltage =  Voltage of Cell number 2
        ## pack_voltage = Voltage of the entire battery pack (cell 1 + cell 2)

        ## Balance_1 = Switch on balancing for cell 1
        ## Balance_2 = Switch on balancing for cell 2

        ## charge = Switch on Charging
        ## discharge = Switch on Discharging

        ## Stop = Stop all operations

        ## ambient_temperature = Room temperature value


        ## cell_1_temperature =  temperature of Cell number 1
        ## cell_2_temperature =  temperature of Cell number 2

        ## current = Total current passing through the circuit




    # if iteration == 10:
    #     charge()
    # elif iteration == 1800:
    #     Discharge()
    # elif iteration ==2100:
    #     charge()
    # elif iteration ==  3900:
    #     Discharge()
    # elif iteration == 4200:
    #     stop()


# ----------------------------------- Your Code/Algorithm here ----------------


    # if pack_voltage <= 5.5 :
    #     charge()
    # elif cell_1_voltage  :
    #     Discharge()
    # elif iteration == 20:
    #     Balance_1()
    # elif iteration == 25:
    #     Balance_2()
    # elif pack_voltage <= 6.4:
    #     stop()

    float tolerance = 0.05 #setting tolerance as 5%

    if ( cell_1_voltage < 3.2 or cell_2_voltage < 3.2 ) and 15 < cell_1_temperature < 40 and 15 < cell_2_temperature <40 :

        while cell_1_voltage < 3.6 or cell_2_voltage < 3.6:
            charge()
    else:
        stop()

    if cell_1_voltage > cell_2_voltage: 
        Balance_1()
    elif cell_2_voltage > cell_1_voltage :
            Balance_2()

    elif cell_1_voltage == cell_2_voltage :
         
         if cell_1_voltage > 3.6 and cell_2_voltage > 3.6:
             Balance_1()
             Balance_2()
    
    else :
        stop()

 
    