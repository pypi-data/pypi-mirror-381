from urllib.parse import urlencode
from fastapi import FastAPI
from fastapi.routing import APIRoute
from pydantic import BaseModel, Field, field_serializer
from fastapi._compat import ModelField
from typing import Dict, Optional, Tuple, Type, Any, Union, List, Self, TypeVar, Generic, Callable, cast
import logging
from contentgrid_hal_client.hal import HALShape, HALLink
from contentgrid_hal_client.hal_forms import HALFormsTemplate, HALFormsMethod, HALFormsPropertyType, HALFormsProperty
import uri_template

def get_route_from_app(app: FastAPI, endpoint_function: str) -> APIRoute:
    for route in app.routes:
        if isinstance(route, APIRoute) and route.name == endpoint_function:
            return route
    else:
        error_message = f"No route found for endpoint {endpoint_function}"
        raise ValueError(error_message)

def _add_params(url : str, params: Optional[Dict[str, str]] = None) -> str:
    if params:
        url_postfix = "?" + urlencode(params)
        url += url_postfix
    return url

def get_body_from_route(route : APIRoute) -> Tuple[Optional[BaseModel], dict]:
    required_body = route.body_field
    if not required_body:
        return None, {}
    pydantic_body, default_data = get_pydantic_base_model_from_model_field(required_body)
    return pydantic_body, default_data
    
def get_pydantic_base_model_from_model_field(model_field : ModelField) -> Tuple[BaseModel, dict]:
    default_data = model_field._type_adapter.get_default_value() or {}
    pydantic_body = cast(BaseModel, model_field._type_adapter._type)
    return pydantic_body, default_data

def extract_hal_forms_properties_from_pydantic_base_model(
    pydantic_base_model : BaseModel,
    default_data : dict = {}
) -> List[HALFormsProperty]:
    properties : List[HALFormsProperty] = []
    for field_name, field_info in pydantic_base_model.model_fields.items():
        # Determine property type based on field type
        property_type = HALFormsPropertyType.text
        
        # Convert field type to HALFormsPropertyType
        if field_info.annotation is int or field_info.annotation is float:
            property_type = HALFormsPropertyType.number
        elif field_info.annotation is bool:
            property_type = HALFormsPropertyType.checkbox
        
        # Get default value for this field if available
        field_default = default_data.get(field_name) if default_data else None
        
        # Create HALFormsProperty
        field_property = HALFormsProperty(
            name=field_name,
            prompt=field_info.description or field_name,
            required=field_info.is_required(),
            type=property_type,
            value=field_default
        )
        properties.append(field_property)
    return properties

class LinkForType(BaseModel):
    endpoint_function_name: str
    templated: bool = False
    path_params: Union[dict[str, str],  Callable[["FastAPIHALResponse"], dict[str, str]]] = Field(default_factory=dict)
    params: Union[dict[str, Union[str, int, float]], Callable[["FastAPIHALResponse"], dict[str, Union[str, int, float]]]] = Field(default_factory=dict)
    condition: Union[Callable[["FastAPIHALResponse"], bool], bool] = True


class HALLinkFor(LinkForType):
    pass

class HALTemplateFor(LinkForType):
    pass
    
    
HALLinks = dict[str, Union[HALLink, HALLinkFor]]
HALTemplates = dict[str, Union[HALFormsTemplate, HALTemplateFor]]

# Type variable for generic embedded resources - must be a subclass of FastAPIHALResponse
T = TypeVar('T', bound='FastAPIHALResponse')


