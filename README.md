# Reddit_Self_Post_Generator
A Python script that Generates a link post with a link for itself

The script runs on **Python 3**

There are instructions on how to modify the script and the .ini properly **in the comments** in the files

You need to **install praw library** on your machine to run it
* you can do that by openning a Command Window in the *Scripts/* folder and running the command "*pip install praw*".  (*Scripts/* folder is generally inside your python instalattion folder, and must have an executable named "pip.exe" inside)

Let praw.ini in the **same folder** as the script.

The script attempts to create the post more than once. On failed attempts, the created post will be automatically deleted and the program will try again. Please note that some subreddits have a minimum 10 minutes timeout for trying to post again. **If it's the case, you need to uncomment the line with the "time.sleep(600)"**, or the script you return you an error. If you tried to use the script in this same sub-reddit recently, move this command to the start of the for block.

If there is a minimum timeout to repost, **the script may take a *long* time.**
