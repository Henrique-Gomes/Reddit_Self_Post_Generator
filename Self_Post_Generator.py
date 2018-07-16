#!/usr/bin/python
import praw
import time

# get next id
def inc_id(id):
    new_id = list(id) 
    i = 5
    while(new_id[i]=='z'):
        new_id[i] = '0'
        i = i - 1
    else:
        if (new_id[i]=='9'):
            new_id[i]='a'
        else:
            new_id[i] = chr(ord(new_id[i]) + 1)
    return "".join(new_id)

reddit = praw.Reddit('bot_name') # change bot name

allposts = reddit.subreddit("all")
dest = reddit.subreddit("subreddit_name") # change name of subreddit where the self post will be made

execute = True

try:
  while(execute):
      for last in allposts.new(limit=1):
          new_id = inc_id(last.id)
          for i in range(0,3): # you need to inc id more than once. according to your internet speed and the difference between generated id and correct id, change the range
            new_id = inc_id(new_id)
          submission = dest.submit("Post Name", url="https://www.reddit.com/r/SubredditName/comments/"+new_id+"/post_name/") # change sub-reddit and post name (in the param and in the link) (replace spaces with underscores in the link) 
          if (submission.id != new_id):
              submission.delete()
              print("\nGenerated id:  "+str(new_id)+"\nCorrect would be: "+str(submission.id))
          else:
              execute = False
      # time.sleep(600) # uncomment it if there is minimum timeout to repost (generally, timeout is 10 minutes = 600 seconds)
                        # move sleep to the start of for block if you tried to use the script in this same sub-reddit recently
  input("Finished")
except Exception as e:
  print(str(e))
  pass
  input("")
