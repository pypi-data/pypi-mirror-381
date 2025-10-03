import os
import pathlib
import sys

# When running locally the environment variable PYPWS_RUN_LOCALLY needs to be set to True.
# Check if the environment variable is set
if os.getenv('PYPWS_RUN_LOCALLY') != None and os.getenv('PYPWS_RUN_LOCALLY').lower() == 'true':
    # Navigate to the PYPWS directory by searching upwards until it is found.
    current_dir = pathlib.Path(__file__).resolve()

    while current_dir.name.lower() != 'package':
        current_dir = current_dir.parent

    # Insert the path to the pypws package into sys.path.
    sys.path.insert(0, f'{current_dir}')

from pypws.calculations import (
    VesselLeakMaxFlammableCloudCalculation,
    VesselStateCalculation,
)
from pypws.entities import (
    DischargeParameters,
    DispersionOutputConfig,
    DispersionParameters,
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
    Resolution,
    ResultCode,
    SpecialConcentration,
    SurfaceType,
    TimeVaryingOption,
    VesselShape,
    WindProfileFlag
)

"""
This sample demonstrates how to use the vessel leak maximum flammable cloud calculation along with with the dependent entities.
"""

def test():

        # Set the case properties.
    material_name = 'METHANE'
    state_temperature = 280.0
    state_pressure = 1.0E+06
    vessel_shape = VesselShape.VESSEL_SPHERE
    vessel_diameter = 3.0
    leak_hole_diameter = 0.1
    time_varying_option = TimeVaryingOption.INITIAL_RATE
    leak_hole_height_fraction = 0.5

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

    # Define the weather
    weather = Weather(wind_speed = 2.0, stability_class = AtmosphericStabilityClass.STABILITY_F, wind_profile_flag = WindProfileFlag.LOGARITHMIC_PROFILE)

    # Define the substrate
    substrate = Substrate(surface_roughness = 0.05, surface_type = SurfaceType.WATER)

    # Define the dispersion parameters
    dispersion_parameters = DispersionParameters()

    # Define the dispersion output configuration
    dispersion_output_config = DispersionOutputConfig(special_concentration = SpecialConcentration.LFL, resolution = Resolution.MEDIUM, time = 5)

    # Create the vessel leak maximum flammable cloud calculation using the previously defined entities.
    vessel_leak_max_flammable_cloud_calculation = VesselLeakMaxFlammableCloudCalculation(vessel=vessel, leak=leak, discharge_parameters=discharge_parameters, weather=weather, substrate=substrate, dispersion_parameters=dispersion_parameters, dispersion_output_config=dispersion_output_config)

    # Run the calculation.
    print('Running vessel_leak_max_flammable_cloud_calculation...')
    resultCode = vessel_leak_max_flammable_cloud_calculation.run()

    # Print any messages.
    if len(vessel_leak_max_flammable_cloud_calculation.messages) > 0:
        print('Messages:')
        for message in vessel_leak_max_flammable_cloud_calculation.messages:
            print(message)

    if resultCode == ResultCode.SUCCESS:
        # check that the phase is 1
        if (vessel_leak_max_flammable_cloud_calculation.vessel_leak_max_flammable_cloud_results.phase != 1):
            assert False,f'Regression failed with vessel_leak_max_flammable_cloud_calculation.vessel_leak_max_flammable_cloud_results.phase = {vessel_leak_max_flammable_cloud_calculation.vessel_leak_max_flammable_cloud_results.phase}'
        
        # check whether the lfl+extent is a number and not zero
        if not isinstance(vessel_leak_max_flammable_cloud_calculation.vessel_leak_max_flammable_cloud_results.lfl_extent, (int, float)) or vessel_leak_max_flammable_cloud_calculation.vessel_leak_max_flammable_cloud_results.lfl_extent == 0:
            assert False,f'Regression failed with vessel_leak_max_flammable_cloud_calculation.vessel_leak_max_flammable_cloud_results.lfl_extent = {vessel_leak_max_flammable_cloud_calculation.vessel_leak_max_flammable_cloud_results.lfl_extent}'
        
        # check whether the lfl_area is a number and not zero
        if not isinstance(vessel_leak_max_flammable_cloud_calculation.vessel_leak_max_flammable_cloud_results.lfl_area, (int, float)) or vessel_leak_max_flammable_cloud_calculation.vessel_leak_max_flammable_cloud_results.lfl_area == 0:
            assert False,f'Regression failed with vessel_leak_max_flammable_cloud_calculation.vessel_leak_max_flammable_cloud_results.lfl_area = {vessel_leak_max_flammable_cloud_calculation.vessel_leak_max_flammable_cloud_results.lfl_area}'
        
        # check whether the lfl_height is a number and not zero
        if not isinstance(vessel_leak_max_flammable_cloud_calculation.vessel_leak_max_flammable_cloud_results.lfl_height, (int, float)) or vessel_leak_max_flammable_cloud_calculation.vessel_leak_max_flammable_cloud_results.lfl_height == 0:
            assert False,f'Regression failed with vessel_leak_max_flammable_cloud_calculation.vessel_leak_max_flammable_cloud_results.lfl_height = {vessel_leak_max_flammable_cloud_calculation.vessel_leak_max_flammable_cloud_results.lfl_height}'
        
        print(f'SUCCESS: vessel_leak_max_flammable_cloud_calculation ({vessel_leak_max_flammable_cloud_calculation.calculation_elapsed_time}ms)')
    else:
        assert False, f'FAILED vessel_leak_max_flammable_cloud_calculation with result code {resultCode}'