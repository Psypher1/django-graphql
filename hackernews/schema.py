import graphene
import graphql_jwt

import links.schema
import users.schema


class Query(users.schema.Query, links.schema.Query, graphene.ObjectType):
    pass


class Mutation(users.schema.Mutation, links.schema.Mutation, graphene.ObjectType):
    # used to authenticate the User with its username and password to obtain the JSON Web token.
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    # to confirm that the token is valid, passing it as an argument.
    verify_token = graphql_jwt.Verify.Field()
    # to obtain a new token within the renewed expiration time for non-expired tokens, if they are enabled to expire. Using it is outside the scope of this tutorial.
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)