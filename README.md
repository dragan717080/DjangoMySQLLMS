# Learning Management System API 📚 🎓 💻 📈

Learning Management System API built with Django. Database agnostic but I've used MySQL. All IDs use UUIDv4. It has middleware for request validation.

## Technologies Used

- **Django**

Django is a high-level Python web framework that encourages rapid development. It facilitates the development of complex, database-driven websites. It emphasizes reusability and "pluggability" of components, less code, low coupling, and rapid development. It comes with a variety of features such as ORM, admin panel, and various security features.

- **MySQL**

MySQL is an open-source relational database management system (RDBMS) that is widely used for building web-based applications. It is known for its reliability, scalability, and ease of use. MySQL uses SQL (Structured Query Language) for querying and managing databases. It supports various storage engines, including InnoDB, MyISAM, and others, each with its own strengths. It is optimized for performance, with features such as indexing, caching, and query optimization to improve database performance.

<img src='https://github.com/dragan717080/DjangoMySQLLMS/assets/135660124/f1c06c0b-b7c6-48d7-8781-96f127c44247' alt='Schema Image' width='670' height='310' />

## Example endpoint

**Read**

```GET /lessons```

Returns

```
200 SUCCESS
[
    {
        "id": "8cb684a8-3670-47cc-a836-a787cb1d4220",
        "title": "Introduction to Programming Languages",
        "content": "Overview of programming languages and their uses.",
        "module_id": "6d3fd4be-0977-4e67-af01-96eaaa1a5963",
        "order": 1
    },
    {
        "id": "af19a8a8-651d-47b0-b28c-2a6ce9e3d902",
        "title": "Basics of Computer Science",
        "content": "Fundamental concepts in computer science.",
        "module_id": "6d3fd4be-0977-4e67-af01-96eaaa1a5963",
        "order": 2
    }
]
```

