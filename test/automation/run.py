# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

import os
import shutil
import argparse
import yaml
from time import sleep
from robot.run import run, run_cli
from scripts.webdriver.web_driver_manager import WebDriverManagerBase
from scripts.webdriver.chrome import ChromeDriverManager
from scripts.webdriver.gecko import GeckoDriverManager
from scripts.webdriver.edge import EdgeChromiumDriverManager
import subprocess
from subprocess import Popen, PIPE, CalledProcessError

def execute(cmd):
    popen = subprocess.Popen(cmd, stdout=subprocess.PIPE, universal_newlines=True)
    for stdout_line in iter(popen.stdout.readline, ""):
        yield stdout_line 
    popen.stdout.close()
    return_code = popen.wait()
    if return_code:
        raise subprocess.CalledProcessError(return_code, cmd)


current_dir = os.path.dirname(os.path.abspath(__file__))
env_list = []


def setup_git_repo(url, branch, commit, path, subpath):
    source_path = os.path.join(path, subpath)
    os.system(f'git clone --branch={branch} {url} {source_path}')
    os.system(f"cd {source_path} && git checkout {commit}")


# Default configuration


test_config = {
    'env': 'dev',
    'driver': 'Firefox',
    'driver_path': os.path.join(current_dir, 'webdriver'),
    'source_path': os.path.join(current_dir, 'sources'),
    'test_app_path': os.path.join(current_dir, 'suites'),
    'cache_path': os.path.join(current_dir, 'cached'),
    'output_path': os.path.join(current_dir, 'results'),
    'cacheToken': False,
}

parser = argparse.ArgumentParser(
    description='Automation Project.')
parser.add_argument('operation', action='store', choices=[
    'run', 'setup', 'clean'], help='Specify operation')
parser.add_argument('--env', action='store', choices=['dev','dev_2', 'docker', 'uat', 'dev2', "pipeline"],
                    default='dev', help='Environment directive')
parser.add_argument('--suite', action='append', help='Specify test suite')
parser.add_argument('--test', action='append', help='Specify test case name')
parser.add_argument('--headless', action='store_true', help='Specify if the test should run in a headless browser')
parser.add_argument('--tag', action='append', help='Specify test case name')
parser.add_argument('--browser', dest='driver',
                    choices=['Chrome', 'Firefox', 'Edge'], default='Firefox', help='Test browser')
parser.add_argument('--cache-token', action="store_true", dest="cacheToken",
                    help='Specify if login token should be cached for next time run')
parser.add_argument('--output-path', action="store",
                    help='Specify test output location (log, screenshot, etc)')
parser.add_argument('--output-file', action="store",
                    help='Specify test output file location (output.xml file)')
parser.add_argument('--webdriver-path', action="store", dest="driver_path", help='Specify webdriver location')
parser.add_argument('--removekeywords', action="store_true", help='Remove keywords in report')
parser.add_argument('--parallel', action="store_true", help='define to run with pabot(parallel robot) or robot')
parser.add_argument('--ordering', action="store", help='define suites in parallel')
parser.add_argument('--dryrun', action="store", help='robot dryrun')
parser.add_argument('--rerunfailed', action="store", help='Rerun test script')

for key, value in vars(parser.parse_args()).items():
    if value is not None:
        test_config[key] = value

default = 'dev'
# Importing environment variable
with open(os.path.join(current_dir,'config_{}.yaml').format(test_config.get('env'))) as file:
    env_list = yaml.load(file, Loader=yaml.FullLoader)

