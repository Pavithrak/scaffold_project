# Expects a yml file named scaffold.yml
# Pulls service template from source
# Reads all the files that matches with template_file_pattern or just fetches all the *.j2 files
# Renders the j2 file under the same directory using the key value pair given under vars in scaffold.yml
# Ignores the files mentioned under ignore_files
# Runs the script file mentioned in start_up_script if given
# Removes the .git folder
# Creates a empty git repo
# Commits the changes as Initial commit
import yaml
from scaffold_project.scaffold import Scaffold


def run():
    try:
        scaffold_opts = yaml.load(open('scaffold.yml'))
        scaff = Scaffold(scaffold_opts)
        scaff.build()
    except Exception as ex:
        print(ex)

