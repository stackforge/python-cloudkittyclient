# Copyright 2019 Objectif Libre
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
#
import json

from cloudkittyclient.common import base
from cloudkittyclient import exc


class DataframesManager(base.BaseManager):
    """Class used to handle /v2/dataframes endpoint"""

    url = '/v2/dataframes'

    def add_dataframes(self, **kwargs):
        """Add DataFrames to the storage backend. Returns nothing.

        :param dataframes: List of dataframes to add to the storage backend.
        :type dataframes: list of dataframes
        """

        dataframes = kwargs.get('dataframes')

        if not dataframes:
            raise exc.ArgumentRequired("'dataframes' argument is required")

        if not isinstance(dataframes, str):
            try:
                dataframes = json.dumps(dataframes)
            except TypeError:
                raise exc.InvalidArgumentError(
                    "'dataframes' must be either a string"
                    "or a JSON serializable object.")

        url = self.get_url(None, kwargs)
        return self.api_client.post(
            url,
            data=dataframes,
        )
