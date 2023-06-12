
<h1> </title>Project: AirBnB clone - The console </title></h1>
   
<p>
  <img src="https://www.google.com/url?sa=i&amp;url=https%3A%2F%2Fmedium.com%2Fkeycafe%2Fthe-history-of-airbnb-397c3d539f27&amp;psig=AOvVaw2xG-eHGr0dj1p8JV71h6wv&amp;ust=1686696070369000&amp;source=images&amp;cd=vfe&amp;ved=0CBAQjRxqFwoTCLiG1djmvv8CFQAAAAAdAAAAABAQ" alt="" loading="lazy" style="" />
</p>


<h4>Description</h4>

<p>This is the first step <strong>a command interpreter to manage our AirBnB objects</strong> towards building our first full web application: the <strong>AirBnB clone</strong>.  We will use what we built in this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration… </p>

<p>About</p>

<ul>
<li>We put in place a parent class (called <code>BaseModel</code>) to take care of the initialization, serialization and deserialization of your future instances</li>
<li>We created a simple flow of serialization/deserialization: Instance &lt;-&gt; Dictionary &lt;-&gt; JSON string &lt;-&gt; file</li>
<li>we created all classes used for AirBnB (<code>User</code>, <code>State</code>, <code>City</code>, <code>Place</code>&hellip;) that inherit from <code>BaseModel</code></li>
<li>We created the first abstracted storage engine of the project: File storage. </li>
<li>We created all unittests to validate all our classes and storage engine</li>
</ul>

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

Dillinger is currently extended with the following plugins.
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

