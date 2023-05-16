# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2023-XX-XX

### Added
    - Contributions from @Jeremy-Coder76. Test / parsing changes + additional parsers. PR#33
        - AAA Config/Declaration
        - CFLOWD
        - DHCP
        - Filters
        - IGMP
        - ISIS
        - L2TP
        - LDP
        - Mirror
        - Mmgt Router
        - PIM
        - Multicast
        - Qos
        - Port Cross XC
        - VRRP
        - TWAMP
        - System /
        - Suubscriber
        - Router Policy
        - BGP
        - Redundancy
        - Radius
    - Introduced Dataclasses and simplified the main class object SrosParser

### Changed
    - Several parsing changes happened, which will break previously working parsers. PR#33

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
