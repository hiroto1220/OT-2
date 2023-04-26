from opentrons import protocol_api

metadata = {
    'protocolName': 'Test Protocol',
    'apiLevel': '2.13'
}

def run(protocol: protocol_api.ProtocolContext):
    plate = protocol.load_labware('corning_96_wellplate_360ul_flat', 2)
    tiprack = protocol.load_labware('opentrons_96_tiprack_300ul', 1)
    pipette = protocol.load_instrument('p300_single', 'left', tip_racks=[tiprack])
    pipette.pick_up_tip()
    pipette.aspirate(100, plate['A1'])
    pipette.dispense(100, plate['A2'])
    pipette.drop_tip()