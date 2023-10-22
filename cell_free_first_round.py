from opentrons import protocol_api

metadata = {
    'protocolName': 'Test Protocol',
    'apiLevel': '2.11'
}

tube_data = {
    'Mg_80': 'A1',
    'Mg_44': 'A2',
    'Mg_16': 'A3',
    'K_1600': 'A4',
    'K_880': 'A5',
    'K_160': 'A6',
    'AA_6': 'B1',
    'AA_4.15': 'B2',
    'AA_0.6': 'B3',
    'SPD_20': 'B4',
    'SPD_11': 'B5',
    'SPD_2': 'B6',
    'NTP_25': 'C1',
    'NTP_14': 'C2',
    'NTP_3': 'C3',
    '3PGA_600': 'C4',
    '3PGA_330': 'C5',
    '3PGA_60': 'C6',
    'PEG': 'D1',
    'DNA': 'D2',
    'milliQ': 'D3',
    'cell_extract': 'D4',
    'mixture': 'D5',
}


# 代表的な試薬条件で3サンプル分注する
def run(protocol: protocol_api.ProtocolContext):
    tip_rack = protocol.load_labware('opentrons_96_tiprack_20ul', 10)
    tube_rack = protocol.load_labware('opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap', 4)
    well_plate_384 = protocol.load_labware('corning_384_wellplate_112ul_flat', 5)

    #ピペットは p20
    pipette = protocol.load_instrument('p20_single_gen2', 'left', tip_racks=[tip_rack])
    pipette.starting_tip = tip_rack['A1']


    # 条件1
    condition1 = {
        'Mg_80':2, 
        'K_1600':1, 
        'AA_6':5, 
        'SPD_20':1, 
        'NTP_25':1, 
        '3PGA_600':1, 
        'PEG':1, 
        'DNA':1, 
        'cell_extract':5, 
        'milliQ':1, 
        'mixture':1
        }
    
    for _,(key,value) in enumerate(condition1.items()):
        pipette.transfer(int(value), tube_rack[tube_data[key]], well_plate_384['B2'], new_tip='always')
        
    # 条件2
    condition2 = {
        'Mg_44':2,
        'K_1600':1,
        'AA_6':5,
        'SPD_20':1,
        'NTP_25':1,
        '3PGA_600':1,
        'PEG':1,
        'DNA':1,
        'cell_extract':5,
        'milliQ':1,
        'mixture':1
        }
    
    for _,(key,value) in enumerate(condition2.items()):
        pipette.transfer(int(value), tube_rack[tube_data[key]], well_plate_384['B3'], new_tip='always')
        
    
    # 条件3
    condition3 = {
        'Mg_16':1,
        'K_1600':1,
        'AA_6':5,
        'SPD_20':1,
        'NTP_25':1,
        '3PGA_600':1,
        'PEG':1,
        'DNA':1,
        'cell_extract':5,
        'milliQ':2,
        'mixture':1
        }
    
    for _,(key,value) in enumerate(condition3.items()):
        pipette.transfer(int(value), tube_rack[tube_data[key]], well_plate_384['B4'], new_tip='always')

    # 条件4
    condition4 = {
        'Mg_80':2,
        'K_880':1,
        'AA_6':5,
        'SPD_20':1,
        'NTP_25':1,
        '3PGA_600':1,
        'PEG':1,
        'DNA':1,
        'cell_extract':5,
        'milliQ':1,
        'mixture':1
        }
    
    for _,(key,value) in enumerate(condition4.items()):
        pipette.transfer(int(value), tube_rack[tube_data[key]], well_plate_384['B5'], new_tip='always')

    # 条件5
    condition5 = {
        'Mg_80':2,
        'K_160':1,
        'AA_6':5,
        'SPD_20':1,
        'NTP_25':1,
        '3PGA_600':1,
        'PEG':1,
        'DNA':1,
        'cell_extract':5,
        'milliQ':1,
        'mixture':1
        }
    
    for _,(key,value) in enumerate(condition5.items()):
        pipette.transfer(int(value), tube_rack[tube_data[key]], well_plate_384['B6'], new_tip='always')
        

    # 条件6
    condition6 = {
        'Mg_80':2,
        'K_1600':1,
        'AA_4.15':4,
        'SPD_20':1,
        'NTP_25':1,
        '3PGA_600':1,
        'PEG':1,
        'DNA':1,
        'cell_extract':5,
        'milliQ':2,
        'mixture':1
        }
    
    for _,(key,value) in enumerate(condition6.items()):
        pipette.transfer(int(value), tube_rack[tube_data[key]], well_plate_384['B7'], new_tip='always')


    # 条件7
    condition7 = {
        'Mg_80':2,
        'K_1600':1,
        'AA_0.6':5,
        'SPD_20':1,
        'NTP_25':1,
        '3PGA_600':1,
        'PEG':1,
        'DNA':1,
        'cell_extract':5,
        'milliQ':1,
        'mixture':1
        }
    
    for _,(key,value) in enumerate(condition7.items()):
        pipette.transfer(int(value), tube_rack[tube_data[key]], well_plate_384['B8'], new_tip='always')

    
    # 条件8
    condition8 = {
        'Mg_80':2,
        'K_1600':1,
        'AA_6':5,
        'SPD_11':1,
        'NTP_25':1,
        '3PGA_600':1,
        'PEG':1,
        'DNA':1,
        'cell_extract':5,
        'milliQ':1,
        'mixture':1
        }
    
    for _,(key,value) in enumerate(condition8.items()):
        pipette.transfer(int(value), tube_rack[tube_data[key]], well_plate_384['B9'], new_tip='always')

    
     # 条件9
    condition9 = {
        'Mg_80':2,
        'K_1600':1,
        'AA_6':5,
        'SPD_2':1,
        'NTP_25':1,
        '3PGA_600':1,
        'PEG':1,
        'DNA':1,
        'cell_extract':5,
        'milliQ':1,
        'mixture':1
        }
    
    for _,(key,value) in enumerate(condition9.items()):
        pipette.transfer(int(value), tube_rack[tube_data[key]], well_plate_384['B10'], new_tip='always')

    
    # 条件10
    condition10 = {
        'Mg_80':2,
        'K_1600':1,
        'AA_6':5,
        'SPD_20':1,
        'NTP_14':1,
        '3PGA_600':1,
        'PEG':1,
        'DNA':1,
        'cell_extract':5,
        'milliQ':2,
        'mixture':1
        }
    
    for _,(key,value) in enumerate(condition10.items()):
        pipette.transfer(int(value), tube_rack[tube_data[key]], well_plate_384['B11'], new_tip='always')

    
     # 条件11
    condition11 = {
        'Mg_80':2,
        'K_1600':1,
        'AA_6':5,
        'SPD_20':1,
        'NTP_3':1,
        '3PGA_600':1,
        'PEG':1,
        'DNA':1,
        'cell_extract':5,
        'milliQ':1,
        'mixture':1
        }
    
    for _,(key,value) in enumerate(condition11.items()):
        pipette.transfer(int(value), tube_rack[tube_data[key]], well_plate_384['B12'], new_tip='always')


     # 条件12
    condition12 = {
        'Mg_80':2,
        'K_1600':1,
        'AA_6':5,
        'SPD_20':1,
        'NTP_25':1,
        '3PGA_330':1,
        'PEG':1,
        'DNA':1,
        'cell_extract':5,
        'milliQ':1,
        'mixture':1
        }
    
    for _,(key,value) in enumerate(condition12.items()):
        pipette.transfer(int(value), tube_rack[tube_data[key]], well_plate_384['B13'], new_tip='always')


     # 条件13
    condition13 = {
        'Mg_80':2,
        'K_1600':1,
        'AA_6':5,
        'SPD_20':1,
        'NTP_25':1,
        '3PGA_60':1,
        'PEG':1,
        'DNA':1,
        'cell_extract':5,
        'milliQ':1,
        'mixture':1
        }
    
    for _,(key,value) in enumerate(condition13.items()):
        pipette.transfer(int(value), tube_rack[tube_data[key]], well_plate_384['B14'], new_tip='always')

    # ネガティブコントロール
    negative_control = {
    'Mg_80':2, 
    'K_1600':1, 
    'AA_6':5, 
    'SPD_20':1, 
    'NTP_25':1, 
    '3PGA_600':1, 
    'PEG':1, 
    'cell_extract':5, 
    'milliQ':2, 
    'mixture':1
    }

    
    for i in range(3):
        for _,(key,value) in enumerate(negative_control.items()):
            pipette.transfer(int(value), tube_rack[tube_data[key]], well_plate_384[f'B'+str(15+i)], new_tip='always')
            
    