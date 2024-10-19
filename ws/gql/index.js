const { ApolloServer, gql } = require('apollo-server');

// In-memory data store
let users = [
  { id: 1, name: 'Alice', age: 30 },
  { id: 2, name: 'Bob', age: 25 },
];

// Type definitions (Schema)
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

// Resolvers
const resolvers = {
  Query: {
    users: () => users,
    user: (parent, args) => users.find(user => user.id === parseInt(args.id)),
  },
  Mutation: {
    createUser: (parent, args) => {
      const newUser = {
        id: users.length + 1,
        name: args.name,
        age: args.age,
      };
      users.push(newUser);
      return newUser;
    },
    updateUser: (parent, args) => {
      let updatedUser = users.find(user => user.id === parseInt(args.id));
      if (updatedUser) {
        if (args.name) updatedUser.name = args.name;
        if (args.age) updatedUser.age = args.age;
      }
      return updatedUser;
    },
    deleteUser: (parent, args) => {
      const userIndex = users.findIndex(user => user.id === parseInt(args.id));
      if (userIndex === -1) return null;
      const deletedUser = users[userIndex];
      users.splice(userIndex, 1);
      return deletedUser;
    },
  },
};

// Apollo Server instance
const server = new ApolloServer({
  typeDefs,
  resolvers,
});

// Start the server
server.listen().then(({ url }) => {
  console.log(`🚀 Server ready at ${url}`);
});
