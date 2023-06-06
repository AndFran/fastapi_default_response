# fastapi_default_response
Just a small test for default responses in fastapi rather than using middleware

VersionResponse will cause the JSON to be of the form:

{
  "version":"1.0",
  "content":
            { "title":"Implementing Domain-Driven Design",
              "author":"Vaughn Vernon",
              "year":2013
            }
}

notice the version and content fields.

class VersionResponse(JSONResponse):
    def render(self, content: Any) -> bytes:
        return super().render({
            "version": VERSION,
            "content": content
        })

We could customise this further i.e. if we didnt want content in its own field.




