const { ApolloServer,gql } = require('apollo-server');

const { resolvers } =  require('./resolvers');


const typeDefs = gql`
  type User {
    id: ID!
    name: String!
    age: Int!
  }

  type Query {
    users: [User]
    user(id: ID!): User
  }

  type Mutation {
    createUser(name: String!, age: Int!): User
    updateUser(id: ID!, name: String, age: Int): User
    deleteUser(id: ID!): User
  }
`;


const server = new ApolloServer({
    typeDefs,
    resolvers
});

server.listen().then(({ url }) => {
    console.log(`Server started at url: ${url}`);
})
