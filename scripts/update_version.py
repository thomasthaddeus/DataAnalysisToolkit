"""update_version.py
_summary_

_extended_summary_

Raises:
    RuntimeError: _description_

Returns:
    _type_: _description_
"""

import os
import re
import toml


def get_current_version():
    # Assuming version is defined in src/my_package/__init__.py
    init_path = "./src/dataanalysistoolkit/utils/update_version.py"
    with open(init_path, "r", encoding="utf-8") as file:
        content = file.read()
    version_match = re.search(
        r"^__version__ = ['\"]([^'\"]*)['\"]", content, re.M
    )
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version in __init__.py")


def update_file_version(file_path, pattern, version):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
    content = re.sub(pattern, version, content)
    with open(file_path, "w", encoding='utf-8') as file:
        file.write(content)


def update_version_in_files(version):
    # Update pyproject.toml
    pyproject_path = "pyproject.toml"
    data = toml.load(pyproject_path)
    data["tool"]["poetry"]["version"] = version
    with open(pyproject_path, "w", encoding='utf-8') as file:
        toml.dump(data, file)

    # Update other files if necessary
    # example: update_file_version('README.md', r"(?<=Version:\s)[\d.]+", version)


if __name__ == "__main__":
    version = get_current_version()
    update_version_in_files(version)
