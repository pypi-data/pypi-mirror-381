# This code is part of Tergite
#
# (C) Copyright Miroslav Dobsicek 2021
# (C) Copyright Axel Andersson 2022
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.
from dataclasses import asdict, dataclass


@dataclass
class AccountInfo:
    service_name: str
    url: str
    token: str = None

    def to_dict(self: object) -> dict:
        return asdict(self)
