XSS Blog is a small application created with Django to demonstrate the severity of Stored XSS attacks. 

To follow along with my article, <a href="https://whitehatways.com/cross-site-scripting-and-cookies-a-delicious-disaster/">linked here</a>, first download this project to your local computer. 

1). Install requirements with
<code>python3 -m pip install -r requirements.txt</code>

2). Run the following commands to get Django up and going!
<br><code>python3 ./manage.py makemigrations</code>
<br><code>python3 ./manage.py migrate</code>
<br><code>python3 ./manage.py createsuperuser</code>
<br>&emsp; Following the prompts here!
<br><code>python3 seed.py</code>

3). XSS Blog is now fully setup for you to test Stored XSS attacks!
<br>Run <code>python3 ./manage.py runserver</code> to begin!

Happy Hacking! :)