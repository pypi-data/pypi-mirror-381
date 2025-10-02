# Copyright CNRS/Inria/UCA
# Contributor(s): Eric Debreuve (since 2021)
#
# eric.debreuve@cnrs.fr
#
# This software is governed by the CeCILL  license under French law and
# abiding by the rules of distribution of free software.  You can  use,
# modify and/ or redistribute the software under the terms of the CeCILL
# license as circulated by CEA, CNRS and INRIA at the following URL
# "http://www.cecill.info".
#
# As a counterpart to the access to the source code and  rights to copy,
# modify and redistribute granted by the license, users are provided only
# with a limited warranty  and the software's author,  the holder of the
# economic rights,  and the successive licensors  have only  limited
# liability.
#
# In this respect, the user's attention is drawn to the risks associated
# with loading,  using,  modifying and/or developing or reproducing the
# software by the user in light of its specific status of free software,
# that may mean  that it is complicated to manipulate,  and  that  also
# therefore means  that it is reserved for developers  and  experienced
# professionals having in-depth computer knowledge. Users are therefore
# encouraged to load and test the software's suitability as regards their
# requirements in conditions enabling the security of their systems and/or
# data to be ensured and,  more generally, to use and operate it in the
# same conditions as regards security.
#
# The fact that you are presently reading this means that you have had
# knowledge of the CeCILL license and that you accept its terms.

from pathlib import Path

from setuptools import setup

AUTHOR = "Eric Debreuve"
E_MAIL = "eric.debreuve@univ-cotedazur.fr"

PYPI_NAME = "cell-tracking-bc"
DESCRIPTION = "Base Classes for Cell Tracking in Microscopy"
version = "2025.1"
PY_VERSION = "3.10"

REPOSITORY_NAME = "cell-tracking-bc"
REPOSITORY_USER = "eric.debreuve"
REPOSITORY_SITE = "src.koda.cnrs.fr"
DOCUMENTATION_SITE = f"https://{REPOSITORY_SITE}/{REPOSITORY_USER}/{REPOSITORY_NAME}"

IMPORT_NAME = "cell_tracking_BC"
PACKAGES = [
    IMPORT_NAME,
    f"{IMPORT_NAME}.catalog",
    f"{IMPORT_NAME}.catalog.channel",
    f"{IMPORT_NAME}.catalog.feature",
    f"{IMPORT_NAME}.catalog.feature.geometrical",
    f"{IMPORT_NAME}.catalog.feature.radiometric",
    f"{IMPORT_NAME}.catalog.feature.set",
    f"{IMPORT_NAME}.catalog.feature.temporal",
    f"{IMPORT_NAME}.catalog.matching",
    f"{IMPORT_NAME}.catalog.processing",
    f"{IMPORT_NAME}.catalog.segmentation",
    f"{IMPORT_NAME}.catalog.tracking",
    f"{IMPORT_NAME}.in_out",
    f"{IMPORT_NAME}.in_out.file",
    f"{IMPORT_NAME}.in_out.file.table",
    f"{IMPORT_NAME}.in_out.graphics",
    f"{IMPORT_NAME}.in_out.graphics.dbe",
    f"{IMPORT_NAME}.in_out.graphics.dbe.matplotlib",
    f"{IMPORT_NAME}.in_out.graphics.dbe.vedo",
    f"{IMPORT_NAME}.in_out.graphics.generic",
    f"{IMPORT_NAME}.in_out.graphics.type",
    f"{IMPORT_NAME}.in_out.text",
    f"{IMPORT_NAME}.standard",
    f"{IMPORT_NAME}.task",
    f"{IMPORT_NAME}.task.channel",
    f"{IMPORT_NAME}.task.feature",
    f"{IMPORT_NAME}.task.ground_truth",
    f"{IMPORT_NAME}.task.matching",
    f"{IMPORT_NAME}.task.processing",
    f"{IMPORT_NAME}.task.registration",
    f"{IMPORT_NAME}.task.segmentation",
    f"{IMPORT_NAME}.task.tracking",
    f"{IMPORT_NAME}.type",
    f"{IMPORT_NAME}.type.acquisition",
    f"{IMPORT_NAME}.type.compartment",
    f"{IMPORT_NAME}.type.segmentation",
    f"{IMPORT_NAME}.type.track",
    f"{IMPORT_NAME}.type.track.multiple",
    f"{IMPORT_NAME}.type.track.single",
]

HERE = Path(__file__).parent.resolve()


long_description = (HERE / "README.rst").read_text(encoding="utf-8")
repository_url = f"https://{REPOSITORY_SITE}/{REPOSITORY_USER}/{REPOSITORY_NAME}"
documentation_url = repository_url

folders = [IMPORT_NAME]
for node in (HERE / IMPORT_NAME).rglob("*"):
    if node.is_dir():
        node = node.relative_to(HERE)
        node = ".".join(node.parts)
        folders.append(node)
folders = sorted(folders)
if sorted(PACKAGES) != folders:
    raise ValueError(
        f"Missing packages in setup:\n"
        f"    - Declared={sorted(PACKAGES)}\n"
        f"    - Actual={folders}"
    )


if __name__ == "__main__":
    #
    setup(
        author=AUTHOR,
        author_email=E_MAIL,
        #
        name=PYPI_NAME,
        description=DESCRIPTION,
        long_description=long_description,
        long_description_content_type="text/x-rst",
        version=version,
        license="CeCILL-2.1",
        #
        classifiers=[
            "Topic :: Scientific/Engineering :: Image Recognition",
            "Intended Audience :: Science/Research",
            "License :: OSI Approved :: CEA CNRS Inria Logiciel Libre License, version 2.1 (CeCILL-2.1)",
            f"Programming Language :: Python :: {PY_VERSION}",
            "Development Status :: 4 - Beta",
        ],
        keywords="cell, tracking, microscopy, classes",
        #
        url=repository_url,
        project_urls={"Documentation": documentation_url, "Source": repository_url},
        #
        packages=PACKAGES,
        entry_points={
            "console_scripts": [f"find_track={IMPORT_NAME}.track_finder:Main"]
        },
        python_requires=f">={PY_VERSION}",
        install_requires=[
            "imageio",
            "issue-manager",
            "json-any",
            "logger-36",
            "matplotlib",
            "mrc",
            "networkx",
            "numpy",
            "openpyxl",
            "pandas",
            "pca-b-stream",
            "Pillow",
            "plotext",
            "rich",
            "scikit-image",
            "scipy",
            "tensorflow",
            "tensorrt",
            "tifffile",
            "xlsxwriter",
        ],
    )
