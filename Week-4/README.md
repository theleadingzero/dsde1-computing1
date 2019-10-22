# Week 4 Exercises

# Tuesday - Updating from Github and More on Datatypes

## Updating Your Forked Repo

Changes will be made in the original repo and new files will be added as the weeks progress. You will want to make sure you update your repo with those changes. This is called syncing the fork.

### One-Time Set Up

You only need to do these steps once.

1. Open a terminal and `cd` to your copy of `dsde-computing1`.

2. Type in the following. If both the URLs that are printed are the same, then you need to do the following steps. If the one labelled `(fetch)` is `git@github.com:theleadingzero/dsde1-computing1.git` then you can skip to the next section to update your repo.

```
git remote -v
```

3. You need to tell your repo where to look for updates (the original repo). Do this by typing the following into the terminal.

```
git remote add upstream git@github.com:theleadingzero/dsde1-computing1.git
```

__NOTE__: If you are using https instead of ssh, the you instead want

```
git remote add upstream https://github.com/theleadingzero/dsde1-computing1.git
```

4. Type in the following again. This time it should show an URL with your username for `(push)` and one the `theleadingzero` for `(fetch)`.

```
git remote -v
```

## How to Update Your Repo

Once you've done the above once, the following steps will let you update your repo.

1. Make sure you have any changes to your repo commited and pushed.

6. Type in the following command. This will request any changes from the master repo and save them in a new branch called `upstream`.

```
git fetch upstream
```

7. Now you will request to pull all the changes from the original repo into your branch called `upstream`.

```
git fetch upstream
```

8. You will now switch back to your repo's `master` branch.

```
git checkout master
```

9. You will now merge the changes you fetched with your local repo. If there are any conflicting changes,

```
git merge upstream/master
```


## Manipulating Data Structures

1. Open up `structures.py` and follow the instructions in the comments above each function definition.

2. Run the test file to determine if the function work correctly.

```
python -m unittest test_structures.py
```

## Docstrings

1. Add docstrings to your functions in `structures.py`.

2. Import your module `structures.py` in an interactive Python shell. Check that your docstrings print when calling the `help()` function.

```
import structures as s
help(s.first_and_last)
```

## Linting

1. Run pylint on the file `fuzzy.py` and correct the issues that are printed.

```
pylint fuzzy.py
```

2. Run pylint on your `fuzzy.py` and fix the issues.

