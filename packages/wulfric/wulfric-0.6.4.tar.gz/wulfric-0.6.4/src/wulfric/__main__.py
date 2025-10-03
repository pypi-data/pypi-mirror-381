# ================================== LICENSE ===================================
# Wulfric - Cell, Atoms, K-path, visualization.
# Copyright (C) 2023-2025 Andrey Rybakov
#
# e-mail: anry@uv.es, web: adrybakov.com
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# ================================ END LICENSE =================================
from argparse import ArgumentParser, RawDescriptionHelpFormatter

from wulfric import __version__
from wulfric._osfix import _winwait
from wulfric._package_info import _warranty, logo


def main():
    parser = ArgumentParser(
        description=logo(),
        formatter_class=RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "command",
        default=None,
        help="Which command to run",
        choices=["logo", "warranty"],
        nargs="?",
    )
    parser.add_argument(
        "-v",
        "--version",
        action="store_true",
        help="Print version",
    )
    args = parser.parse_args()

    if args.version:
        print(f"Wulfric v{__version__}")

    elif args.command == "logo":
        print(logo())
    elif args.command == "warranty":
        print("\n" + _warranty() + "\n")
    elif args.command is None:
        parser.print_help()
    else:
        raise ValueError(f"Command {args.command} is not recognized.")


if __name__ == "__main__":
    main()
    _winwait()
