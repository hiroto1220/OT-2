from opentrons import protocol_api

metadata = {
    'protocolName': 'Test Protocol',
    'apiLevel': '2.11'
}

tube_data = {
    'AA_6': 'A1',
    'Mg_80': 'A2',
    'K_1600': 'A3',
    'SPD_20': 'A4',
    'NTP_25': 'A5',
    '3PGA_600': 'A6',
    'PEG': 'B1',
    'milliQ': 'B2',
    'mixture': 'B3',
    'DNA': 'B4',
    'cell_extract': 'B5',   
}


# 2023/10/20 OT-2で無細胞系の発現を安定させる①
def run(protocol: protocol_api.ProtocolContext):

    left_tip_rack = protocol.load_labware('opentrons_96_tiprack_20ul', 10)
    right_tip_rack = protocol.load_labware('opentrons_96_tiprack_300ul', 11)

    tube_rack = protocol.load_labware('opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap', 4)
    well_plate_384 = protocol.load_labware('corning_384_wellplate_112ul_flat', 5)


    left_pipette = protocol.load_instrument('p20_single_gen2', 'left', tip_racks=[left_tip_rack])
    left_pipette.starting_tip = left_tip_rack['A1']
    
    right_pipette = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=[right_tip_rack])
    right_pipette.starting_tip = right_tip_rack['A1']


    # 条件1
    condition1 = {
        'AA_6':5, 
        'milliQ':1, 
        'Mg_80':2, 
        'K_1600':1, 
        'SPD_20':1, 
        'NTP_25':1, 
        '3PGA_600':1, 
        'PEG':1, 
        'mixture':1,
        'DNA':1, 
        'cell_extract':5
        }
    
    aa_volume = 80
    cell_extract_volume = 80
    
    # B2~B4は事前にアミノ酸を入れている
    for i in range(2,5):
        for _,(key,value) in enumerate(condition1.items()):
            if key == 'AA_6':
                pass
            elif key == 'cell_extract':
                pipetting_volume = cell_extract_volume*0.8
                if pipetting_volume <= 20:
                    left_pipette.pick_up_tip()
                    left_pipette.mix(5, pipetting_volume, tube_rack['B5'])
                    left_pipette.drop_tip()
                else:
                    right_pipette.pick_up_tip()
                    right_pipette.mix(5, pipetting_volume, tube_rack['B5'])
                    right_pipette.drop_tip()

                left_pipette.transfer(int(value), tube_rack[tube_data[key]], well_plate_384[f'B{i}'], new_tip='always')
                cell_extract_volume -= int(value)

            else:
                left_pipette.transfer(int(value), tube_rack[tube_data[key]], well_plate_384[f'B{i}'], new_tip='always')

    # B5~B9はアミノ酸もOT-2で分注する
    for i in range(5,10):
        for _,(key,value) in enumerate(condition1.items()):
            # アミノ酸を入れる前にはピペッティングする
            if key == 'AA_6':
                pipetting_volume = aa_volume*0.9
                if pipetting_volume <= 20:
                    left_pipette.pick_up_tip()
                    left_pipette.mix(5, pipetting_volume, tube_rack['A1'])
                    left_pipette.drop_tip()
                else:
                    right_pipette.pick_up_tip()
                    right_pipette.mix(5, pipetting_volume, tube_rack['A1'])
                    right_pipette.drop_tip()

                left_pipette.transfer(int(value), tube_rack[tube_data[key]], well_plate_384[f'B{i}'], new_tip='always')
                aa_volume -= int(value)


            # 細胞抽出液を入れる前にはピペッティングする
            elif key == 'cell_extract':
                pipetting_volume = cell_extract_volume*0.8
                if pipetting_volume <= 20:
                    left_pipette.pick_up_tip()
                    left_pipette.mix(5, pipetting_volume, tube_rack['B5'])
                    left_pipette.drop_tip()
                else:
                    right_pipette.pick_up_tip()
                    right_pipette.mix(5, pipetting_volume, tube_rack['B5'])
                    right_pipette.drop_tip()

                left_pipette.transfer(int(value), tube_rack[tube_data[key]], well_plate_384[f'B{i}'], new_tip='always')
                cell_extract_volume -= int(value)

            else:
                left_pipette.transfer(int(value), tube_rack[tube_data[key]], well_plate_384[f'B{i}'], new_tip='always')
        
   
    # B10はネガティブコントロール
    negative_control = {
        'AA_6':5, 
        'milliQ':2, 
        'Mg_80':2, 
        'K_1600':1, 
        'SPD_20':1, 
        'NTP_25':1, 
        '3PGA_600':1, 
        'PEG':1, 
        'mixture':1,
        'cell_extract':5, 
    }

    
    for _,(key,value) in enumerate(negative_control.items()):
        left_pipette.transfer(int(value), tube_rack[tube_data[key]], well_plate_384['B11'], new_tip='always')
        
            
            
    # 最後に全セルをピペッティングする
    for i in range(2,11):
        left_pipette.pick_up_tip()
        left_pipette.mix(5, 10, well_plate_384[f'B{i}'])
        left_pipette.drop_tip()
    


# 代表的な試薬条件で3サンプル分注する
# def run(protocol: protocol_api.ProtocolContext):
#     # ここの配置とlabware名は修正する
#     regent_rack = protocol.load_labware('opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap', 7)
#     tube_rack = protocol.load_labware('opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap', 8)
#     tiprack = protocol.load_labware('opentrons_96_tiprack_20ul', 10)

#     #ピペットは p20
#     pipette = protocol.load_instrument('p20_single_gen2', 'left', tip_racks=[tiprack])
#     pipette.starting_tip = tiprack['A1']

#     pipette.pick_up_tip(tiprack['A1'])


#     # Mg(80mM)を2ulずつ3ヶ所に分注
#     for i in range(3):
#         pipette.transfer(2, regent_rack['A1'], tube_rack[f'A{i+1}'], new_tip='never')
        
#     pipette.drop_tip()

#     # K(800mM)を2ulずつ3ヶ所に分注
#     for i in range(3):
#         pipette.transfer(2, regent_rack['A2'], tube_rack[f'A{i+1}'], new_tip='always')

#     # K(800mM)を2ulずつ3ヶ所に分注
#     for i in range(3):
#         pipette.transfer(2, regent_rack['A3'], tube_rack[f'A{i+1}'], new_tip='always')

#     # アミノ酸(6mM)を5ulずつ3ヶ所に分注
#     for i in range(3):
#         pipette.transfer(5, regent_rack['A3'], tube_rack[f'A{i+1}'], new_tip='always')

#     # スペルミジン(10mM)を2ulずつ3ヶ所に分注
#     for i in range(3):
#         pipette.transfer(2, regent_rack['A4'], tube_rack[f'A{i+1}'], new_tip='always')

#     # NTP(15mM)を2ulずつ3ヶ所に分注
#     for i in range(3):
#         pipette.transfer(2, regent_rack['A5'], tube_rack[f'A{i+1}'], new_tip='always')

#     # 3-PGA(300mM)を2ulずつ3ヶ所に分注
#     for i in range(3):
#         pipette.transfer(2, regent_rack['A6'], tube_rack[f'A{i+1}'], new_tip='always')

