# Learning Management System API 📚 🎓 💻 📈

Learning Management System API built with Django. Database agnostic but I've used MySQL. All IDs use UUIDv4. It has middleware for request validation.

## Technologies Used

- **Django**

Django is a high-level Python web framework that encourages rapid development. It facilitates the development of complex, database-driven websites. It emphasizes reusability and "pluggability" of components, less code, low coupling, and rapid development. It comes with a variety of features such as ORM, admin panel, and various security features.

- **MySQL**

MySQL is an open-source relational database management system (RDBMS) that is widely used for building web-based applications. It is known for its reliability, scalability, and ease of use. MySQL uses SQL (Structured Query Language) for querying and managing databases. It supports various storage engines, including InnoDB, MyISAM, and others, each with its own strengths. It is optimized for performance, with features such as indexing, caching, and query optimization to improve database performance.

<img src='https://github.com/dragan717080/DjangoMySQLLMS/assets/135660124/f1c06c0b-b7c6-48d7-8781-96f127c44247' alt='Schema Image' width='670' height='310' />

## Example endpoint

**Create**

```POST /lessons```

```
{
    "title": "Basics of Computer Science",
    "content": "Fundamental concepts in computer science.",
    "module_id": "6d3fd4be-0977-4e67-af01-96eaaa1a5963",
    "order": 2
}
```

Returns

```
201 SUCCESS

{
    "id": "e94fc211-acf4-4e1e-aa98-b4ce8947419e",
    "title": "Basics of Computer Science",
    "content": "Fundamental concepts in computer science.",
    "module_id": "6d3fd4be-0977-4e67-af01-96eaaa1a5963",
    "order": 2
}
```

**Read**

```GET /lessons```

Returns

```
200 SUCCESS

[
    {
        "id": "57f67b18-4d39-49c8-bcaf-1c13a0e45c62",
        "title": "Introduction to Programming Languages",
        "content": "Overview of programming languages and their uses.",
        "module_id": "6d3fd4be-0977-4e67-af01-96eaaa1a5963",
        "order": 1
    },
    {
        "id": "e94fc211-acf4-4e1e-aa98-b4ce8947419e",
        "title": "Basics of Computer Science",
        "content": "Fundamental concepts in computer science.",
        "module_id": "6d3fd4be-0977-4e67-af01-96eaaa1a5963",
        "order": 2
    }
]
```

```GET /lessons/{id}```
**id: unique identifier in UUIDv4 format**

Returns

```
200 SUCCESS

{
    "id": "8cb684a8-3670-47cc-a836-a787cb1d4220",
    "title": "Introduction to Programming Languages",
    "content": "Overview of programming languages and their uses.",
    "module_id": "6d3fd4be-0977-4e67-af01-96eaaa1a5963",
    "order": 1
}
```

**Update**

```PATCH /lessons/{id}```

```
{
    "title": "Variables and Data Types",
    "content": "Understanding variables and different data types."
}
```

Returns
```
200 SUCCESS

{
    "id": "e94fc211-acf4-4e1e-aa98-b4ce8947419e",
    "title": "Variables and Data Types",
    "content": "Understanding variables and different data types.",
    "module_id": "6d3fd4be-0977-4e67-af01-96eaaa1a5963",
    "order": 1
}
```

**Delete**

```DELETE /lesson/{id}```

Returns

```
200 SUCCESS

{
    "message": "Deleted lesson with id e94fc211-acf4-4e1e-aa98-b4ce8947419e"
}
```
