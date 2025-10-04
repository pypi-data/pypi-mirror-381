from blueness.pypi import setup

from bluer_ugv import NAME, VERSION, DESCRIPTION, REPO_NAME

setup(
    filename=__file__,
    repo_name=REPO_NAME,
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    packages=[
        NAME,
        f"{NAME}.help",
        f"{NAME}.help.swallow",
        f"{NAME}.parts",
        f"{NAME}.README",
        f"{NAME}.README.swallow",
        f"{NAME}.README.swallow.digital",
        f"{NAME}.README.swallow.digital.algo",
        f"{NAME}.README.swallow.digital.design",
        # kinds
        f"{NAME}.eagle",
        f"{NAME}.fire",
        f"{NAME}.robin",
        f"{NAME}.swallow",
        f"{NAME}.swallow.dataset",
        f"{NAME}.swallow.session",
        f"{NAME}.swallow.session.classical",
        f"{NAME}.swallow.session.classical.camera",
        f"{NAME}.swallow.session.classical.motor",
        f"{NAME}.swallow.session.classical.setpoint",
        f"{NAME}.swallow.session.classical.ultrasonic_sensor",
        f"{NAME}.sparrow",
    ],
    include_package_data=True,
    package_data={
        NAME: [
            "config.env",
            "sample.env",
            ".abcli/**/*.sh",
        ],
    },
)
