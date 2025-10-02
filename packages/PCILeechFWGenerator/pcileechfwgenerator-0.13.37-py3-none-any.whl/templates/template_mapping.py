#!/usr/bin/env python3
"""
Template path mapping for the flattened directory structure.

This module provides mappings from the old nested template paths to the new
flatter structure, ensuring backward compatibility during the transition.
"""

# Mapping from old paths to new paths
TEMPLATE_PATH_MAPPING = {
    # SystemVerilog templates
    "systemverilog/bar_controller.sv.j2": "sv/bar_controller.sv.j2",
    "systemverilog/basic_bar_controller.sv.j2": "sv/basic_bar_controller.sv.j2",
    "systemverilog/cfg_shadow.sv.j2": "sv/cfg_shadow.sv.j2",
    "systemverilog/device_config.sv.j2": "sv/device_config.sv.j2",
    "systemverilog/msix_capability_registers.sv.j2": "sv/msix_capability_registers.sv.j2",
    "systemverilog/msix_implementation.sv.j2": "sv/msix_implementation.sv.j2",
    "systemverilog/msix_table.sv.j2": "sv/msix_table.sv.j2",
    "systemverilog/option_rom_bar_window.sv.j2": "sv/option_rom_bar_window.sv.j2",
    "systemverilog/option_rom_spi_flash.sv.j2": "sv/option_rom_spi_flash.sv.j2",
    "systemverilog/pcileech_cfgspace.coe.j2": "sv/pcileech_cfgspace.coe.j2",
    "systemverilog/pcileech_fifo.sv.j2": "sv/pcileech_fifo.sv.j2",
    "systemverilog/pcileech_tlps128_bar_controller.sv.j2": "sv/pcileech_tlps128_bar_controller.sv.j2",
    "systemverilog/top_level_wrapper.sv.j2": "sv/top_level_wrapper.sv.j2",
    # Advanced SystemVerilog templates
    "systemverilog/advanced/advanced_controller.sv.j2": "sv/advanced_controller.sv.j2",
    "systemverilog/advanced/clock_crossing.sv.j2": "sv/clock_crossing.sv.j2",
    "systemverilog/advanced/error_counters.sv.j2": "sv/error_counters.sv.j2",
    "systemverilog/advanced/error_declarations.sv.j2": "sv/error_declarations.sv.j2",
    "systemverilog/advanced/error_detection.sv.j2": "sv/error_detection.sv.j2",
    "systemverilog/advanced/error_handling_complete.sv.j2": "sv/error_handling_complete.sv.j2",
    "systemverilog/advanced/error_handling.sv.j2": "sv/error_handling.sv.j2",
    "systemverilog/advanced/error_logging.sv.j2": "sv/error_logging.sv.j2",
    "systemverilog/advanced/error_outputs.sv.j2": "sv/error_outputs.sv.j2",
    "systemverilog/advanced/error_state_machine.sv.j2": "sv/error_state_machine.sv.j2",
    "systemverilog/advanced/main_module.sv.j2": "sv/main_module.sv.j2",
    "systemverilog/advanced/performance_counters.sv.j2": "sv/performance_counters.sv.j2",
    "systemverilog/advanced/power_management.sv.j2": "sv/power_management.sv.j2",
    # Missing advanced templates
    "systemverilog/advanced/clock_gating.sv.j2": "sv/clock_gating.sv.j2",
    "systemverilog/advanced/error_recovery.sv.j2": "sv/error_recovery.sv.j2",
    "systemverilog/advanced/power_transitions.sv.j2": "sv/power_transitions.sv.j2",
    "systemverilog/advanced/reporting_logic.sv.j2": "sv/reporting_logic.sv.j2",
    "systemverilog/advanced/sampling_logic.sv.j2": "sv/sampling_logic.sv.j2",
    # Component templates
    "systemverilog/components/clock_domain_logic.sv.j2": "sv/clock_domain_logic.sv.j2",
    "systemverilog/components/device_specific_ports.sv.j2": "sv/device_specific_ports.sv.j2",
    "systemverilog/components/interrupt_logic.sv.j2": "sv/interrupt_logic.sv.j2",
    "systemverilog/components/power_declarations.sv.j2": "sv/power_declarations.sv.j2",
    "systemverilog/components/power_integration.sv.j2": "sv/power_integration.sv.j2",
    "systemverilog/components/read_logic.sv.j2": "sv/read_logic.sv.j2",
    "systemverilog/components/register_declarations.sv.j2": "sv/register_declarations.sv.j2",
    "systemverilog/components/register_logic.sv.j2": "sv/register_logic.sv.j2",
    # Module templates
    "systemverilog/modules/pmcsr_stub.sv.j2": "sv/pmcsr_stub.sv.j2",
    # TCL templates
    "tcl/bitstream.j2": "tcl/bitstream.j2",
    "tcl/constraints.j2": "tcl/constraints.j2",
    "tcl/device_setup.j2": "tcl/device_setup.j2",
    "tcl/implementation.j2": "tcl/implementation.j2",
    "tcl/ip_config_axi_pcie.j2": "tcl/ip_config_axi_pcie.j2",
    "tcl/ip_config_pcie7x.j2": "tcl/ip_config_pcie7x.j2",
    "tcl/ip_config_ultrascale.j2": "tcl/ip_config_ultrascale.j2",
    "tcl/ip_config.j2": "tcl/ip_config.j2",
    "tcl/master_build.j2": "tcl/master_build.j2",
    "tcl/pcileech_build.j2": "tcl/pcileech_build.j2",
    "tcl/pcileech_constraints.j2": "tcl/pcileech_constraints.j2",
    "tcl/pcileech_generate_project.j2": "tcl/pcileech_generate_project.j2",
    "tcl/pcileech_implementation.j2": "tcl/pcileech_implementation.j2",
    "tcl/pcileech_project_setup.j2": "tcl/pcileech_project_setup.j2",
    "tcl/pcileech_sources.j2": "tcl/pcileech_sources.j2",
    "tcl/project_setup.j2": "tcl/project_setup.j2",
    "tcl/sources.j2": "tcl/sources.j2",
    "tcl/synthesis.j2": "tcl/synthesis.j2",
    "tcl/common/header.j2": "tcl/header.j2",
    # Python templates
    "python/build_integration.py.j2": "python/build_integration.py.j2",
    "python/pcileech_build_integration.py.j2": "python/pcileech_build_integration.py.j2",
}


def get_new_template_path(old_path: str) -> str:
    """
    Get the new template path for a given old path.

    Args:
        old_path: The old nested template path

    Returns:
        The new flattened template path
    """
    # Remove leading slashes and normalize
    old_path = old_path.lstrip("/")

    # Check if we have a mapping
    if old_path in TEMPLATE_PATH_MAPPING:
        return TEMPLATE_PATH_MAPPING[old_path]

    # If no mapping exists, return the original path
    # This allows for gradual migration
    return old_path


def update_template_path(template_name: str) -> str:
    """
    Update a template name to use the new path structure.

    This function handles both old and new path formats gracefully.

    Args:
        template_name: The template name (may include path)

    Returns:
        The updated template path
    """
    # If it's already using the new structure, return as-is
    if template_name.startswith(("sv/", "tcl/", "python/")):
        return template_name

    # Otherwise, map it
    return get_new_template_path(template_name)
