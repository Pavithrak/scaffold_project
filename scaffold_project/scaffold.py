from scaffold_project.utils import extract_file_name_from_template_name
from subprocess import check_call
from pathlib import Path
import jinja2
import shutil
import os


class Scaffold:
    def __init__(self, options):
        self.git_source = options['git_source']
        self.project_name = options['project_name']
        self.template_file_pattern = options['template_file_pattern'] or "*.j2"
        self.ignore_files = self.__add_new_project_name(options['ignore_files'])
        self.start_up_script = options['start_up_script']
        self.vars = options['vars']

    def __add_new_project_name(self, ignore_files):
        return list(map(lambda file: "{}/{}".format(self.project_name, file), ignore_files))

    def pull_from_source(self):
        print("Cloning from " + self.git_source)
        check_call(['git', 'clone', self.git_source, self.project_name])

    def files_matching_template_file_pattern(self):
        return list(Path(self.project_name).rglob(self.template_file_pattern))

    def get_applicable_templates(self):
        matching_files = self.files_matching_template_file_pattern()
        return [file for file in matching_files if str(file) not in self.ignore_files]

    def render_files(self, templates):
        env = jinja2.Environment(loader=jinja2.FileSystemLoader("."))
        for template in templates:
            filename = str(template)
            new_file_name = extract_file_name_from_template_name(str(template))
            env.get_template(filename).stream(self.vars).dump(new_file_name)
            os.remove(filename)

    def run_start_up_script(self):
        check_call(['sh', "{}/{}".format(self.project_name, self.start_up_script)])

    def set_up_new_repo(self):
        shutil.rmtree("{}/.git".format(self.project_name))
        check_call(['git', 'init'])
        check_call(['git', 'add', '.'])
        check_call(['git', 'commit', '-m', 'Initial commit'])

    def build(self):
        self.pull_from_source()
        applicable_template_files = self.get_applicable_templates()
        self.render_files(applicable_template_files)
        self.run_start_up_script()
        self.set_up_new_repo()
