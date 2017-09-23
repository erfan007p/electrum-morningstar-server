from setuptools import setup

setup(
    name="electrum-morningstar-server",
    version="0.9",
    scripts=['run_electrum_morningstar_server','electrum-morningstar-server'],
    install_requires=['plyvel','jsonrpclib', 'irc>=11'],
    package_dir={
        'electrummorningStarserver':'src'
        },
    py_modules=[
        'electrummorningStarserver.__init__',
        'electrummorningStarserver.utils',
        'electrummorningStarserver.storage',
        'electrummorningStarserver.deserialize',
        'electrummorningStarserver.networks',
        'electrummorningStarserver.blockchain_processor',
        'electrummorningStarserver.server_processor',
        'electrummorningStarserver.processor',
        'electrummorningStarserver.version',
        'electrummorningStarserver.ircthread',
        'electrummorningStarserver.stratum_tcp',
        'electrummorningStarserver.stratum_http'
    ],
    description="MorningStar Electrum Server",
    author="Bob",
    author_email="Discord",
    license="GNU Affero GPLv3",
    url="https://github.com/morningStar/electrum-morningstar-server/",
    long_description="""Server for the Electrum Lightweight MorningStar Wallet"""
)


