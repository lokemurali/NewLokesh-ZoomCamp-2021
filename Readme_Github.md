Read me for the Github change and roadblocks faced.

I messed up with the repo in both local and github online and discarded all changes and files created.

somehow managed to get the .git (hidden file) in the local path.
this will get created when we initialize the local folder to the github repo
when we delete this all the conncetion it has with github will be lost.

I deleted all the repo and files including .git and created a new repo in the github wihtout creating the "Readme.md" file. because when we create this file it does the first commit,

And when we try to push the changes to the githib, the mismatch happens and it wont allow us to commit the changes we do form local.

to avoid this, we have to run several git commands to pull the request and merge the commits.

Below are the git commands used:

>git init (should be on the exact path)
>git add .
>git commit -m "mesage"
>git remote add orgin <github repo URL>
>git push -u origin master
 if this shows error, then the error because of commit not in sync b/w local and online because we would have created readme.md and commited those at the time of repo creation in github link.
    to solve this.
    > git pull --rebase origin master (master here is the name of the branch)
        this will pull the changes in changes local from online and do merge all the changes and commit at once for all.
    you can check the commit list using >git log
    now we can try again the push command, >git push -u origin master