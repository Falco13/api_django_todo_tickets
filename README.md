# REST API application - Django: Todo tickets

- Tickets for users. The ticket consists of: Title, Task text, Status (dynamic for the admin), ticket author, who the ticket is assigned to, creation date, update date, image (there may be more than one).
- Implemented the ability to add an Image to a ticket.
- The user can only edit and delete their own tickets.
- Only the ticket author and the person to whom the ticket is assigned can change the Status of a ticket.
- The list of all tickers is available only to authorized users, with the ability to filter by Status.
- Implemented the ability to write comments, as well as write comments on comments.

__API end-points:__
- /api/auth/
- /api/
- /api/todos/
- /api/todos/add
- /api/todos/id
- /api/check_status/id
- /api/upload_image
- /api/add_comment


__Used tools:__    
:heavy_check_mark: Python     
:heavy_check_mark: Django REST Framework      
:heavy_check_mark: Django REST framework filter     
:heavy_check_mark: SQLite database    
