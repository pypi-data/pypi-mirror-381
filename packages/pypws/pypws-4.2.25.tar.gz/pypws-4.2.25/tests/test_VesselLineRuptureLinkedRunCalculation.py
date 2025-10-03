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

from pypws.calculations import LoadMassInventoryVesselForLineRuptureScenarioCalculation, VesselLineRuptureLinkedRunCalculation
from pypws.entities import Material, MaterialComponent, Weather, Substrate, DischargeParameters, LineRupture, Vessel, FlammableParameters, DispersionParameters, FlammableParameters, ExplosionParameters, ExplosionOutputConfig, ExplosionConfinedVolume, FlammableOutputConfig, DispersionOutputConfig, ExplosionConfinedVolume
from pypws.enums import ResultCode, AtmosphericStabilityClass, SpecialConcentration, WindProfileFlag


def test():
	
    material = Material("AMMONIA", [MaterialComponent("AMMONIA", 1.0)], component_count = 1)


    # Create a load mass inventory vessel for line rupture scenario calculation using the material.
    load_mass_inventory_vessel_for_line_rupture_scenario_calculation = LoadMassInventoryVesselForLineRuptureScenarioCalculation(material = material, temperature = 250, pressure = float(11e5), mass = float(1e3), pipe_length = 10.0, pipe_diameter = 0.5, release_elevation = 1.0, release_angle = 0.35)

    # Run the calculation
    print('Running load_mass_inventory_vessel_for_line_rupture_scenario_calculation...')
    resultCode = load_mass_inventory_vessel_for_line_rupture_scenario_calculation.run()

    # Print any messages.
    if len(load_mass_inventory_vessel_for_line_rupture_scenario_calculation.messages) > 0:
        print('Messages:')
        for message in load_mass_inventory_vessel_for_line_rupture_scenario_calculation.messages:
            print(message)

    if resultCode == ResultCode.SUCCESS:
        print(f'SUCCESS: load_mass_inventory_vessel_for_line_rupture_scenario_calculation ({load_mass_inventory_vessel_for_line_rupture_scenario_calculation.calculation_elapsed_time}ms)')
    else:
        assert False, f'FAILED load_mass_inventory_vessel_for_line_rupture_scenario_calculation with result code {resultCode}'

    # Define the weather conditions
    weather = Weather( wind_speed = 5.0, stability_class = AtmosphericStabilityClass.STABILITY_B, wind_profile_flag = WindProfileFlag.LOGARITHMIC_PROFILE)

    # Define the substrate
    substrate = Substrate()

    # Define the dispersion parameters
    dispersion_parameters = [DispersionParameters(averaging_time = 18.75), DispersionParameters(averaging_time = 18.75)]

    # Define the dispersion output configuration
    dispersion_output_configs_flammable = [DispersionOutputConfig(special_concentration = SpecialConcentration.LFL_FRACTION, elevation = 0.0)]
    dispersion_output_configs_toxic = [DispersionOutputConfig(special_concentration = SpecialConcentration.NOT_DEFINED, concentration = 5e-5, elevation = 0.0)]

    # Define the flammable parameters
    flammable_parameters = FlammableParameters()

    # Define the flammable output configuration
    flammable_output_configs = [FlammableOutputConfig()]

    # Define the explosion parameters
    explosion_parameters = ExplosionParameters()

    # Define the explosion output configuration
    explosion_output_configs = [ExplosionOutputConfig()]

    # Define the explosion confined volumes
    explosion_confined_volumes = [ExplosionConfinedVolume()]

    # 
    vessel_line_rupture_linked_run_calculation = VesselLineRuptureLinkedRunCalculation(
        vessel = load_mass_inventory_vessel_for_line_rupture_scenario_calculation.vessel,
        line_rupture = load_mass_inventory_vessel_for_line_rupture_scenario_calculation.line_rupture,
        discharge_parameters = DischargeParameters(),
        substrate = substrate,
        weather = weather,
        dispersion_parameters = dispersion_parameters,
        dispersion_parameter_count = len(dispersion_parameters),
        end_point_concentration = 0.0,
        flammable_parameters = flammable_parameters,
        explosion_parameters = explosion_parameters,
        dispersion_flam_output_configs = dispersion_output_configs_flammable,
        dispersion_flam_output_config_count = len(dispersion_output_configs_flammable),
        dispersion_toxic_output_configs = dispersion_output_configs_toxic,
        dispersion_toxic_output_config_count = len(dispersion_output_configs_toxic),
        flammable_output_configs = flammable_output_configs,
        flammable_output_config_count = len(flammable_output_configs),
        explosion_output_configs = explosion_output_configs,
        explosion_output_config_count = len(explosion_output_configs),
        explosion_confined_volumes = explosion_confined_volumes,
        explosion_confined_volume_count = len(explosion_confined_volumes)
    )

    # Run the calculation
    print('Running vessel_line_rupture_linked_run_calculation...')
    resultCode = vessel_line_rupture_linked_run_calculation.run()

    # Print any messages.
    if len(vessel_line_rupture_linked_run_calculation.messages) > 0:
        print('Messages:')
        for message in vessel_line_rupture_linked_run_calculation.messages:
            print(message)

    if resultCode == ResultCode.SUCCESS:
        # check whether flame_length is a number and not zero
        if not isinstance(vessel_line_rupture_linked_run_calculation.jet_fire_flame_result.flame_length, (int, float)) or vessel_line_rupture_linked_run_calculation.jet_fire_flame_result.flame_length == 0:
            assert False,f'Regression failed with vessel_line_rupture_linked_run_calculation.jet_fire_flame_result.flame_length = {vessel_line_rupture_linked_run_calculation.jet_fire_flame_result.flame_length}'
        
        # check whether flame_diameter is a number and not zero
        if not isinstance(vessel_line_rupture_linked_run_calculation.jet_fire_flame_result.flame_diameter, (int, float)) or vessel_line_rupture_linked_run_calculation.jet_fire_flame_result.flame_diameter == 0:
            assert False,f'Regression failed with vessel_line_rupture_linked_run_calculation.jet_fire_flame_result.flame_diameter = {vessel_line_rupture_linked_run_calculation.jet_fire_flame_result.flame_diameter}'
        
        # check that the number of flam_conc_contour_points is zero
        if (len(vessel_line_rupture_linked_run_calculation.flam_conc_contour_points) != 0):
            assert False,f'Regression failed with len(vessel_line_rupture_linked_run_calculation.flam_conc_contour_points) = {len(vessel_line_rupture_linked_run_calculation.flam_conc_contour_points)}'
        
        # check that the number of toxic_conc_contour_points is not zero
        if (len(vessel_line_rupture_linked_run_calculation.toxic_conc_contour_points) == 0):
            assert False,f'Regression failed with len(vessel_line_rupture_linked_run_calculation.toxic_conc_contour_points) = {len(vessel_line_rupture_linked_run_calculation.toxic_conc_contour_points)}'
        
        # check the value of the first area_footprint_flam_conc is zero
        if (vessel_line_rupture_linked_run_calculation.area_footprint_flam_conc[0] != 0.0):
            assert False,f'Regression failed with vessel_line_rupture_linked_run_calculation.area_footprint_flam_conc[0] = {vessel_line_rupture_linked_run_calculation.area_footprint_flam_conc[0]}'
        
        # check whether the first area_footprint_toxic_conc is a number and not zero
        if not isinstance(vessel_line_rupture_linked_run_calculation.area_footprint_toxic_conc[0], (int, float)) or vessel_line_rupture_linked_run_calculation.area_footprint_toxic_conc[0] == 0:
            assert False,f'Regression failed with vessel_line_rupture_linked_run_calculation.area_footprint_toxic_conc[0] = {vessel_line_rupture_linked_run_calculation.area_footprint_toxic_conc[0]}'
        
        # check that the first area_contour_jet is zero
        if (vessel_line_rupture_linked_run_calculation.area_contour_jet[0] == 0.0):
            assert False,f'Regression failed with vessel_line_rupture_linked_run_calculation.area_contour_jet[0] = {vessel_line_rupture_linked_run_calculation.area_contour_jet[0]}'
        
        # check whether the first area_contour_pool is a number and not zero
        if not isinstance(vessel_line_rupture_linked_run_calculation.area_contour_pool[0], (int, float)) or vessel_line_rupture_linked_run_calculation.area_contour_pool[0] == 0:
            assert False,f'Regression failed with vessel_line_rupture_linked_run_calculation.area_contour_pool[0] = {vessel_line_rupture_linked_run_calculation.area_contour_pool[0]}'
        
        # check that the first explosion_overpressure_result exploded_mass is zero
        if (vessel_line_rupture_linked_run_calculation.explosion_overpressure_results[0].exploded_mass == 0.0):
            assert False,f'Regression failed with vessel_line_rupture_linked_run_calculation.explosion_overpressure_results[0].exploded_mass = {vessel_line_rupture_linked_run_calculation.explosion_overpressure_results[0].exploded_mass}'
        
        # check whether the first maximum_distance is zero
        if (vessel_line_rupture_linked_run_calculation.explosion_overpressure_results[0].maximum_distance == 0.0):
            assert False,f'Regression failed with vessel_line_rupture_linked_run_calculation.explosion_overpressure_results[0].maximum_distance = {vessel_line_rupture_linked_run_calculation.explosion_overpressure_results[0].maximum_distance}'

        print(f'SUCCESS: vessel_line_rupture_linked_run_calculation ({vessel_line_rupture_linked_run_calculation.calculation_elapsed_time}ms)')
    else:
        assert False, f'FAILED vessel_line_rupture_linked_run_calculation with result code {resultCode}'