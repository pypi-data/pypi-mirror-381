from typing import Optional
from gql import gql

from .core.keycloak import DeviceFlowAuth, DeviceAuthConfig
from .core.gql import init_gql, execute_gql

# 전역 상태
_SSO_SERVER: Optional[str] = None
_API_SERVER: Optional[str] = None
_auth: Optional[DeviceFlowAuth] = None

def init_auth(sso_server: str, api_server: str):
    global _SSO_SERVER, _API_SERVER, _auth
    _SSO_SERVER = sso_server
    _API_SERVER = api_server

    _auth = DeviceFlowAuth(
        DeviceAuthConfig(
            api_server_url=_API_SERVER,
            sso_server_url=_SSO_SERVER,
            client_id="sso-client",
        ),
    )
    _auth.refresh_if_needed()
    _auth.login(open_browser=True)

    _set_auth_for_gql()

def _set_auth_for_gql():
    global _API_SERVER, _auth
    _auth.refresh_if_needed()
    init_gql(_API_SERVER, _auth.get_access_token())

def get_twin_data():
    FindEntitiesByTags = gql("""
    query FindEntitiesByTags($tags: [String!]!) {
        findEntitiesByTags(input: { tags: $tags }) {
            id
            properties
            system_properties
            createdAt
            updatedAt
            deletedAt
        }
    }
    """)
    EntitiesTree = gql("""
    query EntitiesTree($ids: [ID!]!) {
        entitiesTree(ids: $ids) {
            id
            properties
            system_properties
        }
    }
    """)

    tags = ["rack"]
    tagged_racks = execute_gql(FindEntitiesByTags, {"tags": tags}).get("findEntitiesByTags", [])

    ids = [rack["id"] for rack in tagged_racks]
    racks = execute_gql(EntitiesTree, {"ids": ids}).get("entitiesTree", [])

    sorted_racks = sorted(
        racks,
        key=lambda d: (d["properties"]["worldPosition"][0], d["properties"]["worldPosition"][1])
    )
    return sorted_racks
