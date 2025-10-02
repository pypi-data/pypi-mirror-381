from typing import List
from pydantic import BaseModel, Field

class ContentGridUser(BaseModel):
    sub: str
    iss: str
    exp: float
    name: str | None = None
    email: str | None = None
    access_token: str
    domains : List[str] = Field(validation_alias="context:application:domains")
    application_id : str = Field(validation_alias="context:application:id")
    
    
    
if __name__ == "__main__":
    user = ContentGridUser(
        **{
            "sub": "https://auth.sandbox.contentgrid.cloud/realms/cg-77594d8b-9bc9-40ed-b2a8-9c03a2905a20#d91e9a4d-8447-4bf1-8d10-339b2e5951ea",
            "aud": "contentgrid:extension:extract",
            "restrict:principal_claims": "24ZPEGV0IS5MAF8C2BjmaqH1p7wL4YS409zlL8ZE+nEUHsFFDu80eDpJXoFvZIb1Hh9bxamGaK0gE14wvA+btCuDrg5lkGcdCVj3zm/RWnIFKzlGUVn7Zkj4z4PCzsq/itKVNXEYBtAS/d0NRFSiZGvy775kFdK1VOi+hxsic1bHAZTvSs1jEFuddxEULExh2MqZ5h43n/vEhB0sxkmXevR7XSE4iolDzCWGrw6HzUZYP/QlSlz/S3cK+aeoShAP1G2SbuTGub5h1fsKMM22eg==",
            "iss": "https://extensions.sandbox.contentgrid.cloud/authentication/external",
            "may_act": {
                "sub": "extract",
                "iss": "https://auth.sandbox.contentgrid.cloud/realms/extensions"
            },
            "context:application:domains": [
                "8be240cc-4581-43c2-96db-a8ccf8579e7d.sandbox.contentgrid.cloud"
            ],
            "exp": 1755775732,
            "context:application:id": "8be240cc-4581-43c2-96db-a8ccf8579e7d",
            "access_token" : "123"
        }
    )
    print(user)