FROM ubuntu:20.04
# [Option] Install zsh
ARG INSTALL_ZSH="true"
# [Option] Upgrade OS packages to their latest versions
ARG UPGRADE_PACKAGES="true"

RUN apt-get install -y \
    python3.9 \
    python3-pip

# Requires SSH Key to be uploaded to GitHub
RUN git clone git@github.com:h4ndzdatm0ld/ttp_sros_parser.git

RUN pip3 install -r requirements.txt

