import os
import pathlib
import sys

PYPWS_RUN_LOCALLY = os.getenv('PYPWS_RUN_LOCALLY')
if PYPWS_RUN_LOCALLY and PYPWS_RUN_LOCALLY.lower() == 'true':
    # Navigate to the PYPWS directory by searching upwards until it is found.
    current_dir = pathlib.Path(__file__).resolve()

    while current_dir.name.lower() != 'package':
        if current_dir.parent == current_dir:  # Check if the current directory is the root directory
            raise FileNotFoundError("The 'pypws' directory was not found in the path hierarchy.")
        current_dir = current_dir.parent

    # Insert the path to the pypws package into sys.path.
    sys.path.insert(0, f'{current_dir}')


from pypws.calculations import (
    DispersionCalculation,
    PoolFireCalculation,
    VesselCatastrophicRuptureCalculation,
    VesselStateCalculation,
)
from pypws.entities import (
    DischargeParameters,
    DispersionParameters,
    FlammableParameters,
    Material,
    MaterialComponent,
    State,
    Substrate,
    Vessel,
    Weather,
)
from pypws.enums import (
    AtmosphericStabilityClass,
    PoolFireType,
    ResultCode,
    WindProfileFlag
)


def test():

    # Define the material contained by the vessel.
    material = Material("N-HEXANE", [MaterialComponent("N-HEXANE", 1.0)])

    # Define the initial state of the vessel.
    state = State(temperature=280.0, pressure= 2.0e5, liquid_fraction=0.8)

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

    # Create a vessel to use in the vessel catastrophic rupture calculation using the previously defined entities.
    vessel = Vessel(state=state,
                    material=material,
                    liquid_fill_fraction_by_volume=0.8,
                    vessel_conditions = vessel_state_calculation.vessel_conditions
                    )

    # Define the discharge parameters for the vessel catastrophic rupture calculation.
    discharge_parameters = DischargeParameters()

    # Create a vessel catastrophic rupture calculation using the vessel and discharge parameters.
    vessel_catastrophic_rupture_calculation = VesselCatastrophicRuptureCalculation(vessel, discharge_parameters)

    # Run the calculation.
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

    # Define the weather.
    weather = Weather(wind_speed = 1.5, stability_class = AtmosphericStabilityClass.STABILITY_F, wind_profile_flag = WindProfileFlag.LOGARITHMIC_PROFILE)

    # Define the substrate.
    substrate = Substrate()

    # Create a dispersion calculation based on the vessel catastrophic rupture calculation, weather, substrate, and dispersion parameters.
    dispersion_calculation = DispersionCalculation(discharge_records = vessel_catastrophic_rupture_calculation.discharge_records, discharge_result = vessel_catastrophic_rupture_calculation.discharge_result, weather = weather, substrate = substrate, dispersion_parameters = DispersionParameters(), end_point_concentration = 0.0, discharge_record_count = 1, material = vessel_catastrophic_rupture_calculation.exit_material)

    # Run the calculation.
    print('Running dispersion_calculation...')
    resultCode = dispersion_calculation.run()

    # Print any messages.
    if len(dispersion_calculation.messages) > 0:
        print('Messages:')
        for message in dispersion_calculation.messages:
            print(message)

    if resultCode == resultCode.SUCCESS:
        print(f'SUCCESS: dispersion_calculation_calculation ({dispersion_calculation.calculation_elapsed_time}ms)')
    else:
        assert False, f'FAILED dispersion_calculation with result code {resultCode}'

    # Define a flammable parameter set.
    flammable_parameters = FlammableParameters(pool_fire_type = PoolFireType.LATE)

    # Create a pool fire calculation based on the dispersion calculation, weather, substrate, and flammable parameters.
    pool_fire_calculation = PoolFireCalculation(material = vessel_catastrophic_rupture_calculation.exit_material, pool_records = dispersion_calculation.pool_records, pool_record_count = len(dispersion_calculation.pool_records), weather = weather, substrate = substrate, flammable_parameters = flammable_parameters)

    # Run the calculation.
    print('Running pool_fire_calculation...')
    resultCode = pool_fire_calculation.run()

    # Print any messages.
    if len(pool_fire_calculation.messages) > 0:
        print('Messages:')
        for message in pool_fire_calculation.messages:
            print(message)

    if resultCode == resultCode.SUCCESS:
        # check whether the flame length is a number and not zero
        if not isinstance(pool_fire_calculation.pool_fire_flame_result.flame_length, (int, float)) or pool_fire_calculation.pool_fire_flame_result.flame_length == 0:
            assert False,f'Regression failed with pool_fire_calculation.flame_result.flame_length = {pool_fire_calculation.flame_result.flame_length}'
        
        print(f'SUCCESS: pool_fire_calculation ({pool_fire_calculation.calculation_elapsed_time}ms)')
    else:
        assert False, f'FAILED pool_fire_calculation with result code {resultCode}'
