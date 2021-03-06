from fabric.api import hide, run, env
import time

def run_cmd(cmd):
    with hide('output', 'running', 'warnings'):
        return run(cmd, timeout=1200)

def check(**kwargs):
    ''' Login over SSH and execute shell command '''
    jdata = kwargs['jdata']
    logger = kwargs['logger']

    env.gateway = jdata['data']['gateway']
    env.host_string = jdata['data']['host_string']
    env.user = jdata['data']['username']
    env.key = jdata['data']['sshkey']
    env.shell = "/bin/sh -c"
    env.disable_known_hosts = True
    env.warn_only = True
    env.abort_on_prompts = True
    try:
        results = run_cmd(jdata['data']['cmd'])
        logger.debug("execute-shell-command: requested command" +
                     " returned with exit code {0}".format(results.return_code))
        if results.succeeded:
            return True
        else:
            return False
    except:
        return None
