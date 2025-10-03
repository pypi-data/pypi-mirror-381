from datetime import datetime

from pydantic import BaseModel, Field, field_serializer

from .asset import Asset
from .geofence import Geofence
from .trigger import Trigger


class LocatorMqttConfig(BaseModel):
  host: str = Field(..., description='Defines the MQTT host of the locator')
  port: int = Field(..., description='Defines the MQTT port of the locator')
  username: str | None = Field(default=None, description='Defines the MQTT username of the locator')
  password: str | None = Field(default=None, description='Defines the MQTT password of the locator')
  topic: str = Field(..., description='Defines the MQTT topic of the locator')


class Locator(BaseModel):
  pk: str = Field(..., description='Defines the primary key of the locator', alias='id')
  token: str = Field(..., description='Defines the token of the locator')
  owner_id: int = Field(..., description='Defines the owner ID of the locator')

  mqtt_config: LocatorMqttConfig | None = Field(..., description='Defines the MQTT configuration of the locator')
  assets: list[Asset] = Field(
    default_factory=list,
    description='Defines the list of assets associated with the locator',
  )

  geofences: list[Geofence] = Field(
    default_factory=list,
    description='Defines the list of geofences associated with the locator',
  )

  triggers: list[Trigger] = Field(
    default_factory=list,
    description='Defines the list of triggers associated with the locator',
  )

  is_expired: bool = Field(
    default=False,
    description='Indicates whether the locator is expired',
  )

  expires_at: datetime | None = Field(
    default=None,
    description='Defines the expiration date of the locator, if applicable',
  )

  @field_serializer('expires_at', when_used='always')
  def serialize_expires_at(self, expires_at: datetime | None) -> float | None:
    return expires_at.timestamp() if expires_at else None
