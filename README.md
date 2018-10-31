# scaffold_project
It is a python package that comes with a command line tool - scaffold_project
This tool will be useful if you are working in microservice environment and you are at the early stage where you find yourself
spinning up lot of services with similar structure with different names and variables.

Given that you have the basic structure of the service templatized (jinja2) in a git repository, 
and you provide all the values for the variables in your template in a yaml file "scaffold.yml" 

When you install and run scaffold_project from the same location as your scaffold.yml

Then it performs the following action
1. Reads a yml file named scaffold.yml
2. Pulls service template
3. Reads all the files that matches with template_file_pattern or just fetches all the *.j2 files
4. Renders the j2 file under the same directory using the key value pair given under vars in scaffold.yml
5. Ignores the files mentioned under ignore_files
6. Runs the script file mentioned in start_up_script if given
7. Recreates a new git repository
8. Commits the changes as Initial commit

-
TODO
Provide an option in the scaffold.yml to rename directories

Sample scaffold.yml

git_source: 'gitrepo'
project_name: 'new_project_repo' 
template_file_pattern: '*.j2'
ignore_files: 
  - 'templates/ignore_that.j2'
  - 'templates/other_folder/ignore_this_too.j2'
start_up_script: 'build_scripts/setup.sh'
rename_folders:
  -
    old: 'src/project_name'
    new: 'new_project'
  - 
    old: 'this/is/old'
    new: 'new'     
vars:
  package_name: 'new_project'
  description: 'something goes here' 

