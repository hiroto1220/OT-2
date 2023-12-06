from opentrons import protocol_api

metadata = {
    'protocolName': 'Test Protocol',
    'apiLevel': '2.11'
}

# チューブラックに設置するする各溶液の種類・濃度とチューブの位置を決める
tube_data = {
    'AA_6': 'A1',
    'AA_4.15': 'A2',
    'AA_0.6': 'A3',
    'Mg_80': 'A4',
    'Mg_44': 'A5',
    'Mg_16': 'A6',
    'K_1600': 'B1',
    'K_880': 'B2',
    'K_160': 'B3',
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
    'milliQ': 'D2',
    'mixture': 'D3',
    'DNA': 'D4',
    'cell_extract': 'D5',
}

tube_volume = {
    'AA_6': 58,
    'AA_4.15': 11,
    'AA_0.6': 10,
    'cell_extract': 100,
}


# 条件1(B2)
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

# 条件2(B3)
condition2 = {
    'AA_6':5,
    'milliQ':1,
    'Mg_44':2,
    'K_1600':1,
    'SPD_20':1,
    'NTP_25':1,
    '3PGA_600':1,
    'PEG':1,
    'mixture':1,
    'DNA':1,
    'cell_extract':5,
    }

# 条件3
condition3 = {
    'AA_6':5,
    'milliQ':1,
    'Mg_16':2,
    'K_1600':1,
    'SPD_20':1,
    'NTP_25':1,
    '3PGA_600':1,
    'PEG':1,
    'mixture':1,
    'DNA':1,
    'cell_extract':5,
    }

# 条件4
condition4 = {
    'AA_6':5,
    'milliQ':1,
    'Mg_80':2,
    'K_880':1,
    'SPD_20':1,
    'NTP_25':1,
    '3PGA_600':1,
    'PEG':1,
    'mixture':1,
    'DNA':1,
    'cell_extract':5,
}

# 条件5
condition5 = {
    'AA_6':5,
    'milliQ':1,
    'Mg_80':2,
    'K_160':1,
    'SPD_20':1,
    'NTP_25':1,
    '3PGA_600':1,
    'PEG':1,
    'mixture':1,
    'DNA':1,
    'cell_extract':5,
    }

# 条件6
condition6 = {
    'AA_4.15':4,
    'milliQ':2,
    'Mg_80':2,
    'K_1600':1,
    'SPD_20':1,
    'NTP_25':1,
    '3PGA_600':1,
    'PEG':1,
    'mixture':1,
    'DNA':1,
    'cell_extract':5,
    }

# 条件7
condition7 = {
    'AA_0.6':5,
    'milliQ':1,
    'Mg_80':2,
    'K_1600':1,
    'SPD_20':1,
    'NTP_25':1,
    '3PGA_600':1,
    'PEG':1,
    'mixture':1,
    'DNA':1,
    'cell_extract':5,
    }

 # 条件8
condition8 = {
    'AA_6':5,
    'milliQ':1,
    'Mg_80':2,
    'K_1600':1,
    'SPD_11':1,
    'NTP_25':1,
    '3PGA_600':1,
    'PEG':1,
    'mixture':1,
    'DNA':1,
    'cell_extract':5,
    }

 # 条件9
condition9 = {
    'AA_6':5,
    'milliQ':1,
    'Mg_80':2,
    'K_1600':1,
    'SPD_2':1,
    'NTP_25':1,
    '3PGA_600':1,
    'PEG':1,
    'mixture':1,
    'DNA':1,
    'cell_extract':5,
    }

# 条件10
condition10 = {
    'AA_6':5,
    'milliQ':1,
    'Mg_80':2,
    'K_1600':1,
    'SPD_20':1,
    'NTP_14':1,
    '3PGA_600':1,
    'PEG':1,
    'mixture':1,
    'DNA':1,
    'cell_extract':5,
    }

# 条件11
condition11 = {
    'AA_6':5,
    'milliQ':1,
    'Mg_80':2,
    'K_1600':1,
    'SPD_20':1,
    'NTP_3':1,
    '3PGA_600':1,
    'PEG':1,
    'mixture':1,
    'DNA':1,
    'cell_extract':5,
    }

