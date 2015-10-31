from setuptools import setup

import parcel

setup(
    name         = parcel.__title__,
    version      = parcel.__version__,
    author       = parcel.__author__,
    author_email = parcel.__email__,
    license      = parcel.__license__,
    summary      = parcel.__summary__,

    entry_points = {
        'console_scripts' : [
            'parcel = parcel.parcel:cli'
        ]
    }
)