try:
    driver_path = test_config.get('driver_path', '')
    # Driver manager configuration
    driver_manager = None
    if test_config.get('driver') == 'Chrome':
        driver_manager = ChromeDriverManager(webdriver_root=driver_path)
    elif test_config.get('driver') == 'Firefox':
        driver_manager = GeckoDriverManager(webdriver_root=driver_path)
    elif test_config.get('driver') == 'Edge':
        driver_manager = EdgeChromiumDriverManager(webdriver_root=driver_path)

    if test_config.get('operation') == 'run':
        if os.path.exists(driver_path) and os.path.isfile(driver_path):
            browserExecutablePath = driver_path
        else:
            browserExecutablePath = os.path.join(
                driver_manager.get_download_path(version='compatible'), driver_manager.get_driver_filename())
            if not os.path.exists(browserExecutablePath):
                print('Compatible webdriver is not installed, processing installation')
                driver_manager.download_and_install()

        if test_config.get('env') == 'docker':
            if not os.path.exists(test_config.get('source_path')):
                print('Setting up code sources')
                remote = env_list['remote']
                if remote and remote['frontend'] and remote['backend']:
                    print('Setting up backend source')
                    setup_git_repo(remote['backend']['url'], remote['backend']['branch'], remote['backend']['commit'],
                                   test_config.get('source_path'), 'backend')
                    print('Setting up frontend source')
                    setup_git_repo(remote['frontend']['url'], remote['frontend']['branch'],
                                   remote['frontend']['commit'], test_config.get('source_path'), 'frontend')
                    print('Building docker container:')
                    os.system('docker-compose build')
                    print('Starting up container for the first time:')
                    os.system('docker-compose up -d')
                    sleep(50)
                    os.system('docker-compose stop')
                else:
                    raise Exception(
                        'Remote repository information is not correctly configured, please config them in the env file')
            os.system('docker-compose up -d')
        run_args = []
        if test_config.get('parallel'):
            run_args.extend(['pabot',
                            '--verbose',
                            
            ])
            if test_config.get('ordering'):
                run_args.extend([
                        '--ordering', test_config.get('ordering'),
                        '--processes', '4'
                ])
            else:
                run_args.extend([
                        '--processes', '4'
                ])
        else:
            run_args.extend(['robot'])
        run_args.extend([
                    '-L', 'TRACE',
                    '-v', 'env:' + test_config.get('env'),
                    '-v', 'driver_path:' + browserExecutablePath,
                    '-v', 'cache_path:' + test_config.get('cache_path'),
                    '-v', 'browser:' + test_config.get('driver'),
                    '-e', 'ignore',
                    '-e', 'not-ready'
                    ])
        if test_config.get('output_path'):
            run_args.extend(['--outputdir', test_config.get('output_path')])
        if test_config.get('output_file'):
            run_args.extend(['--output', test_config.get('output_file')])
        if test_config.get('removekeywords'):
            run_args.extend(['--removekeywords', 'passed'])
        if test_config.get('headless'):
            run_args.extend(['-v', 'headless:True'])
        if not env_list.get('database_uri'):
            run_args.extend(['-e', 'db'])
        if test_config.get('suite') is not None:
            for suite in test_config.get('suite'):
                run_args.extend(['--suite', suite])
        if test_config.get('test'):
            for test in test_config.get('test'):
                run_args.extend(['--test', test])
        if test_config.get('tag'):
            for tag in test_config.get('tag'):
                run_args.extend(['-i', tag])
        if test_config.get('cacheToken'):
            run_args.extend(['-v', 'cacheToken:True'])
        if test_config.get('rerunfailed'):
            run_args.extend(['--rerunfailed', test_config.get('rerunfailed')])
        run_args.append(test_config.get('test_app_path'))
        print(run_args)
        #run_cli(run_args)
        for path in execute(run_args):
             print(path, end="")
    elif test_config.get('operation') == 'clean':
        print('Cleaning up...')
        if os.path.exists(test_config.get('driver_path')):
            print('Removing folder {}'.format(test_config.get('driver_path')))
            shutil.rmtree(test_config.get('driver_path'))
        if os.path.exists(test_config.get('source_path')):
            print('Removing folder {}'.format(test_config.get('source_path')))
            shutil.rmtree(test_config.get('source_path'))
except Exception as e:
    print('Execution error:', str(e))
