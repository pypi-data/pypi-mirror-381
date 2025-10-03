# Updates

## Update Process

To update a piece of software we need to either

- run an external package manager's update mechanism or
- remove the package and install it, while keeping its configuration files or
- run a specific update script

Before running updates, we must fetch the package definition file to see if
the installation strategy for any package has changed.
As an edge case, a package can move from one update strategy to another as
apparent when comparing the package definition file before and after fetching
it.
For example, a package installed through system package managers (brew, ...)
may be moved to a pip-based installer.
In this scenario, the old package must be removed and reinstalled.

The whole update process looks like this:

1. Update funstall itself
2. Fetch new package definition file
3. Update all installed packages

## Out of Scope

The following features are currently out of scope:

- Removing a package's configuration files when removing the package
