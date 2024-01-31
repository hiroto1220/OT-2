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

# 各条件
condition1={'AA_4.15': 4, 'milliQ': 2.0, 'Mg_44': 2, 'K_1600': 1, 'SPD_20': 1, 'NTP_14': 1, '3PGA_600': 1, 'PEG': 1, 'mixture': 1, 'DNA': 1, 'cell_extract': 5}
condition2={'AA_6': 5, 'milliQ': 1.0, 'Mg_80': 2, 'K_1600': 1, 'SPD_20': 1, 'NTP_14': 1, '3PGA_600': 1, 'PEG': 1, 'mixture': 1, 'DNA': 1, 'cell_extract': 5}
condition3={'AA_4.15': 4, 'milliQ': 2.0, 'Mg_80': 2, 'K_1600': 1, 'SPD_20': 1, 'NTP_14': 1, '3PGA_330': 1, 'PEG': 1, 'mixture': 1, 'DNA': 1, 'cell_extract': 5}
condition4={'AA_6': 5, 'milliQ': 1.0, 'Mg_80': 2, 'K_1600': 1, 'SPD_20': 1, 'NTP_14': 1, '3PGA_330': 1, 'PEG': 1, 'mixture': 1, 'DNA': 1, 'cell_extract': 5}
condition5={'AA_6': 5, 'milliQ': 1.0, 'Mg_44': 2, 'K_1600': 1, 'SPD_20': 1, 'NTP_14': 1, '3PGA_330': 1, 'PEG': 1, 'mixture': 1, 'DNA': 1, 'cell_extract': 5}
condition6={'AA_4.15': 4, 'milliQ': 2.0, 'Mg_44': 2, 'K_1600': 1, 'SPD_20': 1, 'NTP_14': 1, '3PGA_330': 1, 'PEG': 1, 'mixture': 1, 'DNA': 1, 'cell_extract': 5}
condition7={'AA_4.15': 4, 'milliQ': 2.0, 'Mg_80': 2, 'K_1600': 1, 'SPD_11': 1, 'NTP_14': 1, '3PGA_600': 1, 'PEG': 1, 'mixture': 1, 'DNA': 1, 'cell_extract': 5}
condition8={'AA_6': 5, 'milliQ': 1.0, 'Mg_80': 2, 'K_1600': 1, 'SPD_11': 1, 'NTP_14': 1, '3PGA_600': 1, 'PEG': 1, 'mixture': 1, 'DNA': 1, 'cell_extract': 5}
condition9={'AA_6': 5, 'milliQ': 1.0, 'Mg_80': 2, 'K_1600': 1, 'SPD_11': 1, 'NTP_14': 1, '3PGA_330': 1, 'PEG': 1, 'mixture': 1, 'DNA': 1, 'cell_extract': 5}
condition10={'AA_6': 5, 'milliQ': 1.0, 'Mg_44': 2, 'K_1600': 1, 'SPD_11': 1, 'NTP_14': 1, '3PGA_600': 1, 'PEG': 1, 'mixture': 1, 'DNA': 1, 'cell_extract': 5}
condition11={'AA_6': 5, 'milliQ': 1.0, 'Mg_44': 2, 'K_1600': 1, 'SPD_11': 1, 'NTP_14': 1, '3PGA_330': 1, 'PEG': 1, 'mixture': 1, 'DNA': 1, 'cell_extract': 5}
condition12={'AA_4.15': 4, 'milliQ': 2.0, 'Mg_80': 2, 'K_1600': 1, 'SPD_11': 1, 'NTP_14': 1, '3PGA_330': 1, 'PEG': 1, 'mixture': 1, 'DNA': 1, 'cell_extract': 5}
condition13={'AA_4.15': 4, 'milliQ': 2.0, 'Mg_44': 2, 'K_1600': 1, 'SPD_11': 1, 'NTP_14': 1, '3PGA_600': 1, 'PEG': 1, 'mixture': 1, 'DNA': 1, 'cell_extract': 5}
condition14={'AA_4.15': 4, 'milliQ': 2.0, 'Mg_44': 2, 'K_1600': 1, 'SPD_11': 1, 'NTP_14': 1, '3PGA_330': 1, 'PEG': 1, 'mixture': 1, 'DNA': 1, 'cell_extract': 5}
condition15={'AA_4.15': 4, 'milliQ': 2.0, 'Mg_80': 2, 'K_1600': 1, 'SPD_20': 1, 'NTP_25': 1, '3PGA_600': 1, 'PEG': 1, 'mixture': 1, 'DNA': 1, 'cell_extract': 5}
condition16={'AA_6': 5, 'milliQ': 1.0, 'Mg_80': 2, 'K_1600': 1, 'SPD_20': 1, 'NTP_25': 1, '3PGA_600': 1, 'PEG': 1, 'mixture': 1, 'DNA': 1, 'cell_extract': 5}
condition17={'AA_6': 5, 'milliQ': 1.0, 'Mg_80': 2, 'K_1600': 1, 'SPD_20': 1, 'NTP_25': 1, '3PGA_330': 1, 'PEG': 1, 'mixture': 1, 'DNA': 1, 'cell_extract': 5}
condition18={'AA_6': 5, 'milliQ': 1.0, 'Mg_80': 2, 'K_1600': 1, 'SPD_20': 1, 'NTP_3': 1, '3PGA_600': 1, 'PEG': 1, 'mixture': 1, 'DNA': 1, 'cell_extract': 5}
condition19={'AA_6': 5, 'milliQ': 1.0, 'Mg_80': 2, 'K_1600': 1, 'SPD_20': 1, 'NTP_3': 1, '3PGA_330': 1, 'PEG': 1, 'mixture': 1, 'DNA': 1, 'cell_extract': 5}
condition20={'AA_6': 5, 'milliQ': 1.0, 'Mg_80': 2, 'K_1600': 1, 'SPD_11': 1, 'NTP_25': 1, '3PGA_600': 1, 'PEG': 1, 'mixture': 1, 'DNA': 1, 'cell_extract': 5}
condition21={'AA_6': 5, 'milliQ': 1.0, 'Mg_80': 2, 'K_1600': 1, 'SPD_11': 1, 'NTP_25': 1, '3PGA_330': 1, 'PEG': 1, 'mixture': 1, 'DNA': 1, 'cell_extract': 5}
condition22={'AA_6': 5, 'milliQ': 1.0, 'Mg_80': 2, 'K_1600': 1, 'SPD_11': 1, 'NTP_3': 1, '3PGA_600': 1, 'PEG': 1, 'mixture': 1, 'DNA': 1, 'cell_extract': 5}
condition23={'AA_6': 5, 'milliQ': 1.0, 'Mg_80': 2, 'K_1600': 1, 'SPD_11': 1, 'NTP_3': 1, '3PGA_330': 1, 'PEG': 1, 'mixture': 1, 'DNA': 1, 'cell_extract': 5}
condition24={'AA_6': 5, 'milliQ': 1.0, 'Mg_44': 2, 'K_1600': 1, 'SPD_20': 1, 'NTP_25': 1, '3PGA_600': 1, 'PEG': 1, 'mixture': 1, 'DNA': 1, 'cell_extract': 5}
condition25={'AA_6': 5, 'milliQ': 1.0, 'Mg_44': 2, 'K_1600': 1, 'SPD_20': 1, 'NTP_25': 1, '3PGA_330': 1, 'PEG': 1, 'mixture': 1, 'DNA': 1, 'cell_extract': 5}
condition26={'AA_6': 5, 'milliQ': 1.0, 'Mg_44': 2, 'K_1600': 1, 'SPD_20': 1, 'NTP_3': 1, '3PGA_600': 1, 'PEG': 1, 'mixture': 1, 'DNA': 1, 'cell_extract': 5}
condition27={'AA_6': 5, 'milliQ': 1.0, 'Mg_44': 2, 'K_1600': 1, 'SPD_20': 1, 'NTP_3': 1, '3PGA_330': 1, 'PEG': 1, 'mixture': 1, 'DNA': 1, 'cell_extract': 5}
condition28={'AA_6': 5, 'milliQ': 1.0, 'Mg_44': 2, 'K_1600': 1, 'SPD_11': 1, 'NTP_25': 1, '3PGA_600': 1, 'PEG': 1, 'mixture': 1, 'DNA': 1, 'cell_extract': 5}
condition29={'AA_6': 5, 'milliQ': 1.0, 'Mg_44': 2, 'K_1600': 1, 'SPD_11': 1, 'NTP_25': 1, '3PGA_330': 1, 'PEG': 1, 'mixture': 1, 'DNA': 1, 'cell_extract': 5}
condition30={'AA_6': 5, 'milliQ': 1.0, 'Mg_44': 2, 'K_1600': 1, 'SPD_11': 1, 'NTP_3': 1, '3PGA_600': 1, 'PEG': 1, 'mixture': 1, 'DNA': 1, 'cell_extract': 5}

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

