Airbnb Clone - Console



Overview


Welcome to the Airbnb Clone Console, a project designed to create and manage data objects for accommodation listings in a
simplified command-line environment. This console serves as a powerful tool for manipulating objects by providing
functionalities for creating, updating, and destroying data objects while seamlessly persisting them to a JSON file.



Features


Data Model Creation:
        Define and create your data model for accommodation listings.

Command Interpreter:
        Utilize a command interpreter to manage objects efficiently.
        Implement commands for creating, updating, deleting, and querying data objects.
        Supports both interactive and non-interactive modes.

Object Storage and Persistence:
        Store and persist created objects to a JSON file.
        Abstract away storage details, providing a separation between the manipulation of objects and their underlying 
        storage.

Flexibility:
        Easily change the storage engine without modifying the codebase, thanks to the abstraction layer.
        Ensure that updates to the storage mechanism don't impact the console, front-end, or RestAPI components.



Getting Started


    Clone the repository:

    bash

git clone https://github.com/your-username/airbnb-clone-console.git

Navigate to the project directory:

bash

cd airbnb-clone-console

Run the console interactively:

bash

    ./console.py

    Start using the console commands to create, update, and manage accommodation listings.

Interactive Mode:


bash

$ ./console.py
(Airbnb Console) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(Airbnb Console) 
(Airbnb Console) 
(Airbnb Console) quit
$


Non-Interactive Mode:


bash

$ echo "help" | ./console.py
(Airbnb Console)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(Airbnb Console) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(Airbnb Console)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(Airbnb Console) 
$


Usage


Console Commands:

    create <object_type>: Create a new object of the specified type.
    update <object_type> <object_id>: Update an existing object.
    destroy <object_type> <object_id>: Delete an object.
    show <object_type> <object_id>: Display details of a specific object.
    all <object_type>: List all objects of a particular type.
    quit or EOF: Exit the console.


Example Usage:


bash

$ ./console.py
Airbnb Console - Type 'quit' or 'EOF' to exit.

(Airbnb Console) create Place
Place.created: <place_id>

(Airbnb Console) update Place <place_id> name "Cozy Cottage"
Place.updated: <place_id>

(Airbnb Console) show Place <place_id>
{
    "id": "<place_id>",
    "name": "Cozy Cottage",
    ...
}

(Airbnb Console) all Place
[
    {
        "id": "<place_id>",
        "name": "Cozy Cottage",
        ...
    },
    ...
]

(Airbnb Console) quit
$
