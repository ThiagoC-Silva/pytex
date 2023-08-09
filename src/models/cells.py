class Cells:
    def __init__(self, day, plate, description_vehicle, day_period, weight):
        self.day = day
        self.plate = plate
        self.description_vehcile = description_vehicle
        self.day_period = day_period
        self.weight = weight


    def check_records(self, record_table):
        status = False
        for data_records in record_table:
            if (
                self.day == data_records['Day'] and 
                self.plate == data_records['Plate'] and 
                self.day_period == data_records['Day Period']
            ):
                status = True
                break
        return status
            