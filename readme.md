# Palnetly Task

in the following repo you can find the implementation for the recruitment task.

I used django with django-rest-framework for implementing it.

I used Knox for the authentication.rest_framework

I used rest_framework.filters for filtering the data.

It took me 5 hours to implement the task.

you can run it using docker-compose `docker-compose up`

## endpoints

you can register on `api/register`

you can login on `api/login`

you can logout on `api/logout`

you can do CRUD on 

```
/users
/usage
/usage_types
```

filtering is available by url (id), query parms, searching for the name fields 