# ポジティブコントロール
positive_control = {
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
    'condition14': 'B15',
    'condition15': 'B16',
    'condition16': 'B17',
    'condition17': 'B18',
    'condition18': 'B19',
    'condition19': 'B20',
    'condition20': 'B21',
    'condition21': 'B22',
    'condition22': 'B23',
    'condition23': 'C2',
    'condition24': 'C3',
    'condition25': 'C4',
    'condition26': 'C5',
    'condition27': 'C6',
    'condition28': 'C7',
    'condition29': 'C8',
    'condition30': 'C9',
    'positive_control_1': 'C10',
    'positive_control_2': 'C11',
    'positive_control_3': 'C12',
    'negative_control': 'C13',
}



#========================================================================================================================================================================
# 各条件の文字列と辞書型の変数を対応させる

conditions = {
    'positive_control_1': positive_control,
    'positive_control_2': positive_control,
    'positive_control_3': positive_control,
    'condition1': condition1,
    'condition2': condition2,
    'condition3': condition3,
    'condition4': condition4,
    'condition5': condition5,
    'condition6': condition6,
    'condition7': condition7,
    'condition8': condition8,
    'condition9': condition9,
    'condition10': condition10,
    'condition11': condition11,
    'condition12': condition12,
    'condition13': condition13,
    'condition14': condition14,
    'condition15': condition15,
    'condition16': condition16,
    'condition17': condition17,
    'condition18': condition18,
    'condition19': condition19,
    'condition20': condition20,
    'condition21': condition21,
    'condition22': condition22,
    'condition23': condition23,
    'condition24': condition24,
    'condition25': condition25,
    'condition26': condition26,
    'condition27': condition27,
    'condition28': condition28,
    'condition29': condition29,
    'condition30': condition30,
    'negative_control': negative_control,
}


