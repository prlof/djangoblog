In our blog
 
Features 
==========
Blog will have the following features

1- Post
2- Categories
3- Tag
4- Author

Relation between tables
=======================

1- Post can have many categories, a  category can have many posts
(Relation Post <-> Categories : ManyToMany)
2- A tag can have many posts and a post can have many tags
(Relation Post <-> Tag : ManyToMany)
3- Author can have many posts, a post post have one author
(Relation Author <-> Post : OneToMany)

Attributes for tables
=====================

Post(title, created_date, body, tags, categories, author)
Categories(cat_name, cat_description)
Author(name, email:not mandatory, bio)
Tag(name, tag_description)

