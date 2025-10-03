import requests
from requests_ntlm import HttpNtlmAuth
import pandas as pd
import os
import logging
import json
from opsrampcli.DataSource import DataSource

logger = logging.getLogger(__name__)

URLSOURCE_DISPLAY_VALUE = 'display_value'


class URLDataSource(DataSource):

    class URLDataSourceException(DataSource.DataSourceException):
        pass

    def get_resources_df(self):
        job = self.job
        url = os.getenv("URLSOURCE_URL") or job['source']['urlsource']['url']

        user = os.getenv("URLSOURCE_USER") or job['source']['urlsource']['auth']['username']
        password = os.getenv("URLSOURCE_PASSWORD") or job['source']['urlsource']['auth']['password']
        result_key = os.getenv("URLSOURCE_RESULT_KEY") or job['source']['urlsource']['result_key'] or 'result'
       
        if 'ssl_verify' in job['source']['urlsource'] and job['source']['urlsource']['ssl_verify'] == False:
            ssl_verify = False
        else:
            ssl_verify = True

        qstrings = {}
        for k, v in job['source']['urlsource']['query_parameters'].items():
            qstrings[f'{k}'] = v
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        if 'headers' in job['source']['urlsource'] and job['source']['urlsource']['headers']:
            headers = job['source']['urlsource']['headers']

        auth_type = job['source']['urlsource']['auth']['type'] or "basic"

        if auth_type == 'oauth2':
            logger.info("Using oauth2 authentication")
            grant_type = os.getenv("URLSOURCE_GRANT_TYPE") or job['source']['urlsource']['auth']['grant_type'] or "password"
            client_id = os.getenv("URLSOURCE_CLIENT_ID") or job['source']['urlsource']['auth']['client_id']
            client_secret = os.getenv("URLSOURCE_CLIENT_SECRET") or job['source']['urlsource']['auth']['client_secret']
            scope = os.getenv("URLSOURCE_SCOPE") or job['source']['urlsource']['auth']['scope']
            token_url = os.getenv("URLSOURCE_TOKEN_URL") or job['source']['urlsource']['auth']['token_url'] or f"{url}/oauth_token.do"
            oauth_payload = {
                "grant_type": grant_type,
                "client_id": client_id,
                "client_secret": client_secret,
            }
            if user:
                oauth_payload["username"] = user
            if password:
                oauth_payload["password"] = password
            if scope:
                oauth_payload["scope"] = scope

            oauth_get_token_headers = {
                'Content-Type': 'application/x-www-form-urlencoded',
                'Accept': 'application/json'
            }
            logger.info("Getting oauth2 token")
            oauth_response = requests.post(token_url, headers=oauth_get_token_headers, data=oauth_payload)
            oauth_response.raise_for_status()
            token = json.loads(oauth_response.content)["access_token"]
            logger.info("Got oauth2 token")
            headers["Authorization"] = f"Bearer {token}"
            logger.info("Executing query")
            response = requests.get(url=url, params=qstrings, headers=headers)

        else:
            if auth_type == 'basic':
                auth = requests.auth.HTTPBasicAuth(user, password)
            elif auth_type == 'ntlm':
                auth = HttpNtlmAuth(user, password)

            response = requests.get(url=url, auth=auth, params=qstrings, headers=headers, verify=ssl_verify)
        try:
            responsedict = response.json()
        except Exception as e:
            msg = f'Failed to retrieve records from URL datasource: {e}'
            raise URLDataSource.URLDataSourceException(msg)
        records = responsedict.get(result_key, [])
        processed_recs = []
        for record in records:
            newrec = {}
            for key,value in record.items():
                if isinstance(value, dict) and URLSOURCE_DISPLAY_VALUE in value:
                    newrec[key] = value[URLSOURCE_DISPLAY_VALUE]
                else:
                    newrec[key] = value
            processed_recs.append(newrec)

        self.df = pd.DataFrame(processed_recs)
        self.df.fillna("", inplace=True)