class FastAPIHALResponse(HALShape):    
    links: dict[str, Union[HALLink, HALLinkFor]] = Field(alias="_links", exclude=False, default_factory=dict)
    templates: dict[str, Union[HALFormsTemplate, HALTemplateFor]] | None = Field(default=None, alias="_templates")
    
    def __expand_link(self, link : HALLinkFor | HALLink) -> HALLink | None:
        """
            Expand the links based on server url and path and params.
            This method should be called after the class is initialized.
            Returns None if the link should be excluded based on condition.
        """
        if not hasattr(self.__class__, '_app'):
            raise ValueError("App not initialized. Call init_app() before using this method.")
        
        if not isinstance(link, HALLinkFor):
            return link
        
        # Check condition - if False, exclude the link
        if isinstance(link.condition, bool):
            if not link.condition:
                return None
        elif callable(link.condition):
            if not link.condition(self):
                return None
        
        if hasattr(self.__class__, '_app') and self.__class__._app:
            route = get_route_from_app(self.__class__._app, link.endpoint_function_name)
            
            if hasattr(self.__class__, '_server_url'):
                uri = f"{self.__class__._server_url}{route.path}"
            else:
                uri = route.path
                
            expanded_link = HALLink(uri=uri, templated=link.templated)
            
            if link.path_params:
                # Handle callable params
                if callable(link.path_params):
                    resolved_path_params = link.path_params(self)
                else:
                    resolved_path_params = link.path_params
                expanded_link.uri = uri_template.URITemplate(expanded_link.uri).expand(**resolved_path_params)
            
            if link.params:
                # Handle callable params
                if callable(link.params):
                    resolved_params = link.params(self)
                else:
                    resolved_params = link.params
                expanded_link.uri = _add_params(expanded_link.uri, resolved_params)
            
            return expanded_link

    
    @field_serializer('links')
    def ser_links(self, value: dict[str, Union[HALLink, HALLinkFor]]) -> dict[str, HALLink]:
        expanded_links = {}
        for key, link_value in value.items():
            expanded_link = self.__expand_link(link_value)
            if expanded_link is not None:  # Only include if condition is met
                expanded_links[key] = expanded_link
        return expanded_links
    
    @field_serializer('templates')
    def ser_templates(self, value: dict[str, Union[HALFormsTemplate, HALTemplateFor]] | None) -> dict[str, HALFormsTemplate]:
        expanded_templates = {}
        if value is None:
            return expanded_templates
        for key, template_value in value.items():
            if isinstance(template_value, HALTemplateFor) and hasattr(self.__class__, '_app') and self.__class__._app:
                try:
                    hallink = self.__expand_link(HALLinkFor(
                        **template_value.model_dump()
                    ))
                    
                    if hallink is None:
                        continue
                    
                    uri = hallink.uri
                    route = get_route_from_app(self.__class__._app, template_value.endpoint_function_name)
                    body_model, default_data = get_body_from_route(route=route)
                    if body_model is None:
                        properties = []
                    else:
                        properties = extract_hal_forms_properties_from_pydantic_base_model(pydantic_base_model=body_model, default_data=default_data)
                            
                    #TODO what should we do when there are multiple methods for the same function/endpoint?
                    expanded_templates[key] = HALFormsTemplate(
                        title=route.description if hasattr(route, 'description') and route.description else None,
                        method=HALFormsMethod(list(route.methods)[0]) if hasattr(route, 'methods') and route.methods else HALFormsMethod.GET,
                        target=uri,
                        properties=properties
                    )
                except ValueError:
                    logging.error(f"{self.__class__} hal template expansion failed: Route not found for template endpoint: {template_value.endpoint_function_name}")
                    continue
            else:
                expanded_templates[key] = template_value
        return expanded_templates
        
    
    @classmethod
    def init_app(cls: Type[Self], app: Any) -> None:
        """
        Bind a FastAPI app to other HyperModel base class.
        This allows HyperModel to convert endpoint function names into
        working URLs relative to the application root.

        Args:
            app (FastAPI): Application to generate URLs from
        """
        cls._app = app
        
    @classmethod
    def add_server_url(cls: Type[Self], server_url: str) -> None:
        """
        Set the server URL for generating absolute URLs.

        Args:
            server_url (str): The base URL of the server.
        """
        cls._server_url = server_url
        
class FastAPIHALCollection(FastAPIHALResponse, Generic[T]):
    embedded: dict[str, List[T]] | None = Field(default=None, alias="_embedded", description="Embedded resources")