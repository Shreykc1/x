let users = [
    {  id:1,  name: "Shrey", age: "20" },
    {  id:2,  name: "Billionaire", age: "30" }
]

const resolvers = {
    Query:{
        users: () => users,
        user: (parents, args) => users.find(user => user.id === parseInt(args.id))
    },

    Mutation:{
        createUser:(parents, args) =>{
            const newUser = {
                id: users.length + 1,
                name: args.name,
                age: args.age
            }
            users.push(newUser);
            return newUser;
        },

        updateUser:(parents, args) =>{
            const current = users.find(user => user.id === parseInt(args.id));

            if (current){
                if(args.name) current.name = args.name;
                if (args.age) current.age = args.age;
            }

            return current
        },

        deleteUser:(parents, args)=>{
            const current = users.findIndex(user => user.id === parseInt(args.id));
            if (current) users.pop(current);

            return users
        }
    }
}

module.exports = {
    resolvers
}
