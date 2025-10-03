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
    FireballCalculation,
    VesselCatastrophicRuptureCalculation,
    VesselStateCalculation,
)
from pypws.entities import (
    DischargeParameters,
    Material,
    MaterialComponent,
    State,
    Vessel,
    Weather,
)
from pypws.enums import AtmosphericStabilityClass, ResultCode, VesselShape


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

    # Create a vessel catastrophic rupture calculation based on the vessel and discharge parameters
    vessel_catastrophic_rupture_calculation = VesselCatastrophicRuptureCalculation(vessel, discharge_parameters)

    # Run the calculation
    print('Running vessel_catastrophic_rupture_calculation...')
    resultCode = vessel_catastrophic_rupture_calculation.run()

    # Print any messages.
    if len(vessel_catastrophic_rupture_calculation.messages) > 0:
        print('Messages:')
        for message in vessel_catastrophic_rupture_calculation.messages:
            print(message)

    if resultCode == resultCode.SUCCESS:
        print(f'SUCCESS: vessel_catastrophic_rupture_calculation ({vessel_catastrophic_rupture_calculation.calculation_elapsed_time}ms)')
    else:
        assert False, f'FAILED vessel_catastrophic_rupture_calculation with result code {resultCode}'

    exit_material = vessel_catastrophic_rupture_calculation.exit_material

    # Define the weather.
    weather = Weather(wind_speed = 1.5, stability_class = AtmosphericStabilityClass.STABILITY_F)

    # Create a fireball calculation based on the vessel catastrophic rupture calculation and weather.
    fireball_calculation = FireballCalculation(discharge_records = vessel_catastrophic_rupture_calculation.discharge_records, discharge_record_count = len(vessel_catastrophic_rupture_calculation.discharge_records), discharge_result = vessel_catastrophic_rupture_calculation.discharge_result, weather = weather, material = exit_material, state = state)

    # Run the calculation
    print('Running fireball_calculation...')
    resultCode = fireball_calculation.run()

    # Print any messages.
    if len(fireball_calculation.messages) > 0:
        print('Messages:')
        for message in fireball_calculation.messages:
            print(message)

    if resultCode == resultCode.SUCCESS:
        # check whether flame_diameter is a number and not zero
        if not isinstance(fireball_calculation.flame_result.flame_diameter, (int, float)) or fireball_calculation.flame_result.flame_diameter == 0:
            assert False, f'Regression failed with fireball_calculation.flame_result.flame_diameter = {fireball_calculation.flame_result.flame_diameter}'
        print(f'SUCCESS: fireball_calculation ({fireball_calculation.calculation_elapsed_time}ms)')
    else:
        assert False, f'FAILED fireball_calculation with result code {resultCode}'

