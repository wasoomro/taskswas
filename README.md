# To Run Application
activate environment in the project, install dependencies by pipenv install (pipenv should be global assumed), pipenv shell (to activate pipenv env), cd to tasks.  Run migrations there by python migrate.py migrate and application is now running.

# To register 
Go to /account/api/register (you'll have ui through rest framework) or send post request to it required fields (username, password, email). it will create your account

# To Get Auth Token
This app is based on jwt tokens, get token by sending post request to /api/token/ you will get access token in response in form {refresh: "", access: ""}

# To Crud tasks
user router /tasks to create update insert and get tasks

# To run cron job
- Create a cron job that runs the management command at 9 PM every day. You can use the **crontab** command to edit your cron file and add a line like this:

```bash
0 21 * * * python manage.py notify_users