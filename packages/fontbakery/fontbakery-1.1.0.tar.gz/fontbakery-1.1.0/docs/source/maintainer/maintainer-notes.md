# Project Maintainer Notes

## Code Testing

`pytest` and `coverage` are used to execute the Font Bakery test suite and line coverage assessment, respectively.

Use the following command to run all tests:

```
$ pytest -x tests
```

The coverage report can be found at the end of the test results that are printed to the standard output/error stream.

Continuous integration testing is performed on GitHub Actions. Test jobs can be found at [https://github.com/fonttools/fontbakery/actions](https://github.com/fonttools/fontbakery/actions).

## Updating the distribution package

Releases to PyPI are performed by running the following commands (with the proper version number and date):

```sh
# Update the local copy
git checkout main
git fetch upstream
git rebase upstream/main

# Be sure that there's no leftover code-changes in the local copy
git status

# Create a branch for the final tweaks prior to release:
git checkout -b preparing_v0_8_2

# Make sure googlefonts "always latest" dependencies are up-to-date at pyproject.toml

# Update the cached list of vendor IDs:
wget https://docs.microsoft.com/en-us/typography/vendors/ --output-document=Lib/fontbakery/data/fontbakery-microsoft-vendorlist.cache
git add -p

# If something changed, commit it:
git commit -m "Updating cache of vendor IDs list from Microsoft's website"

# Check whether ttfautohint has a newer version available at https://sourceforge.net/projects/freetype/files/ttfautohint/
# and manually update the LATEST_TTFAUTOHINT_VERSION number, if needed:
vim Lib/fontbakery/constants.py
git add -p
git commit -m "Updating LATEST_TTFAUTOHINT_VERSION"

# update the docs so that https://fontbakery.readthedocs.io/
# displays the correct version number
vim docs/source/conf.py
git add -p
git commit -m "update version on docs/source/conf.py"

# See if there's any experimental check that could be made effective (non-experimental)
# in the new release and update CHANGELOG accordingly.
git grep "experimental=\"Since"

vim CHANGELOG.md
git add -p
git commit -m "update CHANGELOG in preparation for new release"

# send these changes to the public GitHub repo
git push upstream preparing_v0_8_2

# Open a pull request and wait for all code-tests to pass
# or make additional commits until the build is finally green

# Update the local copy
git checkout main
git fetch upstream
git rebase upstream/main

## Optionally run our code tests locally
pytest -x tests

# If all is good, then make the actual release:
# Register a git tag for this release and publish it
git tag -a v0.8.2 -m "Font Bakery version 0.8.2 (2021-Sep-01)"
git push upstream --tags

# A GitHub Action will be triggered by the version tag and will
# generate the package and automatically publish it on PyPI.
# A GitHub release will also be created automatically.

# ATTENTION!
# We need to manually set this release to be considered the latest one.
# And also uncheck its "pre-release" checkbox!

# Close the current milestone on the GitHub issue tracker
# moving to a future milestone any of its issues that we've
# not been able to close yet.
# https://github.com/fonttools/fontbakery/milestones
```

## Cached Vendor ID data

This project hosts a copy of the Microsoft's Vendor ID list at Lib/fontbakery/Lib/data/fontbakery-microsoft-vendorlist.cache

This is meant only as a caching mechanism. The latest data can always be fetched from Microsoft's website directly at: <https://www.microsoft.com/typography/links/vendorlist.aspx>
