## G3W Configuration Scripts

This repository contains the scripts to quickly configure a G3W-SUITE instance.


### Installation

Install the module via pip:

```bash
pip install g3w-config-scripts
```

### Usage

#### Development or Production Setup

```bash
g3w_dev_setup configure.properties
```

Where the configuration file is a properties file with the following structure:

```properties
SUITE_REPO_TAG: v3.8.0
SUITE_DOCKER_IMAGE: g3wsuite/g3w-suite:v3.8.x
MY_NEW_BRANCH: v3.8.0_myniceproject
SUITE_SHARED_VOLUME: /myniceproject/
DEBUG: True
FRONTEND: False

# optional plugin setup. Comment out completely to skip
PLUGIN_APP_NAME=myplugin
PLUGIN_REPO=https://github.com/myname/myplugin.git

WEBGIS_PUBLIC_HOSTNAME: v38.g3wsuite.it
G3WSUITE_POSTGRES_PASS: myPgPasswd
PG_SERVICE_CONF: [service@111.111.11.111]|host=111.111.11.111user=myuser|password=mypwd|dbname=mydb|port=5432
```

#### Configuration generation

Don't have a config.properties file? No problem, you can generate one with the following command:

```bash
g3w_config_gen
```

This will generate a config.properties file in the current directory based on the answers given by the user.

#### Branding

Place yourself in the same folder in which you ran the setup scripts and just run the 
branding module:

```bash
g3w_branding
```

You will be askef for all the possible branding parameters.

