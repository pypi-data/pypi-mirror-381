from pydantic import BaseModel, Field

from muck_out.validators import HtmlStringOrNone, IdFieldOrNone, UrlList


class CommonActor(BaseModel):
    inbox: IdFieldOrNone = Field(
        None,
        examples=["https://actor.example/inbox"],
        description="The inbox of the actor",
    )

    outbox: IdFieldOrNone = Field(
        None,
        examples=["https://actor.example/outbox"],
        description="The outbox of the actor",
    )

    followers: IdFieldOrNone = Field(
        None,
        examples=["https://actor.example/followers"],
        description="The followers collection of the actor",
    )

    following: IdFieldOrNone = Field(
        None,
        examples=["https://actor.example/following"],
        description="The following collection of the actor",
    )

    summary: HtmlStringOrNone = Field(
        None,
        examples=["My Fediverse account"],
        description="Description of the actor",
    )

    name: HtmlStringOrNone = Field(
        None,
        examples=["Alice"],
        description="Display name of the actor",
    )

    url: UrlList = Field(
        default=[],
        description="A list of urls that expand on the content of the object",
    )
