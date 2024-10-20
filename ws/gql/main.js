const { ApolloServer, gql } = require('apollo-server');
const fs = require('fs');
const path = require('path');

const dataFilePath = path.join(__dirname,'data.json');

const readData = () => {
    const data = fs.readFileSync(dataFilePath,'utf-8');
    return JSON.parse(data);
}


const writeData = (data) =>{
    fs.writeFileSync(dataFilePath,JSON.stringify(data,null,2),'utf-8');
}

let users = readData();


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


const resolvers = {
    Query: {
        users: ()=> users,
        user: (parent, args) => users.find(user => user.id === parseInt(args.id))
    },

    Mutation: {
        createUser: (parents, args) => {
            const newUser = {
                id: users.length + 1,
                name: args.name,
                age: args.age
            }

            users.push(newUser)
            writeData(users);
            return newUser
        },

        updateUser: (parents, args) => {
            const current = users.find(user => user.id === parseInt(args.id));

            current.id = args.id
            current.name = args.name
            current.age = args.age
            writeData(users);
            return current
        },

        deleteUser: (parents, args) => {
            const current = users.findIndex(user => user.id === parseInt(args.id));
            users.pop(current);
            writeData(users);
            return users
        }
    }
}

const server = new ApolloServer({
    typeDefs,
    resolvers
});

server.listen().then(({ url }) => {
    console.log(`🚀 Server ready at ${url}`);
  });
