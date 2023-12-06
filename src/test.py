from opentrons import protocol_api

metadata = {
    'protocolName': 'Test Protocol',
    'apiLevel': '2.11'
}

# チューブラックに設置するする各溶液の種類・濃度とチューブの位置を決める
tube_data = {
    'AA_6': 'A1',
    'Mg_80': 'A2',
    'Mg_44': 'A3',
    'K_1600': 'A4',
    'SPD_20': 'A5',
    'NTP_25': 'A6',
    '3PGA_600': 'B1',
    'PEG': 'B2',
    'milliQ': 'B3',
    'mixture': 'B4',
    'DNA': 'B5',
    'cell_extract': 'B6',
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



# 分注先の番号
tube_num = {
    'condition1': 'B2',
    'condition2': 'B3',
}

# 各条件の文字列と辞書型の変数を対応させる
conditions = {
    'condition1': condition1,
    'condition2': condition2,
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
        
            # left_pipette.transfer(吸ってほしい量, チューブラックのどこに行って欲しいか, どこにはいて欲しいか, チップの取り替え方法)
            left_pipette.transfer(int(value), tube_rack[tube_data[key]], tube_rack[tube_num[k]], new_tip='always')

    