# 条件12
condition12 = {
    'AA_6':5,
    'milliQ':1,
    'Mg_80':2,
    'K_1600':1,
    'SPD_20':1,
    'NTP_25':1,
    '3PGA_330':1,
    'PEG':1,
    'mixture':1,
    'DNA':1,
    'cell_extract':5,
    }

# 条件13
condition13 = {
    'AA_6':5,
    'milliQ':1,
    'Mg_80':2,
    'K_1600':1,
    'SPD_20':1,
    'NTP_25':1,
    '3PGA_60':1,
    'PEG':1,
    'mixture':1,
    'DNA':1,
    'cell_extract':5,
    }


# ネガティブコントロール
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

# 各条件を入れるウェルを指定する
well_num = {
    'condition1': 'B2',
    'condition2': 'B3',
    'condition3': 'B4',
    'condition4': 'B5',
    'condition5': 'B6',
    'condition6': 'B7',
    'condition7': 'B8',
    'condition8': 'B9',
    'condition9': 'B10',
    'condition10': 'B11',
    'condition11': 'B12',
    'condition12': 'B13',
    'condition13': 'B14',
    'negative_control1': 'B15',
    'negative_control2': 'B16',
}

# 各条件の文字列と辞書型の変数を対応させる
conditions = {
    'condition1': condition1,
    'condition2': condition2,
    'condition3': condition3,
    'condition4': condition4,
    'condition5': condition5,
    'condition6': condition6,
    'condition7': condition7,
    'condition8': condition8,
    # 'condition9': condition9,
    # 'condition10': condition10,
    # 'condition11': condition11,
    # 'condition12': condition12,
    # 'condition13': condition13,
    # 'negative_control1': negative_control,
    # 'negative_control2': negative_control,
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
    right_pipette.starting_tip = right_tip_rack['E4']

    # 分注させるためのコード
    for k,v in conditions.items():
        # ex.)k='conditiion1', v={'AA_6':5, 'milliQ':1, 'Mg_80':2, 'K_1600':1, 'SPD_20':1, 'NTP_25':1, '3PGA_600':1, 'PEG':1, 'mixture':1, 'DNA':1, 'cell_extract':5}
        
        for key,value in v.items():
            # ex.) key='AA_6', value=5
            
            # アミノ酸を入れる前にはピペッティングする
                if 'AA' in key :
                    pipetting_volume = tube_volume[key]*0.9
                    if pipetting_volume <= 20:
                        left_pipette.pick_up_tip()
                        left_pipette.mix(5, pipetting_volume, tube_rack[tube_data[key]])
                        left_pipette.drop_tip()
                    else:
                        right_pipette.pick_up_tip()
                        right_pipette.mix(5, pipetting_volume, tube_rack[tube_data[key]])
                        right_pipette.drop_tip()

                    left_pipette.transfer(int(value), tube_rack[tube_data[key]], well_plate_384[well_num[k]], new_tip='always')
                    tube_volume[key] -= int(value)


                # 細胞抽出液を入れる前にはピペッティングする
                elif key == 'cell_extract':
                    pipetting_volume = tube_volume[key]*0.7
                    if pipetting_volume <= 20:
                        left_pipette.pick_up_tip()
                        left_pipette.mix(5, pipetting_volume, tube_rack[tube_data[key]])
                        left_pipette.drop_tip()
                    else:
                        right_pipette.pick_up_tip()
                        right_pipette.mix(5, pipetting_volume, tube_rack[tube_data[key]])
                        right_pipette.drop_tip()

                    left_pipette.transfer(int(value), tube_rack[tube_data[key]], well_plate_384[well_num[k]], new_tip='always')
                    tube_volume[key] -= int(value)

                else:
                    left_pipette.transfer(int(value), tube_rack[tube_data[key]], well_plate_384[well_num[k]], new_tip='always')
        


    print(tube_volume)
            
            
    # 最後に全セルをピペッティングする
    for k,v in conditions.items():
        left_pipette.pick_up_tip()
        left_pipette.mix(5, 10, well_plate_384[well_num[k]])
        left_pipette.drop_tip()
    