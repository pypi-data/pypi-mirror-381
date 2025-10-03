import os
import pathlib
import sys

run_locally = os.getenv('PYPWS_RUN_LOCALLY')
if run_locally and run_locally.lower() == 'true':
    # Navigate to the PYPWS directory by searching upwards until it is found.
    current_dir = pathlib.Path(__file__).resolve()

    while current_dir.name.lower() != 'package':
        if current_dir.parent == current_dir:  # Check if the current directory is the root directory
            raise FileNotFoundError("The 'pypws' directory was not found in the path hierarchy.")
        current_dir = current_dir.parent

    # Insert the path to the pypws package into sys.path.
    sys.path.insert(0, f'{current_dir}')

from pypws.calculations import (
    VesselCatastrophicRuptureCalculation,
    VesselStateCalculation,
)
from pypws.entities import (
    DischargeParameters,
    Material,
    MaterialComponent,
    State,
    Vessel,
)
from pypws.enums import ResultCode, VesselShape


def test():
    material = Material("AMMONIA", [MaterialComponent("AMMONIA", 1.0)])
    state = State(temperature=250.0, pressure= 5.0e6, liquid_fraction=0.8)

    # Create a vessel state calculation using the material and state.
    vessel_state_calculation = VesselStateCalculation(material, state)

    # Run the vessel state calculation.
    print('Running vessel_state_calculation...')
    resultCode = vessel_state_calculation.run()

    # Print any messages.
    if len(vessel_state_calculation.messages) > 0:
        print('Messages:')
        for message in vessel_state_calculation.messages:
            print(message)

    if resultCode == ResultCode.SUCCESS:
        print(f'SUCCESS: vessel_state_calculation ({vessel_state_calculation.calculation_elapsed_time}ms)')
    else:
        assert False, f'FAILED vessel_state_calculation with result code {resultCode}'

    vessel = Vessel(state=state,
                    material=material,
                    liquid_fill_fraction_by_volume=0.8,
                    diameter=2.0,
                    length=5,
                    shape=VesselShape.HORIZONTAL_CYLINDER,
                    vessel_conditions = vessel_state_calculation.vessel_conditions
                    )

    discharge_parameters = DischargeParameters()

    vessel_catastrophic_rupture_calculation = VesselCatastrophicRuptureCalculation(vessel, discharge_parameters)

    print('Running vessel_catastrophic_rupture_calculation...')
    resultCode = vessel_catastrophic_rupture_calculation.run()

    # Print any messages.
    if len(vessel_catastrophic_rupture_calculation.messages) > 0:
        print('Messages:')
        for message in vessel_catastrophic_rupture_calculation.messages:
            print(message)

    if resultCode == resultCode.SUCCESS:
        # check whether the release_mass is a number and not zero
        if not isinstance(vessel_catastrophic_rupture_calculation.discharge_result.release_mass, (int, float)) or vessel_catastrophic_rupture_calculation.discharge_result.release_mass == 0:
            assert False, f'Regression failed with vessel_catastrophic_rupture_calculation.discharge_result.release_mass = {vessel_catastrophic_rupture_calculation.discharge_result.release_mass}'
        
        # check whether the expansion_energy is a number and not zero
        if not isinstance(vessel_catastrophic_rupture_calculation.discharge_result.expansion_energy, (int, float)) or vessel_catastrophic_rupture_calculation.discharge_result.expansion_energy == 0:
            assert False, f'Regression failed with vessel_catastrophic_rupture_calculation.discharge_result.expansion_energy = {vessel_catastrophic_rupture_calculation.discharge_result.expansion_energy}'
        
        print(f'SUCCESS: vessel_catastrophic_rupture_calculation ({vessel_catastrophic_rupture_calculation.calculation_elapsed_time}ms)')
    else:
        assert False, f'FAILED vessel_catastrophic_rupture_calculation with result code {resultCode}'