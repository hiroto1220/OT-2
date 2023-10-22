# tutorial: https://docs.opentrons.com/v2/tutorial.html

from opentrons import protocol_api

metadata = {
    'protocolName': 'Test Protocol',
    'apiLevel': '2.11'
}

# def run(protocol: protocol_api.ProtocolContext):
#     plate = protocol.load_labware('corning_96_wellplate_360ul_flat', 5)
#     tiprack = protocol.load_labware('opentrons_96_tiprack_300ul', 11)
#     pipette = protocol.load_instrument('p300_single', 'right', tip_racks=[tiprack])
#     pipette.pick_up_tip()
#     pipette.aspirate(100, plate['A1'])
#     pipette.dispense(100, plate['A2'])
#     pipette.drop_tip()

# ピペットの開始位置を指定する
# def run(protocol: protocol_api.ProtocolContext):
#    rack = protocol.load_labware('opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap', 7)
#    tiprack = protocol.load_labware('opentrons_96_tiprack_20ul', 10)

#    pipette = protocol.load_instrument('p20_single_gen2', 'left', tip_racks=[tiprack])
   

#    pipette.pick_up_tip(tiprack['A4'])

#    for _ in range(2):
#         pipette.transfer(1, rack['A1'], rack['A2'], new_tip='never')
        
#    pipette.drop_tip()

# ピペッティングする
def run(protocol: protocol_api.ProtocolContext):
    left_tip_rack = protocol.load_labware('opentrons_96_tiprack_20ul', 10)
    right_tip_rack = protocol.load_labware('opentrons_96_tiprack_300ul', 11)
    tube_rack = protocol.load_labware('opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap', 4)
    well_plate_384 = protocol.load_labware('corning_384_wellplate_112ul_flat', 5)
    

    #ピペットは p20
    left_pipette = protocol.load_instrument('p20_single_gen2', 'left', tip_racks=[left_tip_rack])
    left_pipette.starting_tip = left_tip_rack['F1']

    right_pipette = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=[right_tip_rack])

    left_pipette.pick_up_tip(left_tip_rack['G1'])
    left_pipette.mix(5, 10, well_plate_384['B2'])
    left_pipette.drop_tip()
    # left_pipette.transfer(1, tube_rack['A1'], tube_rack['A2'], new_tip='always')