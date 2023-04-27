from opentrons import protocol_api

metadata = {
    'protocolName': 'Test Protocol',
    'apiLevel': '2.11'
}

# 20ul*50
# def run(protocol: protocol_api.ProtocolContext):
#    rack = protocol.load_labware('opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap', 7)
#    tiprack = protocol.load_labware('opentrons_96_tiprack_20ul', 10)

#    pipette = protocol.load_instrument('p20_single_gen2', 'left', tip_racks=[tiprack])

#    pipette.pick_up_tip()

#    for _ in range(50):
#         pipette.transfer(20, rack['A1'], rack['A2'], new_tip='never')
        
#    pipette.drop_tip()


# 1ul*100
# def run(protocol: protocol_api.ProtocolContext):
#    rack = protocol.load_labware('opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap', 7)
#    tiprack = protocol.load_labware('opentrons_96_tiprack_300ul', 10)

#    pipette = protocol.load_instrument('p20_single_gen2', 'left', tip_racks=[tiprack])

#    pipette.pick_up_tip(tiprack['A2'])

#    for _ in range(100):
#         pipette.transfer(1, rack['A1'], rack['A2'], new_tip='never')
        
#    pipette.drop_tip()

# # 20ul*50
# def run(protocol: protocol_api.ProtocolContext):
#     rack = protocol.load_labware('opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap', 7)
#     tiprack = protocol.load_labware('opentrons_96_tiprack_300ul', 11)
#     pipette = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=[tiprack])
#     pipette.pick_up_tip()

#     for _ in range(50):
#         pipette.transfer(20, rack['A1'], rack['A2'], new_tip='never')
        
#     pipette.drop_tip()

# 300ul*4
def run(protocol: protocol_api.ProtocolContext):
    rack = protocol.load_labware('opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap', 7)
    tiprack = protocol.load_labware('opentrons_96_tiprack_300ul', 11)
    pipette = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=[tiprack])
    pipette.pick_up_tip()

    for _ in range(4):
        pipette.transfer(300, rack['A1'], rack['A2'], new_tip='never')
        
    pipette.drop_tip()