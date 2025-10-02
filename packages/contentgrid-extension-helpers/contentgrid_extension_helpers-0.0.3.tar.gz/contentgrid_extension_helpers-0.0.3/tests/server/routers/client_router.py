
from contentgrid_extension_helpers.dependencies.clients.contentgrid.extension_flow_factory import ContentGridExtensionFlowClientFactory  
from fastapi import APIRouter
from contentgrid_application_client.application import ContentGridApplicationClient
from fastapi import Depends
from contentgrid_extension_helpers.authentication.user import ContentGridUser
from server.dependencies import get_contentgrid_application_client, get_contentgrid_user

client_router = APIRouter(prefix="/extract")

# @client_router.get("/")
# def get_user(user : ContentGridUser = Depends(get_contentgrid_user)):
#     return user

@client_router.get("/")
def get_extension_flow_factory(user: ContentGridUser = Depends(get_contentgrid_user), client : ContentGridApplicationClient = Depends(get_contentgrid_application_client)):
    user = user
    profile = client.get_profile()
    return {"profile": profile.data, "user": user}
