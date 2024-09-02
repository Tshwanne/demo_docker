from subprocess import call
import os 

def Deps(force_reinstall):

    if not force_reinstall and os.path.exists('/usr/local/lib/python3.10/dist-packages/safetensors'):
        os.environ['PYTHONWARNINGS'] = 'ignore'
    else:
        
        call('pip install --root-user-action=ignore --disable-pip-version-check --no-deps -qq gdown numpy==1.23.5 accelerate==0.12.0 --force-reinstall',
             shell=True, stdout=open('/dev/null', 'w'))
        if os.path.exists('diffusers'):
            call("rm -r diffusers", shell=True)
        if not os.path.exists('cache'):
            call('mkdir cache', shell=True)
        call("sed -i 's@~/.cache@/workspace/cache@' /usr/local/lib/python3.10/dist-packages/transformers/utils/hub.py", shell=True)
        call("git clone --depth 1 -q --branch main https://github.com/Tshwanne/diffusers",
             shell=True, stdout=open('/dev/null', 'w'))
        os.environ['PYTHONWARNINGS'] = 'ignore'
