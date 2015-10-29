# Parcel

**This software is currently a work in proccess, like I haven't done any coding yet. You have been warned**

This is an experiment to create a cargo (from the Rust programming language) like program for python.
It's currently in the early stages of experimentation and does not probably work as intended at all.


## Feature Ideas
The program is here to help with the creation, packaging and distribution of python software. I would like it to be able to do some of the below features.

	`parcel new <name>`
		This should simply create a directory named <name>, create a repo in that directory (leaning towards git as standard)
		and instanciate some of the standard files that are needed (license etc). The directory structure I'm leaning towards
		is the one I use the most (if you don't think that is a good one I'm always willing to change my mind): http://www.kennethreitz.org/essays/repository-structure-and-python.

		Switches:
			--version-control, -vcs <scm>: Use the specified version control system. Use -vcs=none to not initialize a repository.
			--version-control-list: List the supported version control systems and exit.

	`parcel test`
		Somewhat selfexplanatory but this will run all the tests in the repo and report as usual failures and passed tests.
	`parcel build`
		Downloads required packages if they are not present. Should be able to build a wheel, source dist, and maybe an egg? I'm not familiar enough
		with python packaging to have a good opinion on what to do here. Need more research and / or suggestions.
	`parcel install`
		Installs the software on the machine (should work as pip)
	`parcel package`
		This should distribute the program to pypi, similar to twine upload. Would be nice if we could support other package repos (like private ones) and not just PyPi. Again need more research to make a good decision on what to do.
