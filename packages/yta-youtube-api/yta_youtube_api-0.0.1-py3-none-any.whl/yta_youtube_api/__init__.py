"""
This library will interact with Youtube by
using its v3 Data service.

It will create a 'client-secret.json' file
and a 'token_files' folder in the root
folder of the project in which you are
implementing and using this library.

Some interesting links below:
- https://webapps.stackexchange.com/a/101153
"""
from yta_programming_path import DevPathHandler
from yta_google_api.oauth_api import GoogleOauthAPI


API_NAME = 'youtube'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/youtube']
CLIENT_SECRET_FILENAME = DevPathHandler.get_project_abspath() + 'client-secret.json'
TOKEN_FILES_ABSPATH = DevPathHandler.get_project_abspath() + 'token_files/'

class YoutubeAPI:
    """
    Class to simplify and encapsulate the
    functionality related to the Youtube API
    flow, tokens and credentials handling.

    This class will create a 'client-secret.json'
    file and a 'token_files' folder in the root
    folder of the project in which you are
    implementing and using this library.
    """

    @staticmethod
    def is_youtube_token_valid(
    ) -> bool:
        """
        Check if the current Youtube Data v3 API
        token is valid or not.
        """
        return GoogleOauthAPI(CLIENT_SECRET_FILENAME, TOKEN_FILES_ABSPATH).is_oauth_token_valid(API_NAME, API_VERSION, SCOPES)

    @staticmethod
    def start_youtube_auth_flow(
    ):
        """
        Start the Google Auth flow for Youtube Data
        v3 API.
        """
        return GoogleOauthAPI(CLIENT_SECRET_FILENAME, TOKEN_FILES_ABSPATH).start_google_auth_flow(API_NAME, API_VERSION, SCOPES)

    @staticmethod
    def create_youtube_service(
    ):
        """
        Create a Youtube Data v3 API service and
        return it.
        """
        return GoogleOauthAPI(CLIENT_SECRET_FILENAME, TOKEN_FILES_ABSPATH).create_service(API_NAME, API_VERSION, SCOPES)
