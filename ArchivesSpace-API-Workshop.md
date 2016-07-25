
# Introducing the ArchivesSpace REST API using Python 3

+ [R. S. Doiel](https://rsdoiel.github.io)
    + [Digital Services Programmer](https://caltechlibrary.github.io)
    + Caltech Library
+ [Mark Custer](https://github.com/fordmadox)
    + [Archivist and Metadata Coordinator](https://resources.library.yale.edu/StaffDirectory/detail.aspx?q=702)
    + Beinecke Rare Book and Manuscript Library
    + Yale University Library

[Download these slides and examples](https://github.com/rsdoiel/archivesspace-api-workshop/releases/latest)

--

# Introducing the ArchivesSpace REST API using Python 3

Before we begin ...

## Required

+ A laptop/device with network access
    + e.g. Linux (what I use), Mac OS X (which I am familiar with), or Windows (which I am very very rusty on)
+ Python 3.5 installed including the python standard library (see https://docs.python.org/3/library/)
    + Python 3 (v3.5.2) can be downloaded and from https://www.python.org/downloads/
+ A text editor
    + *IDLE for Python 3* is fine for the workshop
+ A web browser
    + Firefox or Chrome with the [JSONView](https://jsonview.com/) plugin recommended
+ A test deployment ArchivesSpace is being provided as part of the Workshop
    + Or you can install your own via [VirtualBox and Vagrant](./archivesspace-dev/)
+ A basic familiarity with Python and ArchivesSpace

## Suggested

+ Bookmark in your web browser:
    + [ArchivesSpace API Docs](http://archivesspace.github.io/archivesspace/api/)
    + [Python Reference](https://docs.python.org/3/library/index.html)
    + [This presentation website](https://rsdoiel.github.io/archivesspace-api-workshop)
+ Recommended reading
    + Read through the [Python 3 tutorial](https://docs.python.org/3/tutorial/index.html) if they are not familiar with Python.

--

# Introducing the ArchivesSpace REST API using Python 3

## Workshop structure

1. Setup
2. Making an http connection
3. Authentication
4. Working with Repositories
5. Working with Agents
6. Working with Accessions
7. Other ArchivesSpace Models

--

# 1. Setup

## your web browser

Open the following in your web browser tabs

+ [rsdoiel.github.io/archivesspace-api-workshop/00-ArchivesSpace-API-Workshop.html](https://rsdoiel.github.io/archivesspace-api-workshop/00-ArchivesSpace-API-Workshop.html)
+ ArchivesSpace API docs [archivesspace.github.io/archivesspace/api/](http://archivesspace.github.io/archivesspace/api/)

--

# 1. Setup

## ArchivesSpace

+ Our hosts have provided us with test deployments of ArchivesSpace
    + See hand out or whiteboard for connection details
+ Make sure you can access ArchivesSpace Web UI from your web browser
    + usually http://localhost:8080 in the docs
+ Make sure you can access ArchivesSpace API from your web browser
    + usually http://localhost:8089 in the docs

--

# 1. Setup

## ArchivesSpace

1. Point your web browser at the ArchivesSpace web UI
2. Make sure you can login
3. In another browser tab point your web browser the API URL

--

# 1. Setup

## Python Development Environment

+ Start IDLE for Python 3.5
    + confirm the reported version is 3.5.1 or better

--

# 1. Setup

## About the code

The basic organization is as follows

1. import block
2. define some functions
3. and a `if __name__ == '__main__':` block at the end
    + this *if* block is where our tests go

--

# 1. Setup

## About the code

### The import block

This stock import block, as we'll see in the coming code, doesn't change much.

```python
    #!/usr/bin/env python3
    import urllib.request
    import urllib.parse
    import urllib.error
    import json
    import getpass
```

To keep the workshop simple we're only using these standard
libraries. The others we add we'll be writing ourselves.

--

# 1. Setup

## About the code

### The functions we define

In The middle section we will add our functions. Between each section of
the workshop we'll copy the previous code forward to a new file.
We will redefine and adding as we move through the API.  The goal isn't to
have allot of files but to allow you to see how the code evolves overtime
into a python module.

--

# 1. Setup

## About the code

### The closing *if* block

At the end of each of our Python scripts there will be an *if* block.
This is where our test code goes. For the purposes of the workshop we
will minimize what is inside this *if* block.  Normally you would
keep all your tests available (probably written as their own functions,
possibly as a separate included module).

--

# 1. Setup

## About the code

This [helloworld.py](helloworld.py) is typical of the scripts we will
wind up with.

```python
    #!/usr/bin/env python3
    import urllib.request
    import urllib.parse
    import urllib.error
    import json
    import getpass
    # additional modules get added here.

    # This is where we add our functions
    def hello_world():
        return 'Hello World!!!'

    # This is where we put our tests
    if __name__ == '__main__':
        hw = hello_world()
        if hw == 'Hello World!!!':
            print('Success!! -> ', hw)
        else:
            print('Ooops something went wrong!!!"')
```

You shold see "Success!! -> Hello World!!!" when you run the program.

--

# 2. Make an http connection

<blockquote>But when are we going to write some code?</blockquote>

Up next, these three things

+ using the Python interpreter
+ import the standard modules we'll use in the workshop
    + i.e. urllib.request, getpass, json
+ make a connection with the request object

--

# 2. Make an http connection

## Let's get started

At this point your setup should be completed and we're
going to start working in the Python shell via IDLE.

IDLE is python's integrated development environment that
comes standard with Python distributions.

--

# 2. Make an http connection

## launch python

From a terminal on Linux I type ...

```shell
    idle-python3.5
```

On Mac OS X or Windows you'll need to ...

1. find your Python 3.5.2 installation folder.
2. find **idle**, click/double click to start it.

--

# 2. Make an http connection

## Recap and quick check

Before we continue you should have the following
running ...

+ ArchivesSpace
+ Your web browser
+ Python via IDLE

--

# 2. Make an http connection

## import modules

Once **idle** starts it'll launch a Python Shell (also known as a Repl).

Type the following in the shell.

```python
    import urllib.request
    import urllib.parse
    import urllib.error
    import json
    import getpass
```

These are the three modules we'll use through out our Workshop.

--

# 2. Make an http connection

## Create a request object

Continue in the Python shell and add

```python
    api_url = 'http://localhost:8089'
    req = urllib.request.Request(api_url)
```

You will need to replace "http://localhost:8089" with your
Workshop API URL.

The goal is to create a **Request** object named *req*.

--

# 2. Make an http connection

## Make the request, print results

Now we can send our *req* and get back a *response*.

```python
    response = urllib.request.urlopen(req)
    print(response.read().decode('UTF-8'))
```

--

# 2. Make an http connection

+ What do you see?
+ Are there questions?

--

# 2. Make an http connection

## Putting it all together

Let's take what we learned and create a Python scripts called
[make-an-http-connection.py](make-an-http-connection.py).

```python
    #!/usr/bin/env python3
    import urllib.request
    import json
    import getpass

    api_url = input('ArchivesSpace API URL: ')
    req = urllib.request.Request(api_url)

    response = urllib.request.urlopen(req)
    print(response.read().decode('utf-8'))

```
1. In IDLE click on the file name and create a new file
2. Type in the above
3. Save the file as [make-an-http-connection.py](make-an-http-connection.py)

--

# 2. Make an http connection

## Once you've save your script

1. In the editors' menu click "Run"
2. click "Run Check"
3. click "Run module"

We'll be doing this often as we evolve our scripts.

--

# 2. Make an http connection

## If all gone well

1. The shell will have a message saying "RESTART"
2. You'll be prompted for the ArchivesSpace API URL
3. After entering it you'll see the JSON blob response below.

```shell
    RESTART: /home/rsdoiel/Sites/archivespace-api-workshop/make-an-http-connection.py
    ArchivesSpace API URL: http://localhost:8089
    {
       "databaseProductName": "MySQL",
       "databaseProductVersion": "5.6.31",
       "ruby_version": "1.9",
       "host_os": "linux",
       "host_cpu": "x86_64",
       "build": "java1.6",
       "archivesSpaceVersion": "v1.5.0"
    }
```

Now we should be ready to learn how to authenticate with the API.

--

# 3. Authentication

## Basic ingredients

+ Make an http connection
+ Send our username and pasword to the API
+ Save the access token returned

--

# 3. Authentication

## Send our username and password

We need pass our username and password in our request.
We need to keep track of the response.

Close the text editor and go back in the shell.

```python
    username = input('username (e.g. admin): ')
    password = getpass.getpass('password: ')
```

We want to use getpass.getpass('password: ') so the
password doesn't get echoed to the screen. In IDLE it'll
show read and echo the password, ignore this for testing
and development.

--

# 3. Authentication

## Send our username and password

Encode our password for sending with our request.

```python
    data = urllib.parse.urlencode({'password': password})
    data = data.encode('utf-8')
```

--

# 3. Authentication

# Send our username and password

Now send a request with our data.

```python
    req = urllib.request.Request(
        url = api_url+'/users/'+username+'/login',
        data = data)
    response = urllib.request.urlopen(req)
    print(response.read().decode('UTF-8'))
```

You should see content from the response ArchivesSpace send back.

--

# 3. Authentication

## Send our username and password

### Putting it all together

Open the IDLE text editor and create a new file
called **login.py**.

We'll create a python function and add prompts for api url,
username and password to test it. Note the additional *urllib* modules
imported.

```python
    #!/usr/bin/env python3
    import urllib.request
    import urllib.parse
    import urllib.error
    import getpass

    def login (api_url, username, password):
        '''This function logs into the ArchivesSpace REST API and shows the text response'''
        data = urllib.parse.urlencode({'password': password})
        data = data.encode('ascii')
        req = urllib.request.Request(
            url = api_url+'/users/'+username+'/login',
            data = data)
        response = urllib.request.urlopen(req)
        status = response.getcode()
        print('HTTP status code', status)
        return response.read().decode('UTF-8')

    if __name__ == '__main__':
        api_url = input('ArchivesSpace API URL: ')
        username = input('ArchivesSpace username: ')
        password = getpass.getpass('ArchivesSpacew password: ')
        print('Logging in', api_url)
        s = login(api_url, username, password)
        print(s)
        print('Success!')
```

Now "Run" the python script and see the results like we did before.

--

# 3. Authentication

## Let's a closer look at the JSON results

Example results [model-examples/response.json](model-examples/login-response.json)

## Save the access token returned

We need to parse the JSON data into a Python object
so we can save our access token.

```json
    {   
       "session": "84467334ce001b924b0e6d529edf99e383.5.271d4238177ab2e811dc5ac9e5a",
       ...
    }
```

The session value is our access token. We can pluck that single
item out easiest if we turn the JSON blob into a Python variable.

--

# 3. Authentication

## Save the access token returned

We need to modify our login function to "decode" the JSON
response and return only session value. We'll also update our
tests at the bottom.  (We're modifying *login* function and the
testing in the closing *if* block)

```python
    #!/usr/bin/env python3
    import urllib.request
    import urllib.parse
    import urllib.error
    import json
    import getpass
        
    def login (api_url, username, password):
        '''This function logs into the ArchivesSpace REST API returning an acccess token'''
        data = urllib.parse.urlencode({'password': password}).encode('utf-8')
        req = urllib.request.Request(
            url = api_url+'/users/'+username+'/login', 
            data = data)
        try:
            response = urllib.request.urlopen(req)
        except HTTPError as e:
            print(e.code)
            print(e.read())
            return ""
        except URLError as e:
            print(e.reason())
            return ""
        src = response.read().decode('utf-8')
        result = json.JSONDecoder().decode(src)
        # Session holds the value we want for auth_token
        return result['session']
    
    if __name__ == '__main__':
        api_url = input('ArchivesSpace API URL: ')
        username = input('ArchivesSpace username: ')
        password = getpass.getpass('ArchivesSpacew password: ')
        print('Logging in', api_url)
        auth_token = login(api_url, username, password)
        print(auth_token)
        if auth_token != '':
            print('Success!')
        else:
            print('Ooops! something went wrong')
```

This is our first module and will get reused in **repo.py**, **agent.py**
and **accession.py**.  I've added some extra handling around *urlopen*.  
This will give us a little more orderly output when something goes wrong
in the http request.

If all has gone well we are ready to move onto working with repositories!

--

# 4. Repositories

## What we'll do in this section

+ Create some repositories
+ List the available repositories
+ List a specific repository
+ Update a repository
+ Delete a repository

--

# 4. Repositories

Creating a repository requires

+ login to API with appropriate account (e.g. admin)
+ package a request to create a repository
+ send the request to create the repository
+ saving the response from the create request

We repeat the process to create multiple repositories.

--

# 4. Repositories

## The details we need to know

+ Go to [AS REST API docs](http://archivesspace.github.io/archivesspace/api/#get-repositories)
    + We're interested in "Create a Repository"
        + use your browser's find function
+  Look at the example **curl** request on the right


```shell
    curl -H "X-ArchivesSpace-Session: $SESSION"
    -d {
       "jsonmodel_type": "repository",
       "name": "Description: 11",
       "repo_code": "ASPACE REPO 2 -- 631024",
       "org_code": "970UV228G",
       "image_url": "http://www.example-3.com",
       "url": "http://www.example-4.com"
    }
    'http://localhost:8089/repositories'
```

(the bit after the "-d" is what we're interested in.)

--

# 4. Repositories

## Creating our create_repo function

The elements we change with each new create request will
form the parameters in our function. Two elements are required
and the rest are optional.

### required

+ name
+ repo_code (needs to be unique)

### optional

+ org_code
+ image_url
+ url

### What we also need

We will need to submit our access token and provide the api url too

--

# 4. Repositories

Did we catch all the fields we might want to change?

```json
    {
       "jsonmodel_type": "repository",
       "name": "Description: 11",
       "repo_code": "ASPACE REPO 2 -- 631024",
       "org_code": "970UV228G",
       "image_url": "http://www.example-3.com",
       "url": "http://www.example-4.com"
    }
```

Do we need to change "jsonmodel_type"?

--

# 4. Repositories

## Creating the **repo.py** module

1. Create a new file called [repo.py](repo.py)
2. Include our usual import block
3. Add `import login` to the list

We're going to be adding a *create_repo* function and modifying the
testing in the *if* block.

--

# 4. Repositories

Lets create our **create_repo** function.

Similar to our *login()* we need to create a data package,
a request object and with "urlopen" send our request so we can
get a response.

```python
def create_repo(api_url, auth_token, name, repo_code, org_code = '', image_url = '', url = ''):
        '''This function sends a create request to the ArchivesSpace REST API'''
        data = json.JSONEncoder().encode({
                        'jsonmodel_type': 'repository',
                        'name': name,
                        'repo_code': repo_code,
                        'org_code': org_code,
                        'image_url': image_url,
                        'url': url
                    }).encode('utf-8')
        req = urllib.request.Request(
                url = api_url+'/repositories', 
                data = None, 
                headers = {'X-ArchivesSpace-Session': auth_token})
        try:
            response = urllib.request.urlopen(req, data)
        except HTTPError as e:
            print(e.code)
            print(e.read())
            return ""
        except URLError as e:
            print(e.reason())
            return ""
        src = response.read().decode('utf-8')
        return json.JSONDecoder().decode(src)
```

--

# 4. Repositories

Notice how similar it is to our **login** function. Also how we
add the header to pass along our *auth_token* with our request.
Some of the important differences are

+ We're encoding *data* as JSON instead of urlencoding.
+ We've added an *auth_token* as a header parameter in the *Request*
+ *data* is passed via *urlopen* rather than in our *Request* object

```python
    def create_repo(api_url, auth_token, name, repo_code, org_code = '', image_url = '', url = ''):
        '''This function sends a create request to the ArchivesSpace REST API'''
        data = json.JSONEncoder().encode({
                        'jsonmodel_type': 'repository',
                        'name': name,
                        'repo_code': repo_code,
                        'org_code': org_code,
                        'image_url': image_url,
                        'url': url
                    }).encode('utf-8')
        req = urllib.request.Request(
                url = api_url+'/repositories', 
                data = None, 
                headers = {'X-ArchivesSpace-Session': auth_token})
        try:
            response = urllib.request.urlopen(req, data)
        except HTTPError as e:
            print(e.code)
            print(e.read())
            return ""
        except URLError as e:
            print(e.reason())
            return ""
        src = response.read().decode('utf-8')
        return json.JSONDecoder().decode(src)
```

You can copy and paste your def from our text editor to the repl and make
sure it compiles.


--

# 4. Repositories

Putting it all together, add the following after the *login* function and
update the *if* block to match.

```python
    #!/usr/bin/env python3
    import urllib.request
    import urllib.parse
    import urllib.error
    import json
    import getpass
    # Here's our own login module
    import login
    
    
    def create_repo(api_url, auth_token, name, repo_code, org_code = '', image_url = '', url = ''):
        '''This function sends a create request to the ArchivesSpace REST API'''
        data = json.JSONEncoder().encode({
                        'jsonmodel_type': 'repository',
                        'name': name,
                        'repo_code': repo_code,
                        'org_code': org_code,
                        'image_url': image_url,
                        'url': url
                    }).encode('utf-8')
        req = urllib.request.Request(
                url = api_url+'/repositories', 
                data = None, 
                headers = {'X-ArchivesSpace-Session': auth_token})
        try:
            response = urllib.request.urlopen(req, data)
        except HTTPError as e:
            print(e.code)
            print(e.read())
            return ""
        except URLError as e:
            print(e.reason())
            return ""
        src = response.read().decode('utf-8')
        return json.JSONDecoder().decode(src)
    
    
    if __name__ == '__main__':
        # Test login
        print("Testing login()")
        api_url = input('ArchivesSpace API URL: ')
        username = input('ArchivesSpace username: ')
        password = getpass.getpass('ArchivesSpace password: ')
        print('Logging in', api_url)
        auth_token = login.login(api_url, username, password)
        print("auth token", auth_token)
        if auth_token != '':
            print('Success!')
        else:
            print('Ooops! something went wrong')
            sys.exit(1)
    
        # Test create_repo
        print('Testing create_repo()')
        print('Create your first repository')
        name = input('Repo name: ')
        repo_code = input('Repo code: ')
        repo = create_repo(api_url, auth_token, name, repo_code)
        print(json.dumps(repo, indent=4))
        print('Create a second repository')
        name = input('Repo name: ')
        repo_code = input('Repo code: ')
        repo = create_repo(api_url, auth_token, name, repo_code)
        print(json.dumps(repo, indent=4))
```

--

# 4. Repositories

## Adding a new list_repo function

Like *login* and *create_repo* this function needs to contact the API.
But the data we send is less. We need

+ Our api_url and auth_token
+ We need the URL path for listing repositories
    + How do we find that path?

--

# 4. Repositories

## ArchivesSpace API Docs

The documentation about the API will help us know what to ask.

+ Change to your browser tab with the docs
+ Using your web browser's find function search for
    + "Get a list of Repositories"

The **curl** statement suggested looks like

```shell
    curl -H "X-ArchivesSpace-Session: $SESSION" \
        'http://localhost:8089/repositories'
```

Notice there is no "-d" listed. We only need to know the
API URL and then add "/repositories" to it. We still need
to send along our auth token in the header as normal.

--

# 4. Repositories

## Let's give this a try in the shell

We may need a fresh *auth_token* so let's login first.
After that we can build our request and send it. We'll
wrap up by decoding the JSON response and pretty printing
it.

```python
    auth_token = login(api_url, username, password)
    req = urllib.request.Request(
        url = api_url+'/repositories',
        data = None,
        header = {"X-ArchivesSpace-Session": auth_token})
    response = urllib.request.urlopen(req)
    result = json.JSONDecoder().decode(response.read().decode('utf-8'))
    print(json.dumps(result, indent=4))
```

+ How are the results organized?
+ How does this compare with the API document?

--

# 4. Repositories

## Time to put this together in a script

Add *list_repos* function after *create_repo* and update the testing
section at the bottom.

In the definition section add

```python
    def list_repos(api_url, auth_token):
        '''List all the repositories, return the listing object'''
        req = urllib.request.Request(
            url = api_url+'/repositories',
            data = None,
            headers = {'X-ArchivesSpace-Session': auth_token})
        try:
        response = urllib.request.urlopen(req)
        except HTTPError as e:
            print(e.code)
            print(e.read())
            return None
        except URLError as e:
            print(e.reason())
            return None
        src = respone.read().decode('utf-8')
        return json.JSONDecoder().decode(src)
```

In the test *if* block add

```python
        # Test list_repos()
        repos = list_repos(api_url, auth_token)
        print("repositores list", json.dumps(repos, indent=4))
```

(note: the "..." that is just a place holder for the previous tests
added)

We've added our *list_repos* and changed the tests at the bottom.

--

# 4. Repositories

## results should look something like

```json
    [
        {
            "last_modified_by": "admin",
            "created_by": "admin",
            "create_time": "2016-07-17T01:55:21Z",
            "agent_representation": {
                "ref": "/agents/corporate_entities/1"
            },
            "repo_code": "test001",
            "name": "test001",
            "lock_version": 0,
            "system_mtime": "2016-07-17T01:55:21Z",
            "user_mtime": "2016-07-17T01:55:21Z",
            "jsonmodel_type": "repository",
            "uri": "/repositories/2"
        },
        {
            "last_modified_by": "admin",
            "created_by": "admin",
            "create_time": "2016-07-17T01:55:42Z",
            "agent_representation": {
                "ref": "/agents/corporate_entities/2"
            },
            "repo_code": "test002",
            "name": "test002",
            "lock_version": 0,
            "system_mtime": "2016-07-17T01:55:42Z",
            "user_mtime": "2016-07-17T01:55:42Z",
            "jsonmodel_type": "repository",
            "uri": "/repositories/3"
        }
    ]
```

This response is a JavaScript array. What do we do if we want only a
single repository?

--

# 4. Repositories

## Getting a specific repositoriy

1. known the repository id
2. Using the appropriate path get data for the specific repository

--

# 4. Repositories

## How do we know the path?

+ In the API docs, look for "Get a Repository by ID"

```shell
    curl -H "X-ArchivesSpace-Session: $SESSION" \
        'http://localhost:8089/repositories/1'
```

It looks like we add the numeric id to the end of the path (i.e. "/1").

--

# 4. Repositories

## adding list_repo

Let's copy and modify our list_repos definition to *list_repo*. Paste
it after the function *list_repos*. We'll be update the *if* block too.

In the definition section add

```python
    def list_repo(api_url, auth_token, repo_id):
        '''List all the repositories, return the listing object'''
        req = urllib.request.Request(
            url = api_url+'/repositories/'+str(repo_id),
            data = None,
            headers = {'X-ArchivesSpace-Session': auth_token})
        try:
            response =  urllib.request.urlopen(req)
        except HTTPError as e:
            print(e.code)
            print(e.read())
            return None
        except URLError as e:
            print(e.reason)
            return None
        src = response.read().decode('utf-8')
        return json.JSONDecoder().decode(src)
```

In the test *if* block add

```python
        # Test for list_repo
        repo_id = int(input('Enter repo id (e.g. 2): '))
        repos = list_repos(api_url, auth_token, repo_id)
        print('repositores list', json.dumps(repos, indent=4))

```

Are the results what you expected? Are we still getting an array?

--

# 4. Repositories

## How do you update the repository definition?

We use the update API call. Once again we need to check with the
API documentation but this time search for "Update a repository".

On the right side the *curl* expression looks like

```shell
    curl -H "X-ArchivesSpace-Session: $SESSION" \
    -d {
       "jsonmodel_type": "repository",
       "name": "Description: 11",
       "repo_code": "ASPACE REPO 2 -- 631024",
       "org_code": "970UV228G",
       "image_url": "http://www.example-3.com",
       "url": "http://www.example-4.com"
    } \
    'http://localhost:8089/repositories/1'
```

Note the following

1. The repo id is at the end of the path like in list a specific repository
2. We have another JSON data structure to submit and we do so with a "POST"
3. We still need to maintain our token.

--

# 4. Repositories

## Update Repository

What functions have we implement that are similar? What does the documentation
suggest?

1. copy *create_repo* function to *update_repo* adding it after *list_repo*
2. We'll also update our tests at the end of the file

Your code should wind up looking something like this.

In the definition section add

```python
    def update_repo(api_url, auth_token, repo_id, repo):
        '''This function sends a updates a repository via ArchivesSpace REST API'''
        data = json.JSONEncoder().encode(repo).encode('utf-8')
        req = urllib.request.Request(
            url = api_url+'/repositories/'+str(repo_id),
            data = None,
            headers = {'X-ArchivesSpace-Session': auth_token})
        try:
            response = urllib.request.urlopen(req, data)
        except HTTPError as e:
            print(e.code)
            print(e.read())
            return None
        except URLError as e:
            print(e.reason())
            return None
        src = response.read().decode('utf-8')
        return json.JSONDecoder().decode(src)
```

In the test *if* block add

```python
        # Test for update_repo()
        repos = list_repos(api_url, auth_token)
        print('Pick a repository id to update', json.dumps(repos, indent=4))
        repo_id = int(input('Repository numeric id: '))
        print('Getting repository record', repo_id)
        repo = list_repo(api_url, auth_token, repo_id)
        repo["name"] = input('old name is'+repo['name']+', provide a new name: ')
        print('Now we update')
        result = update_repo(api_url, auth_token, repo_id, repo)
        print("Result is", result)
```

Run this updated version and see how it works. Note you can also use the other
methods in the module like *list_repos()* as well as *list_repo()*.

--

# 4. Repositories

## Finally we can delete a repository too

As you may suspect we're beginning to see allot of repetition in our code.
We'll live with it for now. To delete a repository take a look at the
docs. You can find it by searching for "Delete a Repository". The
*curl* looks like this ...

```shell
    curl -H "X-ArchivesSpace-Session: $SESSION" \
        -X DELETE \
        'http://localhost:8089/repositories/:repo_id'
```

Notice it looks allot like our *list_repo()* curl example but with
an "-X DELETE".  There are four common methods in HTTP transactions

+ GET, POST, PUT, DELETE

DELETE does what it sounds like. It'll send a "DELETE" method call to
the API requesting the repository to be deleted. Note deleting a record
via the API is permanent. There is no "UNDO"!!!!

1. Copy *list_repo()* function definition to *delete_repo* after *update_repo*
2. We need to modify the default test methods once again

--

# 4. Repositories

## The dangerous delete method

```python
    def delete_repo(api_url, auth_token, repo_id):
        '''Delete a repository via ArchivesSpace REST API, returns status code 200 on success'''
        req = urllib.request.Request(
            url = api_url+'/repositories/'+str(repo_id),
            data = None,
            headers = {'X-ArchivesSpace-Session': auth_token},
            method = 'DELETE')
        try:
            response = urllib.request.urlopen(req)
        except HTTPError as e:
            print(e.code)
            print(e.read())
            return None
        except URLError as e:
            print(e.reason())
            return None
        src = response.read().decode('utf-8')
        return json.JSONDecoder().decode(src)
```

Our test should look something like ...

```python
        # Test delete_repo
        print('Testing delete_repo()')
        repo_id = int(input('Repository numeric id to delete: '))
        result = delete_repo(api_url, auth_token, repo_id)
        print('Result is', json.dumps(result, indent=4))
```

--

# 4 Repositories

## Our second mofule, repo.py

```python
    #!/usr/bin/env python3
    import urllib.request
    import urllib.parse
    import urllib.error
    import json
    import getpass
    # Here's our own login module
    import login
    
    
    def create_repo(api_url, auth_token, name, repo_code, org_code = '', image_url = '', url = ''):
        '''This function sends a create request to the ArchivesSpace REST API'''
        data = json.JSONEncoder().encode({
                        'jsonmodel_type': 'repository',
                        'name': name,
                        'repo_code': repo_code,
                        'org_code': org_code,
                        'image_url': image_url,
                        'url': url
                    }).encode('utf-8')
        req = urllib.request.Request(
                url = api_url+'/repositories', 
                data = None, 
                headers = {'X-ArchivesSpace-Session': auth_token})
        try:
            response = urllib.request.urlopen(req, data)
        except HTTPError as e:
            print(e.code)
            print(e.read())
            return ""
        except URLError as e:
            print(e.reason())
            return ""
        src = response.read().decode('utf-8')
        return json.JSONDecoder().decode(src)
    
    def list_repos(api_url, auth_token):
        '''List all the repositories, return the listing object'''
        req = urllib.request.Request(
            url = api_url+'/repositories',
            data = None,
            headers = {'X-ArchivesSpace-Session': auth_token})
        try:
        response = urllib.request.urlopen(req)
        except HTTPError as e:
            print(e.code)
            print(e.read())
            return None
        except URLError as e:
            print(e.reason())
            return None
        src = respone.read().decode('utf-8')
        return json.JSONDecoder().decode(src)
    
    def list_repo(api_url, auth_token, repo_id):
        '''List all the repositories, return the listing object'''
        req = urllib.request.Request(
            url = api_url+'/repositories/'+str(repo_id),
            data = None,
            headers = {'X-ArchivesSpace-Session': auth_token})
        try:
            response =  urllib.request.urlopen(req)
        except HTTPError as e:
            print(e.code)
            print(e.read())
            return None
        except URLError as e:
            print(e.reason)
            return None
        src = response.read().decode('utf-8')
        return json.JSONDecoder().decode(src)
    
    def update_repo(api_url, auth_token, repo_id, repo):
        '''This function sends a updates a repository via ArchivesSpace REST API'''
        data = json.JSONEncoder().encode(repo).encode('utf-8')
        req = urllib.request.Request(
            url = api_url+'/repositories/'+str(repo_id),
            data = None,
            headers = {'X-ArchivesSpace-Session': auth_token})
        try:
            response = urllib.request.urlopen(req, data)
        except HTTPError as e:
            print(e.code)
            print(e.read())
            return None
        except URLError as e:
            print(e.reason())
            return None
        src = response.read().decode('utf-8')
        return json.JSONDecoder().decode(src)
    
    def delete_repo(api_url, auth_token, repo_id):
        '''Delete a repository via ArchivesSpace REST API, returns status code 200 on success'''
        req = urllib.request.Request(
            url = api_url+'/repositories/'+str(repo_id),
            data = None,
            headers = {'X-ArchivesSpace-Session': auth_token},
            method = 'DELETE')
        try:
            response = urllib.request.urlopen(req)
        except HTTPError as e:
            print(e.code)
            print(e.read())
            return None
        except URLError as e:
            print(e.reason())
            return None
        src = response.read().decode('utf-8')
        return json.JSONDecoder().decode(src)
    
    
    if __name__ == '__main__':
        # Test login
        print("Testing login()")
        api_url = input('ArchivesSpace API URL: ')
        username = input('ArchivesSpace username: ')
        password = getpass.getpass('ArchivesSpace password: ')
        print('Logging in', api_url)
        auth_token = login.login(api_url, username, password)
        print("auth token", auth_token)
        if auth_token != '':
            print('Success!')
        else:
            print('Ooops! something went wrong')
            sys.exit(1)
    
        # Test create_repo
        print('Testing create_repo()')
        print('Create your first repository')
        name = input('Repo name: ')
        repo_code = input('Repo code: ')
        repo = create_repo(api_url, auth_token, name, repo_code)
        print(json.dumps(repo, indent=4))
        print('Create a second repository')
        name = input('Repo name: ')
        repo_code = input('Repo code: ')
        repo = create_repo(api_url, auth_token, name, repo_code)
        print(json.dumps(repo, indent=4))
    
        # Test list_repos
        print('Testing list_repos()')
        repos = list_repos(api_url, auth_token)
        print('repositores list', json.dumps(repos, indent=4))
    
        # Test list_repo
        print('Testing list_repo()')
        repo_id = int(input('Enter repo id: '))
        repo = list_repo(api_url, auth_token, repo_id)
        print('repository list', json.dumps(repo, indent=4))
        
        # Test update_repo
        print('Testing update_repo()')
        repo_id = int(input('Repository numeric id to update: '))
        print('Getting repository record', repo_id)
        repo = list_repo(api_url, auth_token, repo_id)
        repo['name'] = input('old name is '+repo['name']+', provide a new name: ')
        print('Now we update')
        result = update_repo(api_url, auth_token, repo_id, repo)
        print('Result is', json.dumps(result, indent=4))
        
        # Test delete_repo
        print('Testing delete_repo()')
        repo_id = int(input('Repository numeric id to delete: '))
        result = delete_repo(api_url, auth_token, repo_id)
        print('Result is', json.dumps(result, indent=4))
        
        # All done!
        print('Success!')
```

Full listing [repo.py](repo.py)

--

# 5. Working with Agents

## Our recipe

Each ArchivesSpace API Model tends to have its own nuances based on the
schema. Agents is no exception. Rely on the docs as much as you can. 
When the docs fail there is the email list and you can experiment too.
When I first started working with AS documentation was thin and I used
*curl* and [jq](https://stedolan.github.io/jq/tutorial/).

1. Look up in the API Docs the object module that applies
    + Is there more than one?
2. Look up in the API Docs the activity want to use
3. Look at the HTTP method required (e.g. GET, POST, DELETE)
4. Look at any data that needs to be sent, noting how it is sent
    + (e.g. a JSON blob or as part of a path)

--

# 5. Working with Agents

## Sorting the HTTP methods we need to use

Suggested functions

+ create_agent (CREATE)
+ list_agents  (READ)
+ list_agent   (READ)
+ update_agent (UPDATE)
+ delete_agent (DELETE)

These are our basic CRUD operations as functions working with the API.

--

# 5. Working with Agents

## How about types of agents?

ArchivesSpace stores the agent type in the schema but it also uses it when
organizing API access via the URL (e.g. /agents/software, /agents/people).

+ corporate_entities
+ families
+ people (we'll focus on this type in the workshop)
+ software

--

# 5. Working with Agents

## agent types versus paths

One thing to notice is that in the data modules the *type*
doesn't exactly match the *path* in the REST API. 

+ *agent_corporate_entity* becomes */agents/corporate_entities*
+ *agent_family* becomes */agents/families*
+ *agent_person* becomes */agents/people*
+ *agent_software* becomes */agents/software*

The URL's a easy to remember with these adjustments but it easy
to make the mistake when building a model by hand (or debugging one
you've written) that you can't replace the '/' with a '_'.

--

# 5. Working with Agents

## create_agent recipe

1. import our usual modules
2. define our create_agent
    + need to figure out the minimum agent record
3. add our tests at the botton of our script in the *if* block

--

# 5. Working with Agents

## create_agent concerns

The API docs we want to read closely are the models/schema for
the specific agent type we want to handle.  The API will validate
our fields so we'll need to handle the response case where the API
is trying to tell us we're missing a required field or something else
is out of order.

This has the benefit of keep our code simple but does mean we need more
code evaluating the response.

--

# 5. Working with Agents

## create_agent code will need:

1. Open a new file called [agent.py](agent.py)
2. Create our usual block plus `import login`
3. To create our function create_agent() we need to know
    + api_url
    + auth_token
    + agent_type
    + the rest of the agent data (see the API docs)
        + hint: we want the minimum data first
4. Add tests for each type of agent we want to support

--

# 5. Working with Agents

## create_agent schema

A quick search in the API docs for "Create a person agent" leads us
to ... nothing. As I was writing the agents section I notice most
of the *curl* examples and their outputs are missing since the upgrade
to v1.5.0. This provided a educational moment for me.  I can talk a little
bit about how to sort things when the docs are a bit thin.

### Debugging the API docs

Read what's there and guess at the next step.

```shell
    curl -H "X-ArchivesSpace-Session: $SESSION" \
        http://localhost:8089/agents/people
```

I get back an error

```json
    {
        "error":{
            "page":[
                "Parameter required but no value provided"
            ],
            "id_set":[
                "Parameter required but no value provided"
            ],
            "all_ids":[
                "Parameter required but no value provided"
            ]
        }
    }
```

And it lets us know the options expected. We will use "all_ids=true" next.

--

### Second attempt

```shell
    curl -H "X-ArchivesSpace-Session: $SESSION" \
    http://localhost:8089/agents/people?all_ids=true
```

This gives an array of integer ids. I haven't created any "people" yet
so I'm guessing that is the "Admin" account.

```json
    [
      1
    ]
```

Trying

```shell
    curl -H "X-ArchivesSpace-Session: $SESSION" \
    http://localhost:8089/agents/people/1
```

I get back a big JSON blob like [model-examples/admin-agent.json](model-examples/admin-agent.json).

--

# 5. Working with Agents

## Thats too much info!

From the docs we know we need a POST and we known that the path in the
URL will look like "/agent/people". The docs also tell us what we should
except if we're successful. This is where working in the shell is handy.

After some experimentation I've arrahved at the following minimum 
*agent_person* request.

```python
    # Our minimal agent record includes a :name_person and a :agent_person
    # model
    name_model = {
           'primary_name': primary_name,
           'rest_of_name': rest_of_name,
           'name_order': 'inverted',
           'jsonmodel_type': 'name_person',
           'source': source,
           'rules': rules,
           'sort_name': primary_name+', '+rest_of_name,
           'is_display_name': True,
    }

    agent_model = {
        'jsonmodel_type': agent_type,
        'title': primary_name+', '+rest_of_name,
        'is_link_to_be_published': False,
        'agent_type': agent_type,
        'publish': False,
        'display_name': name_model,
        'names':[
           name_model
         ]
    }
```

--

# 5. Working with Agents

## create_agent implementation

At the end of our imports block add

```python
    import login
```

In our definition section add

```python
    def agent_type_path(agent_type):
       '''Map the agent type to a partial path'''
       # agent_person agent_corporate_entity agent_software agent_family user
       m = {
          'agent_person': 'people',
          'agent_corporate_entity': 'corporate_entities',
          'agent_software': 'software',
          'agent_family': 'families',
          'user': 'user'
       }
       return '/agents/'+m[agent_type]
    
    def create_agent(api_url, auth_token, agent_model):
       '''create an agent and return the new agent record'''
       data = json.JSONEncoder().encode(agent_model).encode('utf-8')
       url = api_url+agent_type_path(agent_model['agent_type'])
       req = urllib.request.Request(
            url = url,
            data = None,
            headers = {'X-ArchivesSpace-Session': auth_token},
            method = 'POST')
       try:
            response = urllib.request.urlopen(req, data)
       except urllib.error.URLError as e:
            print(e.reason)
            return None
       except urllib.error.HTTPError as e:
            print(e.code)
            print(e.read())
            return None
       src = response.read().decode('utf-8')
       return json.JSONDecoder().decode(src)
```

Finally in our *if* block  we need some test code.

```python
        # check mapping of agent type (e.g. agent_person) to path
        print('Check that our mapping of agent type to path works')
        url_test = agent_type_path('agent_person')
        if url_test != '/agents/people':
           print('ERROR: expected .../agents/people, found ', url_test)
           sys.exit(0)
        else:
           print('agent_type_path() OK')

        print('Testing create_agent')
        # Here's our minimal fields
        primary_name = input('Primary name (e.g. family name) ')
        rest_of_name = input('Rest of name (e.g. first name) ')
        agent_type = 'agent_person'
        source = 'local'
        rules = 'local'

        # Our minimal agent record includes a :name_person and a :agent_person
        # model
        name_model = {
               'primary_name': primary_name,
               'rest_of_name': rest_of_name,
               'name_order': 'inverted',
               'jsonmodel_type': 'name_person',
               'source': source,
               'rules': rules,
               'sort_name': primary_name+', '+rest_of_name,
               'is_display_name': True,
        }

        agent_model = {
            'jsonmodel_type': agent_type,
            'title': primary_name+', '+rest_of_name,
            'is_link_to_be_published': False,
            'agent_type': agent_type,
            'publish': False,
            'display_name': name_model,
            'names':[
               name_model
             ]
        }

        # Now that we have a minimal record lets make a request
        print("The minimum payload looks like ", json.dumps(agent_model, indent=4))
        agent_response = create_agent(api_url, auth_token, agent_model)
        agent_id = agent_response['id']
        print('agent created response', json.dumps(agent_response, indent=4))
```

Full listing [agent.py](agent.py)

--

# 5. Working with Agents

## list_agents recipe

1. we need the usual api_url, auth_token
2. plus we need to know the agent_type (e.g. "agent_person")
3. Get and decode the response.

--

# 5. Working with Agents

## list_agents implementation

1. Add our list_agents() to our *def* section
2. Update our tests in our *if* block

In our definition section add

```python
    def list_agents(api_url, auth_token, agent_type):
       '''List all the agent ids of a given type'''
       data = urllib.parse.urlencode({'all_ids': True}).encode('utf-8')
       url = api_url+agent_type_path(agent_type)
       req = urllib.request.Request(
          url = url,
          data = data,
          headers = {'X-ArchivesSpace-Session': auth_token},
          method = 'GET')
       try:
            response = urllib.request.urlopen(req)
       except urllib.error.URLError as e:
            print(e.reason)
            return None
       except urllib.error.HTTPError as e:
            print(e.code)
            print(e.read())
            return None
       src = response.read().decode('utf-8')
       return json.JSONDecoder().decode(src)
```

In our *if* test block add

```python
        # Test list_agents(), requires api_url, auth_token and agent_type
        print('Test list_agents()')
        agent_ids = list_agents(api_url, auth_token, 'agent_person')
        if len(agent_ids) < 1:
            print('ERROR: should have at least one agent!')
            sys.exit(0)
        print('agent ids ->', json.dumps(agent_ids, indent = 4))
```

Full listing [agent.py](agent.py)

--

# 5. Working with Agents

## list_agent implementation

In our definition section add

```python
    def list_agent(api_url, auth_token, agent_type, agent_id):
       '''List all the agent ids of a given type'''
       url = api_url+agent_type_path(agent_type)+'/'+str(agent_id)
       req = urllib.request.Request(
          url = url,
          data = None,
          headers = {'X-ArchivesSpace-Session': auth_token},
          method = 'GET')
       try:
            response = urllib.request.urlopen(req)
       except urllib.error.URLError as e:
            print(e.reason)
            return None
       except urllib.error.HTTPError as e:
            print(e.code)
            print(e.read())
            return None
       src = response.read().decode('utf-8')
       return json.JSONDecoder().decode(src)
```

In our test *if* block add

```python
        print('Test list_agent()')
        agent_id = int(input('Enter agent_id (numeric): '))
        agent = list_agent(api_url, auth_token, 'agent_person', agent_id)
        print('agent', agent_id, ' details', json.dumps(agent, indent=4))
```

Full listing [agent.py](agent.py)

--

# 5. Working with Agents

## Update an Agent

+ we need to decide what part of the record we're updating
+ we need to get a recent copy of the agent record to modify
+ make our changes
+ submit the updates

The ArchivesSpace API is very picky here. You're going to 
spend allot of time debugging your data modifications.

--

# 5. Working with Agents

## Update an Agent implementation

In the definition section add

```python
    def update_agent(api_url, auth_token, agent_type, agent_id, agent_model):
       '''create an agent and return the new agent record'''
       data = json.JSONEncoder().encode(agent_model).encode('utf-8')
       url = api_url+agent_type_path(agent_type)+'/'+str(agent_id)
       req = urllib.request.Request(
            url = url,
            data = None,
            headers = {'X-ArchivesSpace-Session': auth_token},
            method = 'POST')
       try:
            response = urllib.request.urlopen(req, data)
       except urllib.error.URLError as e:
            print(e.reason)
            return None
       except urllib.error.HTTPError as e:
            print(e.code)
            print(e.read())
            return None
       src = response.read().decode('utf-8')
       return json.JSONDecoder().decode(src)
```

In the test section add

```python
        # Update the record we just created
        agent_type = input('Enter agent type: ')
        agent_id = int(input('Enter agent id to update: '))
        note_text = input('Enter some text to add as a note: ')
        agent_model = list_agent(api_url, auth_token, agent_type, str(agent_id))
    
        note_count = len(agent_model['notes'])
        if (note_count > 0):
            print('The existing notes are', json.dumps(agent_model['notes'], indent=4))
    
        new_note = {
            'jsonmodel_type': 'note_bioghist',
            'persistent_id': 'urn:test.a.note.to.self/'+str(note_count+1),
            'label': 'Personal note to self',
            'subnotes': [
                {
                    'jsonmodel_type': 'note_text',
                    'content': note_text,
                    'publish': True
                }
            ],
            'publish':True
        }
        # now adding a new note
        agent_model['notes'].append(new_note)
        print("Added a note", json.dumps(agent_model['notes'], indent=4))
        res = update_agent(api_url, auth_token, agent_type, 3, agent_model)
        print('Response was', json.dumps(res, indent=4))
```

Notice the specifics of the test. The tests are bittle. Debugging the
submitted record if painful. Just no two ways about it.  *curl* can
sometimes be a better friend than Python for debugging http error 
responses.

Full listing [agent.py](agent.py)

--

# 5. Working with Agents

## Delete an Agent

The delete agent should look familiar compared to delete_repo(),
We need *agent_type* in addition to *agent_id*.

In the definition section add

```python
    def delete_repo(api_url, auth_token, repo_id):
        '''Delete a repository via ArchivesSpace REST API, returns status code 200 on success'''
        req = urllib.request.Request(
            url = api_url+'/repositories/'+str(repo_id),
            data = None,
            headers = {'X-ArchivesSpace-Session': auth_token},
            method = 'DELETE')
        try:
            response = urllib.request.urlopen(req)
        except HTTPError as e:
            print(e.code)
            print(e.read())
            return None
        except URLError as e:
            print(e.reason())
            return None
        src = response.read().decode('utf-8')
        return json.JSONDecoder().decode(src)
```

In the test *if* block add

```python
       # Test delete_agent()
       print('Testing delete_repo()')
       agent_id = int(input('Agent numeric id to delete: '))
       result = delete_agent(api_url, auth_token, agent_type, agent_id)
       print('Result is', json.dumps(result, indent=4))
```

Full listing [agent.py](agent.py)

--

<blockquote>We've covered allot, stretch break? questions? API adventure stories?</blockquote>

--

# 6. Accessions

## Working with Accessions

This is going to feel a little like Deja Vu because the process
is largely similar to working with Agents only the nuances of the data
models are different.

We're going to blast through 

+ Creating Accessions
+ Viewing Accession details
+ Listing Accession IDs
+ Listing an individual Accession
+ Updating an Accession
+ Deleting an Accession

--

# 7. What's next?

## Working in Batches

+ getting a list of useful IDs
+ iterating over the IDs
+ managing process load
    + avoiding too much of a good thing

--

#  7.  What's next?

## Other ArchivesSpace models

+ Digital Objects
+ Resources
+ Subjects/Terms

--

# References

+ [ArchivesSpace REST API](http://archivesspace.github.io/archivesspace/api/)
+ [Python 3 Docs](https://docs.python.org/3.5/)
    + [urllib2](https://docs.python.org/3/howto/urllib2.html)
        + [Basic Auth example](http://www.voidspace.org.uk/python/articles/authentication.shtml)
    + [JSON module](https://docs.python.org/3.5/library/json.html?highlight=json#module-json)
    + [OS module](https://docs.python.org/3.5/library/os.html) (for using environment variables)
+ [github.com/caltechlibrary/aspace-api-workshop](https://github.com/caltechlibrary/aspace-api-workshop)

--

Thank you for participating!

Presentation is at

[rsdoiel.github.io/archivesspace-api-workshop](https://rsdoiel.github.io/archivesspace-api-workshop)

Slides can be downloaded at

[github.com/rsdoiel/archivesspace-api-workshop/releases/latest](https://github.com/rsdoiel/archivesspace-api-workshop/releases/latest)

Please feel free to fork and improve.
