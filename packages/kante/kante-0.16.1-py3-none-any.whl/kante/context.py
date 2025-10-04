from strawberry.channels import ChannelsConsumer
from dataclasses import dataclass
from typing import Any, Dict, Literal, Mapping, Optional, Protocol


class User(Protocol):
    id: int
    sub: str

    def is_anonymous(self) -> bool:
        """Check if the user is anonymous."""
        ...


class Client(Protocol):
    id: str
    client_id: str
    
    
class Organization(Protocol):
    id: int
    slug: str
    
class Membership(Protocol):
    id: int


@dataclass
class UniversalRequest:
    _extensions: Dict[str, Any]
    _client: Optional[Client] = None
    _user: Optional[User] = None
    _organization: Optional[Organization] = None
    _membership: Optional[Membership] = None

    @property
    def user(self) -> User:
        """Get the user associated with the request."""
        if self._user is None:
            raise ValueError(
                "User is not set in the request. Do you have a strawberry extension setting this?"
            )

        return self._user
    
    
    @property
    def membership(self) -> Membership:
        """Get the user associated with the request."""
        if self._membership is None:
            raise ValueError(
                "Membserhip is not set in the request. Do you have a strawberry extension setting this?"
            )

        return self._membership


    @property
    def client(self) -> Client:
        if self._client is None:
            raise ValueError(
                "Client is not set in the request.  Do you have a strawberry extension setting this?"
            )

        return self._client
    
    @property
    def organization(self) -> Organization:
        if self._organization is None:
            raise ValueError(
                "Organization is not set in the request.  Do you have a strawberry extension setting this?"
            )

        return self._organization

    def set_user(self, user: User) -> None:
        """Set an extension value in the request."""
        self._user = user
        
    def set_organization(self, organization: Organization) -> None:
        """Set an organization in the request."""
        self._organization = organization
        
    def set_membership(self, membership: Membership) -> None:
        self._membership = membership
        
    def set_client(self, client: Client) -> None:
        """Set an extension value in the request."""
        self._client = client

    def get_extension(self, name: str) -> Any:
        """Get an extension value from the request."""

        if name not in self._extensions:
            raise ValueError(f"Extension {name} is not set in the request.")
        return self._extensions.get(name)

    def set_extension(self, name: str, value: Any) -> None:
        """Set an extension value in the request."""

        self._extensions[name] = value


@dataclass
class WsContext:
    request: UniversalRequest
    connection_params: Dict[str, Any]
    consumer: ChannelsConsumer
    extensions: Optional[Dict[str, Any]] = None
    type: Literal["ws"] = "ws"


@dataclass
class HttpContext:
    request: UniversalRequest
    headers: Mapping[str, str]
    type: Literal["http"] = "http"


Context = HttpContext | WsContext
