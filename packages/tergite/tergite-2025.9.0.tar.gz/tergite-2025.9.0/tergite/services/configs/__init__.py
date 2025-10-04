# This code is part of Tergite
#
# (C) Copyright Miroslav Dobsicek 2020, 2021
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.
#
# Alteration Notice
# -----------------
# This code was refactored from the original by:
#
# Martin Ahindura, 2023
# Chalmers Next Labs, 2025

"""Entry into the configuration service"""
import dataclasses
import pathlib
import re
from configparser import ConfigParser
from typing import List, Optional

from .dtos import AccountInfo

TERGITERC_FILE = pathlib.Path.home() / ".qiskit" / "tergiterc"


class Tergiterc:
    """the Configuration parser for tergiterc files"""

    def __init__(self, rc_file: pathlib.Path = TERGITERC_FILE):
        """Initializes a Tergiterc instance

        The instance initialized, saves to and retrieves its
        data from file_path

        Args:
            rc_file: the path where the tergiterc file is saved, defaults to ``$HOME/.qiskit/tergiterc``
        """
        self._file_path = rc_file
        self._parser = Tergiterc._get_parser(rc_file)

    def load_accounts(self) -> List["AccountInfo"]:
        """Retrieves the accounts from the tergiterc file

        Returns:
            list of instances of
                :class:`~tergite.providers.tergite.account.AccountInfo`
                as read from the tergiterc file
        """

        account_fields = {field.name: True for field in dataclasses.fields(AccountInfo)}
        accounts = []

        parser = self._parser
        if not parser:
            return accounts

        sections_all = parser.sections()
        for section in sections_all:
            if section.startswith("service"):
                if not parser.has_option(section, "url"):
                    print(
                        f"Warning: Skipping account provider '{section}'. Invalid configuration."
                    )
                    continue

                section_items = dict(parser.items(section))
                service_name = section.split(" ", 1)[1].strip()

                new_account = AccountInfo(service_name, **section_items)
                accounts.append(new_account)

        return accounts

    def save_accounts(self, accounts: List["AccountInfo"]):
        """Saves the accounts into the tergiterc file

        Args:
            accounts: the list of instances of
                :class:`~tergite.providers.tergite.account.AccountInfo`
                to save

        Raises:
            Exception: If no accounts are passed
        """
        if not accounts:
            raise Exception("Cannot save account(s). None given.")

        if not self._parser:
            self._parser = ConfigParser()

        for account in accounts:
            # section
            section_name = "service " + account.service_name
            self._parser.add_section(section_name)

            # account configuration
            config = account.to_dict()
            config.pop("service_name")  # remove 'service_name'

            for key, value in config.items():
                self._parser.set(section_name, str(key), str(value))

        with self._file_path.open("w") as dest:
            self._parser.write(dest)

    @staticmethod
    def _get_parser(rc_file: pathlib.Path) -> Optional[ConfigParser]:
        """Initializes a :class:`configparser.ConfigParser` instance that
        has read from rc_file

        It returns None if rc_file does not exist.

        Returns:
            Optional[configparser.ConfigParser]: the ConfigParser with the
                rc_file loaded in it if the file exists
        """
        if not rc_file.exists():
            return None

        parser = ConfigParser()
        parser.SECTCRE = re.compile(r"\[ *(?P<header>[^]]+?) *\]")
        parser.read(rc_file)

        return parser
