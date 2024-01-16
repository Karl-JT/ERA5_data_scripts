import cdsapi
import calendar
from subprocess import call
import os

if __name__ == '__main__':
    c = cdsapi.Client()  
    # build up a dictionary

    variables = ['u_component_of_wind', 'v_component_of_wind', 'geopotential']    

    dic = {
        'product_type': 'reanalysis',
        'variable': '',
        'pressure_level': '500',
        'year': '',
        'month': [
            '01', '02', '03',
            '04', '05', '06',
            '07', '08', '09',
            '10', '11', '12'
            ],
        'day': [
            '01', '02', '03',
            '04', '05', '06',
            '07', '08', '09',
            '10', '11', '12',
            '13', '14', '15',
            '16', '17', '18',
            '19', '20', '21',
            '22', '23', '24',
            '25', '26', '27',
            '28', '29', '30',
            '31',
        ],

        'time': [
            '00:00', '01:00', '02:00',
            '03:00', '04:00', '05:00',
            '06:00', '07:00', '08:00',
            '09:00', '10:00', '11:00',
            '12:00', '13:00', '14:00',
            '15:00', '16:00', '17:00',
            '18:00', '19:00', '20:00',
            '21:00', '22:00', '23:00',
        ],

        'area':    [
             40, 70, -10,
             150,
         ],

        'format': 'netcdf',
    }

    for var in variables:
        for y in range(1940, 2023):  
            dic['year'] = str(y)
            dic['variable'] = var
            cur_path= os.getcwd() + '/'+ var + str(y) + '.nc'
            if not os.path.exists(cur_path):
                filename = var + str(y) + '.nc'    # file name
                c.retrieve('reanalysis-era5-pressure-levels', dic, filename)  # start downloading
                print('starting downloading year' + str(y))
            else:
                print('already exist')
