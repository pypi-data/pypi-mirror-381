from __future__ import annotations

import logging
from typing import TYPE_CHECKING
from typing import Any
from typing import Dict

if TYPE_CHECKING:
    from ragger_sdk.client import RaggerClient

from ..endpoints.status import StatusMixin

logger = logging.getLogger(__name__)


class IndexAPI(StatusMixin):
    def __init__(
        self,
        client: "RaggerClient",
    ) -> None:
        # Store the client reference for making authenticated API requests
        self.client = client
        # Define the base endpoint for all index operations
        self.endpoint = "/index/"

    def index(
        self,
        organization: str,
        project: str,
        force_overwrite: bool = False,
    ) -> Dict[str, Any]:

        # Prepare the API request payload
        # Clean whitespace from string parameters to avoid issues
        data = {
            "organization": organization.strip(),
            "project": project.strip(),
            "force_overwrite": force_overwrite,
        }

        # Make the API request to initiate index creation
        response = self.client.request(
            method="POST",  # POST to create new resources
            endpoint=self.endpoint,  # /index/ endpoint
            data=data,  # Request payload
        )

        # Step 6: Log successful initiation and return response
        logger.debug(f"Index creation initiated successfully for {organization}/{project}")
        return response
