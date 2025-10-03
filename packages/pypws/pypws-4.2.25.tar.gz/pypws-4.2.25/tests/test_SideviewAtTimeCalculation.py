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
    DispersionCalculation,
    SideviewAtTimeCalculation,
    VesselCatastrophicRuptureCalculation,
    VesselStateCalculation,
)
from pypws.entities import (
    Bund,
    DischargeParameters,
    DispersionOutputConfig,
    DispersionParameters,
    Material,
    MaterialComponent,
    State,
    Substrate,
    Vessel,
    Weather,
)
from pypws.enums import AtmosphericStabilityClass, ResultCode, SurfaceType, VesselShape, WindProfileFlag


def test():

    """
    Sideview at time calculation test case with the following properties:

        material = 'ETHANE (50%), BUTANE (30%) and PROPANE (20%)'
        state_temperature = 265.0
        state_pressure = 5.0E+05
        liquid_fraction = 0.8
        surface_type = SurfaceType.LAND
        surface_roughness = 0.2
        wind_speed = 5.0
        stability_class = AtmosphericStabilityClass.STABILITY_A
        end_point_concentration = 0.0
        specify_bund = True
        bund_height = 1.0
        bund_diameter = 8.0

    """

    material = Material("ETHANE_BUTANE_PROPANE", [MaterialComponent("ETHANE", 0.5), MaterialComponent("N-BUTANE", 0.3), MaterialComponent("PROPANE", 0.2)], component_count = 3)
    state = State(temperature=265.0, pressure= 5.0e5, liquid_fraction=0.8)
    surface_type = SurfaceType.LAND
    surface_roughness = 0.2
    wind_speed = 5.0
    stability_class = AtmosphericStabilityClass.STABILITY_A
    wind_profile_flag = WindProfileFlag.LOGARITHMIC_PROFILE
    end_point_concentration = 0.0
    specify_bund = True
    bund_height = 1.0
    bund_diameter = 8.0

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
                    shape=VesselShape.VERTICAL_CYLINDER,
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
        print(f'SUCCESS: vessel_catastrophic_rupture_calculation ({vessel_catastrophic_rupture_calculation.calculation_elapsed_time}ms)')
    else:
        assert False, f'FAILED vessel_catastrophic_rupture_calculation with result code {resultCode}'

    # Set up the entities required by the dispersion calculation.
    bund = Bund(specify_bund=specify_bund, bund_height=bund_height, bund_diameter=bund_diameter)
    substrate = Substrate(bund=bund, surface_type=surface_type, surface_roughness=surface_roughness)
    weather = Weather(wind_speed=wind_speed, stability_class=stability_class, wind_profile_flag=wind_profile_flag)
    dispersion_parameters = DispersionParameters()

    # Set up the dispersion calculation.
    dispersion_calculation = DispersionCalculation(vessel_catastrophic_rupture_calculation.exit_material, substrate, vessel_catastrophic_rupture_calculation.discharge_result, vessel_catastrophic_rupture_calculation.discharge_records, len(vessel_catastrophic_rupture_calculation.discharge_records), weather, dispersion_parameters, end_point_concentration)

    print('Running dispersion_calculation...')
    resultCode = dispersion_calculation.run()

    # Print any messages.
    if len(dispersion_calculation.messages) > 0:
        print('Messages:')
        for message in dispersion_calculation.messages:
            print(message)

    if resultCode == resultCode.SUCCESS:
        print(f'SUCCESS: dispersion_calculation ({dispersion_calculation.calculation_elapsed_time}ms)')
    else:
        assert False, f'FAILED dispersion_calculation with result code {resultCode}'

    # Set up the entities required by the sideview calculation.
    dispersion_output_config = DispersionOutputConfig(concentration = end_point_concentration, time=0)

    # Set up the sideview calculation.
    sideview_at_time_calculation = SideviewAtTimeCalculation(scalar_udm_outputs= dispersion_calculation.scalar_udm_outputs, weather= weather, dispersion_records= dispersion_calculation.dispersion_records, dispersion_record_count= len(dispersion_calculation.dispersion_records), substrate=substrate, dispersion_output_config=dispersion_output_config, material=vessel_catastrophic_rupture_calculation.exit_material, dispersion_parameters=dispersion_parameters)

    print('Running sideview_at_time_calculation...')
    resultCode = sideview_at_time_calculation.run()

    # Print any messages.
    if len(sideview_at_time_calculation.messages) > 0:
        print('Messages:')
        for message in sideview_at_time_calculation.messages:
            print(message)

    if resultCode == resultCode.SUCCESS:
        # check whether there are contour points
        if (len(sideview_at_time_calculation.contour_points) == 0):
            assert False, f'Regression failed with len(sideview_at_time_calculation.contour_points) = {len(sideview_at_time_calculation.contour_points)}'

        # check whether the x value of one of the contour points is a number and not zero
        if not isinstance(sideview_at_time_calculation.contour_points[len(sideview_at_time_calculation.contour_points)-3].x, (int, float)) or sideview_at_time_calculation.contour_points[len(sideview_at_time_calculation.contour_points)-3].x == 0:
            assert False, f'Regression failed with sideview_at_time_calculation.contour_points[len(sideview_at_time_calculation.contour_points)-3].x = {sideview_at_time_calculation.contour_points[len(sideview_at_time_calculation.contour_points)-3].x}'
        
        # check where there are dispersion records
        if (len(sideview_at_time_calculation.dispersion_records) == 0):
            assert False, f'Regression failed with len(sideview_at_time_calculation.dispersion_records) = {len(sideview_at_time_calculation.dispersion_records)}'

        # check whether the centreline concentration of one of the dispersion records is a number and not zero
        if not isinstance(sideview_at_time_calculation.dispersion_records[len(sideview_at_time_calculation.dispersion_records)-1].centreline_concentration, (int, float)) or sideview_at_time_calculation.dispersion_records[len(sideview_at_time_calculation.dispersion_records)-1].centreline_concentration == 0:
            assert False, f'Regression failed with sideview_at_time_calculation.dispersion_records[len(sideview_at_time_calculation.dispersion_records)-1].centreline_concentration = {sideview_at_time_calculation.dispersion_records[len(sideview_at_time_calculation.dispersion_records)-1].centreline_concentration}'

        print(f'SUCCESS: sideview_at_time_calculation ({sideview_at_time_calculation.calculation_elapsed_time}ms)')
    else:
        assert False, f'FAILED sideview_at_time_calculation with result code {resultCode}'
