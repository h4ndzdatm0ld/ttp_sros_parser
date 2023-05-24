# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2023-XX-XX

### Added
    - Introduced Dataclasses and simplified the main class object SrosParser
    - Contributions from @Jeremy-Coder76. Test / parsing changes + additional parsers. PR#33
    Methods
    - get_system_begin
    - get_mgmt_router_config
    - get_cflowd
    - get_python_declaration_configuration
    - get_filter_log_configuration
    - get_filter_match_list_configuration
    - get_system_security_configuration
    - get_qos_policy_configuration
    - get_qos_policy_configuration1
    - get_qos_policy_configuration2
    - get_python_configuration
    - get_isis_configuration
    - get_subscriber_mgmt_configuration
    - get_aaa_declarations_configuration
    - get_multicast_path_management_policy_configuration
    - get_port_xc_configuration
    - get_redundancy_configuration
    - get_filter_configuration
    - get_vrrp_configuration
    - get_igmp_configuration
    - get_l2tp_configuration
    - get_router_policy_configuration
    - get_router_bgp_configuration
    - get_subscriber_mgmt_ss_configuration
    - get_mirror_configuration
    - get_radius_configuration
    - get_dhcp_configuration
    - get_twamp_light_config
    - get_aaa_configuration
    - get_pim_configuration
    - get_ldp_configuration
    - get_system_time_ntp_config
### Changed
    - Several parsing changes happened, which will break previously working parsers. PR#33
    - Private `_parse` method always returns Dict now
    - All unit tests reflect the above changes

## [0.1.6] - 2022-22-05

### Added
    - Better support for LAG parsing
    - CI Actions updated for easy release process on Pypi / GH

### Changed
    - Double quotes on LAG rendering stripped to single
    - Loosened development dependencies for local dev
    - Pinned TTP (0.7.2) as anything above breaks parsing

## [0.1.5] - 2021-24-12

### Added

    - Full Test Coverage
    - Project restructure
    - Docker/Docker-Compose for local project testing, linting, etc.
    - Github Actions updates
    - Documentation
    - Added Changelog
    - Created a develop branch as default

## [Unreleased]
