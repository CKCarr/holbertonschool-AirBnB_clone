
<h1> Project: AirBnB clone - The console </h1>

<p>
  <img src="https://miro.medium.com/v2/resize:fit:828/0*NChTo-XqLOxLabIW" alt="Logo_Airbnb" loading="lazy" style="" />
</p>


<h3>Description</h3>

<p>This is the first step <strong>a command interpreter to manage our AirBnB objects</strong> towards building our first full web application: the <strong>AirBnB clone</strong>.  We will use what we built in this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration… </p>

<p>About</p>

<ul>
<li>We put in place a parent class (called <code>BaseModel</code>) to take care of the initialization, serialization and deserialization of your future instances</li>
<li>We created a simple flow of serialization/deserialization: Instance &lt;-&gt; Dictionary &lt;-&gt; JSON string &lt;-&gt; file</li>
<li>we created all classes used for AirBnB (<code>User</code>, <code>State</code>, <code>City</code>, <code>Place</code>&hellip;) that inherit from <code>BaseModel</code></li>
<li>We created the first abstracted storage engine of the project: File storage. </li>
<li>We created all unittests to validate all our classes and storage engine</li>
</ul>


<h3>Diagram AirBnB clone (The Console)</h3>

<p>
  <img src="https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2018/6/815046647d23428a14ca.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20230615%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20230615T210513Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=067d0a1d183e0e3f2cfc218292f4a1339cc1bb3850dcc100b5ab9c3ac17801b8" alt="console_Airbnb" loading="lazy" style="" />
</p>


<h3>Files in this Repository</h3>

| No. | File               | File Hierarchy                          | Description                                    |
|-----|--------------------|-----------------------------------------|------------------------------------------------|
| 1   | console.py         |                                         | The main console, command interpreter (EOF, all, create, destroy, help, quit, show, update.) |
| 2   | Authors            |                                         | File with the name of Authors                  |                          
| 3   | README.md          |                                         | Readme file proyect                            |
| 4   | '__init__.py'        | models/__init__.py                      | File to mark a directory as a package          |
| 5   | amenity.py         | models/amenity.py                       | The amenity subclass                           |
| 6   | base_model.py      | models/base_model.py                    | Defines all common attributes/methods for other classes |
| 7   | city.py            | models/city.py                           | The city subclass                              |
| 8   | place.py           | models/place.py                          | The place subclass                             |
| 9   | review.py          | models/review.py                         | The review subclass                            |
| 10  | state.py           | models/state.py                          | The state subclass                             |
| 11  | user.py            | models/user.py                           | The user subclass                              |
| 12  | __init__.py        | models/engine/__init__.py                | File to mark a directory as a package          |
| 13  | file_storage.py    | models/engine/file_storage.py            | The file storage class                         |
| 14  | test_amenity.py    | tests/test_models/test_amenity.py        | The unittest module for amenity                |
| 15  | test_base_model.py | tests/test_models/base_model.py          | The unittest module for base model             |
| 16  | test_city.py       | tests/test_models/city.py                | The unittest module for city                   |
| 17  | test_place.py      | tests/test_models/place.py               | The unittest module for place                  |
| 18  | test_review.py     | tests/test_models/review.py              | The unittest module for review                 |
| 19  | test_state.py      | tests/test_models/state.py               | The unittest module for state                  |
| 20  | test_user.py       | tests/test_models/user.py                | The unittest module for user                   |
| 21  | '__init__.py'        | tests/test_models/test_engine/__init__.py | File to mark a directory as a package         |
| 22  | test_file_storage.py| tests/test_models/test_engine/test_file_storage.py | The unittest module for file storage   |


<h2>How to Use Console</h2>

<h3>Execution</h3>

<p>The console in interactive mode:</p>

<pre><code>/holbertonschool-AirBnB_clone#  ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb)

</code></pre>

<p>To use in non-interactive mode: </p>

<pre><code> /holbertonschool-AirBnB_clone# echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb)
</code></pre>

<p>help command use: </p>

<pre><code> 
(hbnb)
(hbnb) help destroy

        Deletes an instance based on the
        class name and id, and saves the change into
        the JSON file.

(hbnb) help EOF
Exit command to exit the program
(hbnb)
</code></pre>


## Commands in terminal

Instructions on how to use them in your own application are linked below.

| Command | Description |
| ------ | ------ |
| Quit | Quit the Prompt |
| Help | Display help the console |
| Create | Create New object |
| Show | Show the info object |
| All | Display All objects |
| Update | Update objects |
| Destroy | Destroy Objects |


## AUTHORS

<br>Crystal Carrillo <6108@holbertonstudents.com>
<br>Carlos Alarcon   <6138@holbertonstudents.com>

