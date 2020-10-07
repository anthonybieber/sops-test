import os
import yaml

print(os.environ)
# os.environ["ENV"] = "staging"
env = os.environ['ENV']

config_dict = {}
if env == 'local':
    config_dict = yaml.load(open('./configs/dev.yml'))
if env == 'staging':
    config_dict = yaml.load(open('./configs/staging.yml'))
if env == 'production':
    config_dict = yaml.load(open('./configs/production.yml'))

print(config_dict)
print(config_dict['db'])
print(config_dict['api'])