# 各チューブの残量を記録する
tube_volume = {
    'AA_6': 140,
    'AA_4.15': 42,
    'AA_0.6': 0,
    'cell_extract': 200,
}


#========================================================================================================================================================================



    
# 2023/10/20 OT-2で無細胞系の発現を安定させる①
def run(protocol: protocol_api.ProtocolContext):
    tip_rack_p20 = protocol.load_labware('opentrons_96_tiprack_20ul', 10)
    tip_rack_p20_2 = protocol.load_labware('opentrons_96_tiprack_20ul', 11)
    tip_rack_p20_3 = protocol.load_labware('opentrons_96_tiprack_20ul', 7)
    tip_rack_p20_4 = protocol.load_labware('opentrons_96_tiprack_20ul', 8)
    tip_rack_p20_5 = protocol.load_labware('opentrons_96_tiprack_20ul', 5)

    tip_rack_p300 = protocol.load_labware('opentrons_96_tiprack_300ul', 9)
    # tip_rack_p300_2 = protocol.load_labware('opentrons_96_tiprack_300ul', 6)

    tube_rack = protocol.load_labware('opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap', 1)
    well_plate_384 = protocol.load_labware('corning_384_wellplate_112ul_flat', 2)


    left_pipette = protocol.load_instrument('p20_single_gen2', 'left', tip_racks=[tip_rack_p20,tip_rack_p20_2,tip_rack_p20_3,tip_rack_p20_4,tip_rack_p20_5])
    left_pipette.starting_tip = tip_rack_p20['A3']
    
    right_pipette = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=[tip_rack_p300])
    right_pipette.starting_tip = tip_rack_p300['B3']

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
                    if tube_volume[key]>100:
                        pipetting_volume = tube_volume[key]*0.5
                    else:
                        pipetting_volume = tube_volume[key]*0.3
                    if pipetting_volume <= 20:
                        left_pipette.pick_up_tip()
                        left_pipette.mix(5, pipetting_volume, tube_rack[tube_data[key]],rate=0.5)
                        left_pipette.drop_tip()
                    else:
                        right_pipette.pick_up_tip()
                        right_pipette.mix(5, pipetting_volume, tube_rack[tube_data[key]],rate=0.5)
                        right_pipette.drop_tip()

                    left_pipette.transfer(int(value), tube_rack[tube_data[key]], well_plate_384[well_num[k]], new_tip='always')
                    tube_volume[key] -= int(value)

                else:
                    left_pipette.transfer(int(value), tube_rack[tube_data[key]], well_plate_384[well_num[k]], new_tip='always')
        

            
    # 最後に全セルをピペッティングする
    for k,v in conditions.items():
        left_pipette.pick_up_tip()
        left_pipette.mix(5, 10, well_plate_384[well_num[k]])
        left_pipette.drop_tip()
    