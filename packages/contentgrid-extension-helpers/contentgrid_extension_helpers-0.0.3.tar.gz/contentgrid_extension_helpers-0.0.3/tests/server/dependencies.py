
# Foo repository dependency
from contentgrid_extension_helpers.authentication.user import ContentGridUser
from contentgrid_extension_helpers.dependencies.clients.contentgrid.extension_flow_factory import ContentGridExtensionFlowClientFactory
from contentgrid_extension_helpers.dependencies.authentication.user import ContentGridUserDependency

from contentgrid_application_client.application import ContentGridApplicationClient
from fastapi import Depends
from sqlmodel import Session
from contentgrid_extension_helpers.dependencies.sqlalch.db import SQLiteSessionFactory
from contentgrid_extension_helpers.dependencies.clients.contentgrid.service_account_factory import ContentGridServiceAccountFactory
from server.repositories.foo_repo import FooRepository

db_factory = SQLiteSessionFactory()

contentgrid_user_dependency = ContentGridUserDependency()

def get_foo_repository(session: Session = Depends(db_factory)) -> FooRepository:
    """Get a foo repository instance"""
    return FooRepository(session)

def get_contentgrid_user(user : ContentGridUser = Depends(contentgrid_user_dependency)) -> ContentGridUser:
    """Get a ContentGridUser instance"""
    return user

extension_flow_factory = ContentGridExtensionFlowClientFactory()
contentgrid_application_client_dependency = extension_flow_factory.create_client_dependency(user_dependency=get_contentgrid_user)


def get_contentgrid_application_client(client : ContentGridApplicationClient = Depends(contentgrid_application_client_dependency)) -> ContentGridApplicationClient:
    """Get a ContentGridApplicationClient instance"""
    return client