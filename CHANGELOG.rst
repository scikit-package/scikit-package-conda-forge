=============
Release notes
=============

.. current developments

0.1.2
=====

**Added:**

* Add entry points in the recipe.

**Fixed:**

* ``release-on-github-on-tag-push.yml`` is deprecated. Use ``_build-release-github-no-pypi-no-docs.yml``.


0.1.1
=====

**Added:**

* Add ``cookiecutter.json`` in the template to allow ``scikit-package-conda-forge`` to automatically create the project-level config.


0.1.0
=====

**Added:**

* Add test on PR CI without codecov report.
* Add a test for generating meta.yaml by entering input values to cookiecutter.
* Add news item check GH workflow to communcicate the changes made in each PR, while this repository is not released as a package.
* Add pre-commit setup, Github release workflow.

**Changed:**

* Change cookiecutter inputs: github_org to github_username_or_orgname, module_name to package_import_name, repo_name to github_repo_name.

**Removed:**

* Remove support for using GitHub source code to generate meta.yml file.
