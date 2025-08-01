from setuptools import setup, find_packages

setup(
    name="weber-ddos",
    version="1.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "weber=weber_ddos.__main__:main"
        ]
    },
    install_requires=[
        "pyfiglet"
    ],
    author="Jeth Weber",
    description="Ferramenta para executar ataques DDoS robustos",
)
