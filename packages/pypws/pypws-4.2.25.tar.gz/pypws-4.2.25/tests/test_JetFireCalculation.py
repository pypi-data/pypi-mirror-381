import os
import pathlib
import sys

# When running locally the environment variable RUN_LOCALLY needs to be set to True.
# Check if the environment variable is set
if os.getenv('PYPWS_RUN_LOCALLY') != None and os.getenv('PYPWS_RUN_LOCALLY').lower() == 'true':
    # Navigate to the PYPWS directory by searching upwards until it is found.
    current_dir = pathlib.Path(__file__).resolve()

    while current_dir.name.lower() != 'package':
        current_dir = current_dir.parent

    # Insert the path to the pypws package into sys.path.
    sys.path.insert(0, f'{current_dir}')

from pypws.calculations import (
    JetFireCalculation,
    VesselLeakCalculation,
    VesselStateCalculation,
)
from pypws.entities import (
    DischargeParameters,
    FlammableParameters,
    Leak,
    Material,
    MaterialComponent,
    State,
    Substrate,
    Vessel,
    Weather,
)
from pypws.enums import (
    AtmosphericStabilityClass,
    ResultCode,
    TimeVaryingOption,
    VesselShape,
)

"""
This sample demonstrates how to use the vessel leak calculation along with with the dependent entities.
"""

def test():

    """
    Jet fire calculation test case with the following properties:

        material_name = 'METHANE'
        state_temperature = 280.0
        state_pressure = 1.0E+06
        vessel_shape = VesselShape.VESSEL_SPHERE
        vessel_diameter = 3.0
        leak_hole_diameter = 0.1
        time_varying_option = TimeVaryingOption.INITIAL_RATE
        leak_hole_height_fraction = 0.5
        wind_speed = 2.0
        stability_class = STABILITY_F
        surface_roughness = 0.18
        time_of_interest = 10.0
    """

    # Set the case properties.
    material_name = 'METHANE'
    state_temperature = 280.0
    state_pressure = 1.0E+06
    vessel_shape = VesselShape.VESSEL_SPHERE
    vessel_diameter = 3.0
    leak_hole_diameter = 0.1
    time_varying_option = TimeVaryingOption.INITIAL_RATE
    leak_hole_height_fraction = 0.5
    wind_speed = 2.0
    stability_class = AtmosphericStabilityClass.STABILITY_F
    surface_roughness = 0.18
    time_of_interest = 10.0

    # Define the initial state of the vessel.
    state = State(temperature = state_temperature, pressure = state_pressure, liquid_fraction = 0.0)

    # Define the material contained by the vessel.
    material = Material(material_name, [MaterialComponent(material_name, 1.0)])

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

    # Create a vessel to use in the leak calculation using the previously defined entities.
    # The vessel is a horizontal cylinder with a diameter of 8m and a length of 16m.
    # All other values are defaulted.
    vessel = Vessel(state = vessel_state_calculation.output_state, material = vessel_state_calculation.material, vessel_conditions = vessel_state_calculation.vessel_conditions, diameter = vessel_diameter, shape = vessel_shape, liquid_fill_fraction_by_volume=0.0)

    # Create a leak to use in the vessel leak calculation.
    # The leak has a hole of diameter of 0.05m.  The time varying option is set topytest initial rate.
    leak = Leak(hole_diameter = leak_hole_diameter, hole_height_fraction = leak_hole_height_fraction , time_varying_option = time_varying_option)

    # Create discharge parameters to use in the vessel leak calculation taking all the default values.
    discharge_parameters = DischargeParameters()

    # Create a vessel leak calculation using the vessel, leak, and discharge parameters.
    vessel_leak_calculation = VesselLeakCalculation(vessel, leak, discharge_parameters)

    # Run the vessel leak calculation.
    print('Running vessel_leak_calculation...')
    resultCode = vessel_leak_calculation.run()

    # Print any messages.
    if len(vessel_leak_calculation.messages) > 0:
        print('Messages:')
        for message in vessel_leak_calculation.messages:
            print(message)

    if resultCode == ResultCode.SUCCESS:
        print(f'SUCCESS: vessel_leak_calculation ({vessel_leak_calculation.calculation_elapsed_time}ms)')
    else:
        assert False, f'FAILED vessel_leak_calculation with result code {resultCode}'

    # Instantiate the data required by the jet fire calculation.
    weather = Weather(wind_speed = wind_speed, stability_class = stability_class)
    substrate = Substrate(surface_roughness = surface_roughness)
    flammable_parameters = FlammableParameters(time_of_interest = time_of_interest)

    # Create a jet fire calculation using the required input data.
    jet_fire_calculation = JetFireCalculation(vessel_leak_calculation.exit_material, vessel_leak_calculation.discharge_records, len(vessel_leak_calculation.discharge_records), vessel_leak_calculation.discharge_result, weather, substrate, flammable_parameters)

    # Run the jet fire calculation.
    print('Running jet_fire_calculation...')
    resultCode = jet_fire_calculation.run()

    # Print any messages.
    if len(jet_fire_calculation.messages) > 0:
        print('Messages:')
        for message in jet_fire_calculation.messages:
            print(message)

    if resultCode == ResultCode.SUCCESS: 
        # check whether flame_length is a number and not zero
        if not isinstance(jet_fire_calculation.flame_result.flame_length, (int, float)) or jet_fire_calculation.flame_result.flame_length == 0:
            assert False, f'Regression failed with jet_fire_calculation.flame_result.flame_length = {jet_fire_calculation.flame_result.flame_length}'  
        
        # check whether surface_emissive_power is a number and not zero
        if not isinstance(jet_fire_calculation.flame_result.surface_emissive_power, (int, float)) or jet_fire_calculation.flame_result.surface_emissive_power == 0:
            assert False, f'Regression failed with jet_fire_calculation.flame_result.surface_emissive_power = {jet_fire_calculation.flame_result.surface_emissive_power}'
        
        # check whether there are 2 flame records
        if (len(jet_fire_calculation.flame_records) != 2):
            assert False,f'Regression failed with len(jet_fire_calculation.flame_records) = {len(jet_fire_calculation.flame_records)}'

        print(f'SUCCESS: jet_fire_calculation ({jet_fire_calculation.calculation_elapsed_time}ms)')
    else:
        assert False, f'FAILED jet_fire_calculation with result code {resultCode}'