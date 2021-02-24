# Project Template

This project is a boiler plate for any new Pyspark projects for epp in Agatha. It houses the basic project structure that we should generally use.

To use:
1. Click Use this template button in GitHub
2. On the create new repo page
    * Change owner to EPP within dropdown
    * Name repository
    * Provide brief project description
3. Create dev Branch
    * On your repo's main page, press the branch selector dropdown (immediately above your file list, currently set to Branch: master)
    * Type `dev` into the branch selector
    * Click "Create branch: dev'
3. Protect Master and Dev Branches
    * Go to the Settings of your repository
    * Go to Branches-->Branch protection rules-->Add rule
    * Type `master` under the branch pattern name and choose "Require pull request reviews before merging"
    * Click Create
    * Repeat this procedure to protect your dev branch (note: make sure you do go back and click the "Add rule" button or you might accidently edit your master branch protection to dev)
4. Clone repository down to local machine
